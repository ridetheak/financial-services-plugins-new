// arctic-edge/lib/pit-fundamentals.js
//
// Point-in-time fundamentals client for Arctic Edge, sourced from the SEC
// XBRL Company Facts API (free, no key, authoritative).
//
// Point-in-time semantics: given an as-of date, we return the observation
// that was ON THE PUBLIC RECORD at that date. That is, `filed <= asOfDate`,
// then take the latest `end`. Restatements filed later are NOT retroactively
// visible — the tearsheet cites what the advisor could actually have known.
//
// Data source:
//   https://data.sec.gov/api/xbrl/companyfacts/CIK{padded}.json
//   https://www.sec.gov/files/company_tickers.json
//
// CORS: SEC endpoints are generally CORS-permissive but occasionally reject
// browser-set User-Agent headers. When direct fetch fails, the consumer UI
// should present a paste-JSON fallback (advisor opens the URL, copies JSON).
// The compliance-recommended production path is a firm-hosted proxy per
// arctic-edge/compliance/13-data-handling.md.
//
// This library is intentionally dependency-free and browser-native.

(function () {
  const NS = (window.ArcticEdge = window.ArcticEdge || {});
  if (NS.PIT) return; // idempotent

  const TICKER_MAP_URL = "https://www.sec.gov/files/company_tickers.json";
  const COMPANY_FACTS_URL = (cik) =>
    `https://data.sec.gov/api/xbrl/companyfacts/CIK${String(cik).padStart(10, "0")}.json`;
  const TICKER_CACHE_KEY = "ae.pit.tickers.v1";
  const TICKER_CACHE_TTL_MS = 7 * 24 * 60 * 60 * 1000; // 7 days

  // ── Concept map: aliases per metric, tried in order ─────────────────
  // Each metric maps to a list of us-gaap concepts. Companies tag things
  // differently; we try each until we find data. The `unit` is the preferred
  // XBRL unit key returned by the API ('USD', 'shares', 'pure', 'USD/shares').
  const CONCEPTS = {
    revenue: {
      unit: "USD",
      tags: [
        "Revenues",
        "RevenueFromContractWithCustomerExcludingAssessedTax",
        "SalesRevenueNet",
        "RevenueFromContractWithCustomerIncludingAssessedTax",
      ],
    },
    netIncome: {
      unit: "USD",
      tags: ["NetIncomeLoss", "ProfitLoss"],
    },
    operatingCashFlow: {
      unit: "USD",
      tags: [
        "NetCashProvidedByUsedInOperatingActivities",
        "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations",
      ],
    },
    capex: {
      unit: "USD",
      tags: [
        "PaymentsToAcquirePropertyPlantAndEquipment",
        "PaymentsToAcquireProductiveAssets",
      ],
    },
    totalAssets: {
      unit: "USD",
      tags: ["Assets"],
    },
    totalLiabilities: {
      unit: "USD",
      tags: ["Liabilities"],
    },
    stockholdersEquity: {
      unit: "USD",
      tags: [
        "StockholdersEquity",
        "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest",
      ],
    },
    longTermDebt: {
      unit: "USD",
      tags: ["LongTermDebtNoncurrent", "LongTermDebt"],
    },
    sharesOutstanding: {
      unit: "shares",
      tags: [
        "CommonStockSharesOutstanding",
        "EntityCommonStockSharesOutstanding",
      ],
    },
    epsDiluted: {
      unit: "USD/shares",
      tags: [
        "EarningsPerShareDiluted",
        "IncomeLossFromContinuingOperationsPerDilutedShare",
      ],
    },
  };

  // ── Utilities ───────────────────────────────────────────────────────
  const iso = (d) => (d instanceof Date ? d.toISOString().slice(0, 10) : String(d));
  const daysBetween = (a, b) =>
    Math.round((new Date(a) - new Date(b)) / (24 * 3600 * 1000));

  function cached(key, ttl) {
    try {
      const raw = localStorage.getItem(key);
      if (!raw) return null;
      const { at, value } = JSON.parse(raw);
      if (Date.now() - at > ttl) return null;
      return value;
    } catch {
      return null;
    }
  }
  function setCached(key, value) {
    try {
      localStorage.setItem(key, JSON.stringify({ at: Date.now(), value }));
    } catch {}
  }

  // ── Ticker → CIK ────────────────────────────────────────────────────
  // The SEC's company_tickers.json is a small map; we cache it locally so
  // we hit the network once per week per browser.
  async function loadTickerMap() {
    const c = cached(TICKER_CACHE_KEY, TICKER_CACHE_TTL_MS);
    if (c) return c;
    const res = await fetch(TICKER_MAP_URL, { headers: { Accept: "application/json" } });
    if (!res.ok) throw new Error(`ticker map fetch failed: HTTP ${res.status}`);
    const raw = await res.json();
    // raw = { "0": {cik_str:320193, ticker:"AAPL", title:"Apple Inc."}, ... }
    const map = {};
    for (const k in raw) {
      const r = raw[k];
      map[r.ticker.toUpperCase()] = { cik: r.cik_str, name: r.title };
    }
    setCached(TICKER_CACHE_KEY, map);
    return map;
  }

  async function resolveCIK(ticker) {
    const t = String(ticker || "").toUpperCase().trim();
    if (!t) throw new Error("ticker required");
    const map = await loadTickerMap();
    const hit = map[t];
    if (!hit) throw new Error(`ticker not found in SEC map: ${t}`);
    return hit; // { cik, name }
  }

  // ── Company Facts fetch ─────────────────────────────────────────────
  async function fetchCompanyFacts(cik) {
    const url = COMPANY_FACTS_URL(cik);
    const res = await fetch(url, { headers: { Accept: "application/json" } });
    if (!res.ok) throw new Error(`company facts fetch failed: HTTP ${res.status}`);
    return await res.json();
  }

  // ── PIT extraction ──────────────────────────────────────────────────
  // Pick the observation for a concept that (a) was filed on or before the
  // as-of date, (b) has the latest `end` among those, and (c) matches the
  // requested unit. Returns { val, end, filed, form, accn, tag } or null.
  function pickPIT(concept, asOfDate, unit) {
    if (!concept || !concept.units || !concept.units[unit]) return null;
    const rows = concept.units[unit].filter((r) => r.filed <= asOfDate);
    if (!rows.length) return null;
    // Prefer 10-K / 10-Q over 8-K amendments for stability. Then latest end.
    const rank = (f) => (f === "10-K" ? 3 : f === "10-Q" ? 2 : f && f.startsWith("10-K/A") ? 1 : 0);
    rows.sort((a, b) => {
      if (a.end !== b.end) return a.end < b.end ? 1 : -1; // desc by end
      return rank(b.form) - rank(a.form);
    });
    return rows[0];
  }

  // For flow items (revenue, net income, OCF, CapEx), we want TTM. We build
  // TTM from the four most recent quarterly points or take an annual point.
  // The company_facts API distinguishes quarters via 'fp' (Q1..Q4, FY). We
  // return either the FY annual point or a stitched TTM of trailing quarters.
  function pickFlowTTM(concept, asOfDate, unit) {
    if (!concept || !concept.units || !concept.units[unit]) return null;
    const rows = concept.units[unit].filter(
      (r) => r.filed <= asOfDate && r.fp && (r.fp === "FY" || /^Q[1-4]$/.test(r.fp))
    );
    if (!rows.length) return null;
    // Group by (end, form) — sometimes duplicates exist.
    const byEnd = new Map();
    for (const r of rows) {
      const key = r.end;
      const prev = byEnd.get(key);
      if (!prev || prev.filed < r.filed) byEnd.set(key, r);
    }
    const uniq = Array.from(byEnd.values()).sort((a, b) => (a.end < b.end ? 1 : -1));
    // Preferred: latest FY annual point.
    const fy = uniq.find((r) => r.fp === "FY");
    if (fy) return { val: fy.val, end: fy.end, filed: fy.filed, form: fy.form, accn: fy.accn, method: "FY" };
    // Fallback: stitch trailing 4 quarters ending at latest available quarter.
    const quarters = uniq.filter((r) => /^Q[1-4]$/.test(r.fp));
    if (quarters.length < 4) {
      // Not enough quarters — return the single most recent observation as-is.
      if (quarters.length) {
        const q = quarters[0];
        return { val: q.val, end: q.end, filed: q.filed, form: q.form, accn: q.accn, method: `single-${q.fp}` };
      }
      return null;
    }
    const trailing = quarters.slice(0, 4);
    const sum = trailing.reduce((s, r) => s + r.val, 0);
    return {
      val: sum,
      end: trailing[0].end,
      filed: trailing.reduce((mx, r) => (r.filed > mx ? r.filed : mx), "0000-00-00"),
      form: trailing.map((t) => t.form).join(","),
      accn: trailing.map((t) => t.accn).join(","),
      method: "TTM(Q1+Q2+Q3+Q4)",
    };
  }

  // ── Snapshot extraction ─────────────────────────────────────────────
  function extractSnapshot(facts, asOfDate) {
    if (!facts || !facts.facts) throw new Error("company facts payload has no `facts` field");
    const gaap = facts.facts["us-gaap"] || {};
    const dei = facts.facts.dei || {};

    function pull(metric, mode = "point") {
      const spec = CONCEPTS[metric];
      if (!spec) return null;
      for (const tag of spec.tags) {
        const concept = gaap[tag] || dei[tag];
        if (!concept) continue;
        const val =
          mode === "flow" ? pickFlowTTM(concept, asOfDate, spec.unit) : pickPIT(concept, asOfDate, spec.unit);
        if (val) return { tag, ...val };
      }
      return null;
    }

    const snapshot = {
      asOfDate,
      entity: { cik: facts.cik, name: facts.entityName },
      lines: {
        revenue: pull("revenue", "flow"),
        netIncome: pull("netIncome", "flow"),
        operatingCashFlow: pull("operatingCashFlow", "flow"),
        capex: pull("capex", "flow"),
        totalAssets: pull("totalAssets", "point"),
        totalLiabilities: pull("totalLiabilities", "point"),
        stockholdersEquity: pull("stockholdersEquity", "point"),
        longTermDebt: pull("longTermDebt", "point"),
        sharesOutstanding: pull("sharesOutstanding", "point"),
        epsDiluted: pull("epsDiluted", "flow"),
      },
    };

    // Derived metrics — computed only when both inputs are available.
    const L = snapshot.lines;
    const derived = {};
    if (L.revenue && L.netIncome) derived.netMarginPct = +((L.netIncome.val / L.revenue.val) * 100).toFixed(2);
    if (L.operatingCashFlow && L.capex)
      derived.freeCashFlow = { val: L.operatingCashFlow.val - L.capex.val, method: "OCF - CapEx" };
    if (L.netIncome && L.stockholdersEquity && L.stockholdersEquity.val > 0)
      derived.roePct = +((L.netIncome.val / L.stockholdersEquity.val) * 100).toFixed(2);
    if (L.netIncome && L.totalAssets && L.totalAssets.val > 0)
      derived.roaPct = +((L.netIncome.val / L.totalAssets.val) * 100).toFixed(2);
    if (L.longTermDebt && L.stockholdersEquity && L.stockholdersEquity.val > 0)
      derived.debtToEquity = +(L.longTermDebt.val / L.stockholdersEquity.val).toFixed(2);
    if (L.stockholdersEquity && L.sharesOutstanding && L.sharesOutstanding.val > 0)
      derived.bookValuePerShare = +(L.stockholdersEquity.val / L.sharesOutstanding.val).toFixed(2);

    snapshot.derived = derived;

    // Prior-year revenue for growth rate. We pull the observation ending in
    // approximately (revenue.end - 365 days), tolerant to +/- 100 days.
    if (L.revenue && facts.facts["us-gaap"]) {
      const target = new Date(L.revenue.end);
      target.setDate(target.getDate() - 365);
      const targetIso = iso(target);
      const rows = [];
      for (const tag of CONCEPTS.revenue.tags) {
        const c = gaap[tag];
        if (c && c.units && c.units.USD) rows.push(...c.units.USD);
      }
      const candidates = rows
        .filter(
          (r) =>
            r.filed <= asOfDate &&
            (r.fp === "FY" ||
              (L.revenue.method !== "FY" && /^Q[1-4]$/.test(r.fp)))
        )
        .filter((r) => Math.abs(daysBetween(r.end, targetIso)) < 100);
      candidates.sort(
        (a, b) => Math.abs(daysBetween(a.end, targetIso)) - Math.abs(daysBetween(b.end, targetIso))
      );
      const prev = candidates[0];
      if (prev) {
        snapshot.derived.revenuePriorYear = { val: prev.val, end: prev.end };
        snapshot.derived.revenueGrowthPct = +(
          ((L.revenue.val - prev.val) / prev.val) * 100
        ).toFixed(2);
      }
    }

    // Citation summary — every line's origin, deduped by accession.
    const cites = new Map();
    for (const [_metric, obs] of Object.entries(L)) {
      if (!obs) continue;
      // Flow-TTM may contain a comma-separated list of accessions.
      const accs = String(obs.accn || "").split(",").filter(Boolean);
      for (const a of accs) {
        if (!cites.has(a))
          cites.set(a, {
            accession: a,
            form: obs.form,
            filed: obs.filed,
            url: `https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=${facts.cik}&type=&dateb=&owner=include&count=40`,
          });
      }
    }
    snapshot.citations = Array.from(cites.values()).sort((a, b) => (a.filed < b.filed ? 1 : -1));
    snapshot.contract = "pit-fundamentals/v1";
    snapshot.source = "SEC XBRL Company Facts";
    snapshot.retrievedAt = new Date().toISOString();
    return snapshot;
  }

  // ── High-level API ──────────────────────────────────────────────────
  async function getPITFundamentals(ticker, asOfDate) {
    const asOf = iso(asOfDate);
    const { cik, name } = await resolveCIK(ticker);
    const facts = await fetchCompanyFacts(cik);
    const snap = extractSnapshot(facts, asOf);
    snap.entity.name = snap.entity.name || name;
    snap.entity.ticker = String(ticker).toUpperCase();
    return snap;
  }

  // Parse a Company Facts JSON pasted from the browser (CORS-fallback path).
  function extractFromPastedJSON(jsonText, asOfDate) {
    const facts = typeof jsonText === "string" ? JSON.parse(jsonText) : jsonText;
    return extractSnapshot(facts, iso(asOfDate));
  }

  NS.PIT = {
    resolveCIK,
    fetchCompanyFacts,
    extractSnapshot,
    getPITFundamentals,
    extractFromPastedJSON,
    COMPANY_FACTS_URL,
    _CONCEPTS: CONCEPTS,
  };
})();
