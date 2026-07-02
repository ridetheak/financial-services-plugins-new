# Tool Composition Playbook

**Purpose:** The highest-value combinations of the 17 AE skill tools and the
288 OpenBB tools, ranked by advisor time saved × frequency of use ×
compliance leverage. Each combination is a specific advisor workflow with a
named Arctic Edge module hand-off.

**Scoring lens:** A combination is high-value only if it (a) solves a task
advisors do at least monthly, (b) currently takes 30+ minutes of manual
work, (c) produces an artifact that feeds an Arctic Edge module and enters
the compliance record, and (d) uses tools that have been verified to return
real data.

---

## Tool inventory (short reference)

**AE skill tools (17)** — built on top of OpenBB + FMP; every gauge cites
its source.

| Tool | Output |
|---|---|
| `ae_route` / `ae_suggest` / `ae_refresh` | Router for skill selection |
| `glance` | 15-gauge one-page read: risk, vol, growth, dividend, valuation-vs-peers, analyst view, moat proxy, liquidity, momentum, trend, quality (Piotroski), insider, revisions |
| `capm` | Cost of equity |
| `graham-value` | Graham value screen |
| `reverse-dcf` | Growth priced in at current price |
| `comps` | Peer multiples table |
| `capital-allocation` | Buybacks / dividends / capex / M&A framework |
| `dividend-safety` | Payout, coverage, growth durability |
| `moat-durability` | 10-year moat scorecard |
| `estimate-revisions` | IBES-style revision momentum |
| `eva-spread` | Economic value added spread (ROIC – WACC) |
| `financial-scores` | Piotroski F, Altman Z, composite |
| `fair_value_triangulation` | Multi-method fair value range |
| `valuation-context` | Where the multiple sits historically |

**OpenBB (288)** — organized broadly:

- Equity: price/quote/history, fundamentals, estimates, ownership,
  discovery, screener, market snapshots
- EDGAR: 13F holders/holdings, Form 4 (insider), full-text search,
  sector flow aggregate
- Options / derivatives: chains, snapshots, unusual, Databento flow,
  futures curves
- Economy: FRED, BLS, EIA, FOMC, treasury, yield curve, CPI, PCE, GDP,
  SLOOS, employment
- Fixed income: treasury rates, yield curve, corporate HQM, spot rates,
  rate forecasts
- Schwab (`sw_*`): live positions, orders, quotes, transactions,
  option chain, options trading, movers
- FMP: DCF, key metrics, grades, historical ratings, price targets
- ETF: search, holdings, exposure, sectors, N-PORT disclosures
- Index: constituents, sectors, snapshots
- Currency, crypto, commodities (incl. EIA petroleum)
- News: company, world
- Sentiment: Adanos (`adanos_*`), FinBERT (`sentiment_pulse`)
- Fama-French: factors, portfolio returns
- QuantLib (`ql_*`): bonds, options, swaps, yield curves
- TradingView (`tv_*`): charts
- Vector Vest (`vv_*`): forecast horizons, VaR/OaR, narrative alignment
- Fintel-style ownership, zombie scanner, famous-investor reverse screen
- Composite tools: `peer_comparison`, `portfolio_risk_decomposition`,
  `sentiment_pulse`, `risk_analysis`, `regret_analysis`, `macro_snapshot`,
  `cross_investor_consensus`, `company_briefing`, `earnings_review`

---

## The Top 10 Combinations

### 1. Pre-Trade Recommendation Dossier  ★★★★★

**Advisor task:** "I'm considering recommending X. Give me everything I need
to write a defensible thesis in 30 seconds."

**Tools (chained):**

| Step | Tool | Purpose |
|---|---|---|
| 1 | `AE.glance` | 15-gauge triage read |
| 2 | `AE.moat-durability` | 10-year moat evidence (if glance moat proxy is high) |
| 3 | `AE.reverse-dcf` | What growth is priced in at today's price |
| 4 | `AE.fair_value_triangulation` | Multi-method fair value range |
| 5 | `AE.comps` | Peer multiples context |
| 6 | `AE.estimate-revisions` | Analyst revision momentum |
| 7 | `OpenBB.edgar_form4_recent` | Insider buying/selling cluster |
| 8 | `OpenBB.equity_ownership_form_13f` | Institutional footprint |
| 9 | `OpenBB.adanos_stock_sentiment` | Sentiment overlay |
| 10 | `OpenBB.news_company` | Recent material news |

**Output artifact:** A `pre-trade-dossier/v1` bundle that populates:
- **Module 4 (Trade Thesis)** — variant perception (glance gauges vs.
  Street), catalyst (revisions + upcoming news), exit condition (fair-value
  triangulation range).
- **Module 6 (Reg BI Note)** — `care-basis` field, `alternatives` field
  (comps peer list), risks (glance risk + volatility gauges), costs
  (glance provides expense ratio / dividend yield).

**Time saved:** ~45 minutes of research per recommendation → ~30 seconds.
**Compliance leverage:** Very high — the resulting Reg BI note has every
required element sourced to a citable output. This is the single most
important workflow to enable.

---

### 2. Live Portfolio Concentration + Factor X-Ray  ★★★★★

**Advisor task:** "Show me what my client actually owns after look-through,
and where the factor exposure sits."

**Tools:**

| Step | Tool | Purpose |
|---|---|---|
| 1 | `OpenBB.sw_positions` | Live holdings from Schwab |
| 2 | `OpenBB.etf_holdings` | ETF constituents for look-through |
| 3 | `OpenBB.etf_equity_exposure` | Reverse — which ETFs hold a name |
| 4 | `OpenBB.equity_compare_company_facts` | Aggregate underlying exposures |
| 5 | `OpenBB.portfolio_risk_decomposition` | Factor decomposition |
| 6 | `OpenBB.famafrench_factors` | Factor returns for context |
| 7 | `OpenBB.risk_analysis` | Structured risk output |

**Output artifact:** A `concentration-xray/v2` with look-through single-name
net + gross exposure per underlying name across household + factor loading
(market, size, value, momentum, quality, low-vol).

**Feeds:**
- **Module 9 (Concentration X-Ray)** — replaces the current hand-entered
  weight approximation with a live custodian-sourced view.
- **Module 3 (Portfolio Risk Analyzer)** — replaces the single-correlation
  parametric estimate with a factor-decomposition-anchored risk figure.

**Time saved:** ~2 hours of spreadsheet work per quarterly review → ~10
seconds. **Compliance leverage:** Very high — the Reg BI Care Obligation
requires understanding concentration risk; this is the auditable evidence.

---

### 3. Ongoing Thesis-Break Monitor  ★★★★★

**Advisor task:** "Which of my clients' positions have thesis breaks I
should call about before their next quarterly review?"

**Tools (batch over `sw_positions`):**

| Step | Tool | Purpose |
|---|---|---|
| 1 | `OpenBB.sw_positions` | Positions across household |
| 2 | `AE.estimate-revisions` | Estimate direction per holding |
| 3 | `AE.moat-durability` | Moat still intact? |
| 4 | `AE.eva-spread` | Economic value still positive? |
| 5 | `OpenBB.fmp_grades_historical` | Analyst rating history |
| 6 | `OpenBB.news_company` | Recent material news |
| 7 | `OpenBB.adanos_stock_sentiment` | Sentiment trajectory |
| 8 | `OpenBB.regret_analysis` | "Should I have exited earlier" signal |

**Output artifact:** A `thesis-monitor/v1` — per-position status: green
(thesis intact), amber (one deterioration signal), red (multiple signals or
material news).

**Feeds:**
- **Module 4 (Trade Thesis)** — close-out flow. When a red flag fires, the
  advisor opens the original thesis, decides to keep or exit, and closes
  the record with outcome (thesis correct / wrong / partial / untested).
- **Module 5 (Audit Trail)** — a decision to exit becomes a new
  recommendation event.

**Time saved:** ~4 hours of book review per quarter → ~30 seconds.
**Compliance leverage:** Very high — it demonstrates ongoing monitoring
under Adviser Act duty of care and provides the evidentiary basis for
exit recommendations.

---

### 4. Income / Dividend Safety Review  ★★★★

**Advisor task:** "Which dividends in my client's income book are safe,
which are at risk, and which are actually paid out of ROC?"

**Tools:**

| Step | Tool | Purpose |
|---|---|---|
| 1 | `OpenBB.sw_positions` | Holdings with yield > 2% |
| 2 | `AE.dividend-safety` | Per-position safety score |
| 3 | `OpenBB.fmp_owner_earnings` | FCF anchor for payout |
| 4 | `AE.eva-spread` | Is the business earning its cost of capital |
| 5 | `OpenBB.equity_fundamental_trailing_dividend_yield` | Verified yields |
| 6 | `OpenBB.equity_calendar_dividend` | Upcoming ex-dividend dates |
| 7 | `OpenBB.equity_fundamental_ratios` | Payout ratio history |

**Output artifact:** A `income-review/v1` — per-position: yield, payout %,
FCF coverage, EVA spread, risk tier (safe / watch / cut probable).

**Feeds:**
- **Module 6 (Reg BI Note)** — for retirees, the note's `care-basis` cites
  yield safety not just yield level.
- **Module 4 (Trade Thesis)** — for income names, the exit condition is
  "dividend cut or FCF coverage drops below 1.2x."

**Time saved:** ~90 minutes per client per quarter for income books.
**Compliance leverage:** High — many yield-chasing recommendations that
draw exam scrutiny are precisely the ones where the payout is unsafe.

---

### 5. Options Income Overlay Screener  ★★★★

**Advisor task:** "On which of my client's long positions can I sell
covered calls this month for meaningful income without giving up upside I
care about?"

**Tools:**

| Step | Tool | Purpose |
|---|---|---|
| 1 | `OpenBB.sw_positions` | Long positions of 100+ shares |
| 2 | `OpenBB.sw_option_chain` | Live chain (Schwab) |
| 3 | `OpenBB.derivatives_options_chains` | Alt chain (Databento/FMP) |
| 4 | `OpenBB.ql_option` | Black-Scholes fair value |
| 5 | `OpenBB.ql_implied_vol` | IV context |
| 6 | `OpenBB.derivatives_options_unusual` | Where flow is concentrated |
| 7 | `OpenBB.databento_options_flow` | Institutional flow |
| 8 | `AE.fair_value_triangulation` | Sanity — is the strike above fair value? |

**Output artifact:** A `covered-call-candidates/v1` list — for each
qualifying position: recommended strike / expiry, premium, annualized
income %, delta, break-even.

**Feeds:**
- **Module 6 (Reg BI Note)** — options recommendations require additional
  disclosures under FINRA 2360; the note template includes an options
  variant (out of Phase 1 scope but this composition prepares for it).
- **Module 5 (Audit Trail)** — the recommendation event is captured with
  origin.

**Time saved:** ~2 hours per client per month for options-eligible books.
**Compliance leverage:** Medium-high — options recommendations are highly
regulated (FINRA 2360, OCC OCD delivery); a structured output reduces
gaps.

---

### 6. Earnings-Week Prep Kit  ★★★★

**Advisor task:** "Which of my clients' positions have earnings next week,
and what should I be watching?"

**Tools:**

| Step | Tool | Purpose |
|---|---|---|
| 1 | `OpenBB.sw_positions` | Held names |
| 2 | `OpenBB.equity_calendar_earnings` | Earnings calendar filter |
| 3 | `AE.estimate-revisions` | Recent revisions per name |
| 4 | `OpenBB.equity_estimates_consensus` | Consensus expectations |
| 5 | `OpenBB.equity_fundamental_transcript` | Last quarter's guidance |
| 6 | `OpenBB.databento_options_flow` | What options traders expect |
| 7 | `OpenBB.derivatives_options_surface` | IV term structure |
| 8 | `OpenBB.adanos_stock_sentiment` | Sentiment going in |
| 9 | `OpenBB.earnings_review` | Post-earnings comparison (day after) |

**Output artifact:** A weekly `earnings-prep/v1` per client — held names
reporting this week, consensus expectations, implied move from options,
sentiment.

**Feeds:**
- **Module 4 (Trade Thesis)** — updates to the thesis' catalyst field
  after earnings.
- **Module 6 (Reg BI Note)** — a proactive check-in note to the client
  before earnings can cite the specific data.

**Time saved:** ~1 hour per week per advisor. **Compliance leverage:**
Medium — proactive communication is not required by rule but is best
practice under Adviser Act duty of care.

---

### 7. Macro Regime Overlay  ★★★

**Advisor task:** "What's the macro backdrop I should reference in this
client's next quarterly review?"

**Tools:**

| Step | Tool | Purpose |
|---|---|---|
| 1 | `OpenBB.macro_snapshot` | Composite regime read |
| 2 | `OpenBB.fixedincome_government_yield_curve` | Curve shape |
| 3 | `OpenBB.fixedincome_rate_effr_forecast` | Fed path |
| 4 | `OpenBB.economy_fomc_documents` | Recent FOMC positioning |
| 5 | `OpenBB.economy_composite_leading_indicator` | Cycle position |
| 6 | `OpenBB.economy_survey_sloos` | Credit conditions |
| 7 | `OpenBB.economy_pce` | Inflation |
| 8 | `OpenBB.economy_indicators` | Broad indicators |
| 9 | `OpenBB.equity_market_snapshots` | Risk-on/risk-off flavor |

**Output artifact:** A `macro-regime/v1` — one-page context that references
specific numbers and dates.

**Feeds:**
- **Module 6 (Reg BI Note)** — the `care-basis` field can cite specific
  macro conditions ("given the inverted yield curve as of X…") rather than
  the vague "market conditions" language that gets flagged in exams.

**Time saved:** ~20 minutes per note. **Compliance leverage:** Medium —
specificity beats vagueness in exam defense.

---

### 8. Fixed-Income Duration & Rate-Sensitivity  ★★★★

**Advisor task:** "What's the actual duration of my client's fixed-income
sleeve and how sensitive is it to a 100bp move?"

**Tools:**

| Step | Tool | Purpose |
|---|---|---|
| 1 | `OpenBB.sw_positions` | Fixed-income holdings |
| 2 | `OpenBB.fixedincome_government_yield_curve` | Base curve |
| 3 | `OpenBB.fixedincome_corporate_hqm` | Corporate spreads |
| 4 | `OpenBB.fixedincome_government_treasury_rates` | Point rates |
| 5 | `OpenBB.ql_yield_curve` | Curve construction |
| 6 | `OpenBB.ql_bond` | Bond pricing / duration |
| 7 | `OpenBB.fixedincome_rate_effr_forecast` | Rate path scenarios |

**Output artifact:** A `fixed-income-analytics/v1` — per-holding modified
duration, portfolio-weighted duration, DV01, ±100bp scenario table.

**Feeds:**
- **Module 3 (Portfolio Risk Analyzer)** — fixed-income sleeve gets a
  proper duration-based risk analysis rather than a rough vol/beta
  approximation.
- **Module 6 (Reg BI Note)** — rate risk disclosure has specific numbers.

**Time saved:** ~1 hour per fixed-income-heavy client per review cycle.
**Compliance leverage:** High for retirees / conservative books.

---

### 9. 13F + Insider "Smart Money" Consensus  ★★★

**Advisor task:** "Who else is buying this name? Is there evidence beyond
my own thesis?"

**Tools:**

| Step | Tool | Purpose |
|---|---|---|
| 1 | `OpenBB.edgar_13f_holders` | Institutional holders |
| 2 | `OpenBB.edgar_13f_holdings` | What they hold |
| 3 | `OpenBB.edgar_form4_by_cluster` | Clustered insider buying |
| 4 | `OpenBB.edgar_form4_recent` | Recent insider activity |
| 5 | `OpenBB.edgar_sector_flow_aggregate` | Sector-level flow |
| 6 | `OpenBB.equity_ownership_insider_trading` | Verified insider stream |
| 7 | `OpenBB.famous_investor_reverse_screen` | What top investors hold |
| 8 | `OpenBB.cross_investor_consensus` | Overlap analysis |

**Output artifact:** A `smart-money/v1` — institutional and insider
positioning on the name, with recent trend.

**Feeds:**
- **Module 4 (Trade Thesis)** — supporting evidence for the variant
  perception ("if we're right, [institution X] is early too").

**Time saved:** ~30 minutes per name researched. **Compliance leverage:**
Low-medium — supporting evidence, not required documentation.

---

### 10. Zombie / Credit Quality Screen  ★★★

**Advisor task:** "Are there any credit-risk time bombs in this book I've
missed?"

**Tools:**

| Step | Tool | Purpose |
|---|---|---|
| 1 | `OpenBB.sw_positions` | All holdings |
| 2 | `OpenBB.zombie_scanner` | Zombie flag (interest coverage < 1 for 3y) |
| 3 | `AE.financial-scores` | Piotroski F / Altman Z |
| 4 | `OpenBB.equity_fundamental_ratios` | Solvency check |
| 5 | `AE.moat-durability` | Business durability |
| 6 | `OpenBB.fmp_financial_growth` | Growth trajectory |

**Output artifact:** A `credit-quality-screen/v1` — flags any position
showing Altman distress zone or zombie characteristics.

**Feeds:**
- **Module 3 (Portfolio Risk Analyzer)** — same-direction flag if
  multiple positions in distress zone.
- **Module 6 (Reg BI Note)** — a hold recommendation on a zombie name
  requires additional care-basis documentation.

**Time saved:** ~45 minutes per book review. **Compliance leverage:**
High for accounts with equity income mandates in cyclical names.

---

## Prioritization matrix

If we can only build the first three integrations into Arctic Edge, the
order is:

1. **#1 Pre-Trade Recommendation Dossier** — highest workflow leverage,
   directly feeds three modules, highest compliance value.
2. **#2 Live Portfolio Concentration + Factor X-Ray** — makes Module 9
   real (currently hand-entered) and upgrades Module 3.
3. **#3 Ongoing Thesis-Break Monitor** — makes Module 4 an ongoing tool
   rather than a one-time capture, and demonstrates duty of care over
   the relationship.

The next tier — options overlay (#5), income review (#4), fixed-income
duration (#8) — are book-type specific but very high value for the
matching books.

The remainder are opportunistic tools that flesh out the workstation but
are not gating for a firm rollout.

---

## Architectural note

Each combination is built the same way:
1. A router entry (added to Arctic Edge's `ae_route` if AE-owned) or a
   workstation action button.
2. A parallel fan-out (using `Promise.all` client-side, or a server-side
   parallel MCP call chain) that fetches each tool's output.
3. A composition step that assembles the outputs into a versioned
   contract (`pre-trade-dossier/v1`, etc.).
4. A hand-off step that populates the relevant Arctic Edge module fields.

The version-lock policy (`compliance/12-version-lock.md`) applies:
composition contracts get versioned; changes trigger the same review
workflow as module changes.
