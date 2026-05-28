# Module Compliance Matrix

**Audience:** CCO, Compliance Testing.
**Purpose:** For each of the 10 Phase 1 modules, what rule it touches, what it
produces, and what about it is **deterministic vs. judgmental**.

The distinction between deterministic and judgmental matters. Deterministic
logic produces the same output for the same input and can be tested by
compliance. Judgmental input (the advisor's analysis) is what the
deterministic logic *requires the advisor to capture* — Arctic Edge does not
substitute for it.

---

## Module 1 — IPS Module

| Attribute | Value |
|---|---|
| **Terminal surface** | `section-ips` |
| **Input contract** | Advisor entry |
| **Output contract** | `ips-record/v1` |
| **Persistence** | Client-side (browser localStorage) |
| **Regulated** | No (not regulatory work product; it is operational input to regulatory work product) |
| **Rules touched** | Reg BI Care (15l-1(a)(2)(ii)(B) — investment profile); Adviser Act fiduciary duty of care; FINRA 2111 customer-specific suitability |

**Deterministic logic:**
- Validates asset-class targets sum to 100%.
- Validates min/max bands are internally consistent (min ≤ target ≤ max).
- Stamps `createdAt` ISO 8601 timestamp.

**Judgmental input (advisor enters; system does not infer):**
- Client objectives, time horizon, risk tolerance, risk capacity, liquidity needs.
- Asset-class target percentages and bands.
- Rebalancing rules, prohibited holdings, constraints.

**Why this matters:** The IPS is the yardstick against which every later
recommendation is measured. The Reg BI Care Obligation requires understanding
the customer's investment profile. The IPS Record formalizes that profile in
a structured, machine-readable form that downstream modules (3, 5, 6, 9) can
cite by reference rather than by re-typing.

**What an exam reviewer would see:** A timestamped `ips-record/v1` JSON in
the client file, version-tagged, with all fields populated. When a trade note
references "fits the IPS objective of long-term growth with moderate risk,"
the IPS record is the audit trail behind that claim.

---

## Module 2 — Four-Quadrant Risk Framework

| Attribute | Value |
|---|---|
| **Terminal surface** | `section-risk-framework` |
| **Input contract** | Inputs from Modules 1, 3 (and Phase 2 modules) |
| **Output contract** | `four-quadrant-risk/v1` |
| **Persistence** | Client-side |
| **Regulated** | No |
| **Rules touched** | Reg BI Care (risks). Adviser Act duty of care. |

**Deterministic logic:**
- **Collapse guard** — explicitly blocks assembly if any "combined risk
  score" / "overall risk" / single-number field is present. The four
  quadrants are never collapsed into one number.
- Each quadrant has exactly one producer module.
- Each quadrant is rated low/moderate/high with a plain-language rationale.

**Why this matters:** Many advisor platforms produce a single "risk score"
(often proprietary, often opaque). Regulators have increasingly questioned
whether such scores are reliable measures of customer-specific suitability.
The Four-Quadrant Framework refuses to produce a single score by design —
the advisor must read the four independent views and exercise judgment.

**Compliance benefit:** No single score that can be challenged as
proprietary or unverifiable. Each quadrant cites its own deterministic
inputs.

---

## Module 3 — Portfolio Risk Analyzer

| Attribute | Value |
|---|---|
| **Terminal surface** | `section-portfolio-risk` |
| **Input contract** | Holdings Snapshot, market data |
| **Output contract** | `portfolio-risk/v1` |
| **Persistence** | Client-side; market data via Schwab websocket (firm-managed) |
| **Regulated** | No (operational; output feeds regulated work) |
| **Rules touched** | Reg BI Care (risks/rewards/costs). Adviser Act duty of care. |

**Deterministic logic:**
- Expected return (position-weighted).
- Portfolio volatility (parametric, single-correlation matrix; see assumptions).
- Beta (position-weighted vs. SPX).
- Sharpe ratio (rf-adjusted excess return / volatility).
- Parametric VaR at 95% and 99% confidence, 1-year horizon, mean excluded.
- Maximum drawdown (advisor-supplied lookback or modeled).
- Component risk contributions (sum to 100%).
- Sector concentration percentages.
- Same-direction risk flags: positions with weight ≥ X% and beta ≥ Y; sectors > Z%.

**Method assumptions surfaced in UI:**
- Single average pairwise correlation across positions (vs. full covariance
  matrix). Documented in UI.
- Mean excluded from VaR (conservative — produces higher VaR than
  mean-adjusted variant).
- 1-year horizon (configurable).
- Risk-free rate input (advisor enters; defaults disclosed).

**Why method-assumption disclosure matters:** Reg BI Care requires
"understanding the potential risks." If the firm's risk numbers depend on
method assumptions that aren't disclosed, the documented "understanding" is
incomplete. Arctic Edge shows the assumption alongside the result.

**Suggested Quadrant 1 rating:** The module produces a *suggested* rating
(low/moderate/high) based on volatility and concentration thresholds. The
advisor **confirms or overrides**; the system never sets Quadrant 1
silently.

---

## Module 4 — Trade Thesis Library

| Attribute | Value |
|---|---|
| **Terminal surface** | `section-thesis` |
| **Input contract** | Advisor entry; security reference |
| **Output contract** | `trade-thesis/v1` |
| **Persistence** | Client-side; immutable capture timestamp |
| **Regulated** | No (but high evidentiary value at exam) |
| **Rules touched** | Reg BI Care (reasonable basis); Adviser Act duty of care; basis-for-recommendation under Rule 204-2 / 17a-3. |

**Deterministic logic:**
- Capture timestamp is **immutable** once written (never editable; only
  superseded by a new entry referencing the prior).
- Outcome close-out tags: thesis correct / wrong / partially correct /
  untested.

**Judgmental input:**
- Variant perception (what does the advisor see that the market does not).
- Catalyst (what triggers the thesis to play out).
- Time horizon.
- Exit condition (what would prove the thesis wrong).

**Why this matters:** The single largest gap in current advisor
documentation is *the absence of a pre-trade thesis*. When a trade goes
against the client, regulators will look for what the advisor believed
**at the time**. If the only record is a post-trade note, the burden of
proof shifts. Module 4 forces the pre-trade record.

**The exit condition is the most important field.** It is the difference
between "advice" and "speculation" under Adviser Act doctrine. An advisor
who cannot articulate what would prove their recommendation wrong is not
giving advice; they are gambling on the client's behalf.

---

## Module 5 — Solicited / Unsolicited Audit Trail

| Attribute | Value |
|---|---|
| **Terminal surface** | `section-audit-trail` |
| **Input contract** | IPS Record (referenced by ID) |
| **Output contract** | `recommendation-event/v1` |
| **Persistence** | Append-only; immutable timestamps |
| **Regulated** | No (but central to FINRA 2111 / 3110 / 4511 record) |
| **Rules touched** | FINRA 2111 (suitability); FINRA 3110 (supervision); FINRA 4511 (recordkeeping); Reg BI Care (alternatives considered). |

**Deterministic logic:**
- Append-only — entries never edited or deleted, only superseded.
- Required fields: origin (solicited / unsolicited), security, action,
  IPS-record-id reference, alternatives considered, rationale, timestamp.
- The system rejects entries with origin missing.

**Why solicited/unsolicited matters:** This single tag drives the
supervisory regime (an unsolicited order has dramatically different
supervisory obligations than a solicited one). Inconsistent or post-hoc
tagging is a recurring FINRA exam finding.

**Append-only design:** The advisor cannot retroactively change "solicited"
to "unsolicited" after a position goes against the client. The original
entry stays; a new entry referencing the prior may be added with the
correction *and the reason for correction*.

---

## Module 6 — Reg BI Note Generator  [REGULATED]

| Attribute | Value |
|---|---|
| **Terminal surface** | `section-reg-bi-note` |
| **Input contract** | IPS Record, Trade Thesis, Recommendation Event |
| **Output contract** | `reg-bi-note/v1` |
| **Persistence** | Client-side; exported to firm system for principal review |
| **Regulated** | **Yes — regulatory work product. CCO sign-off required.** |
| **Rules touched** | Reg BI Disclosure, Care, Conflict. Adviser Act fiduciary. CFP Standards A.1, A.8, A.10. |

**Deterministic logic:**
- Template version pinned (`reg-bi-note/v1`).
- All required fields enforced (cannot generate with missing fields).
- Status field defaults to `draft-pending-compliance-review` and remains
  that way until the principal review flag is set (firm process).
- Client reference uses ID or initials, never PHI/full name in the note
  body, unless the firm's template variant requires it.

**Required fields (enforced):**
- Recommendation (action + security).
- Client investment profile (referenced to IPS record by ID).
- Care basis — why this is in the client's best interest.
- Reasonably available alternatives considered.
- Cost consideration (fees, expense ratio, commission).
- Conflict of interest — must be affirmatively stated (cannot be blank;
  "none identified" is an explicit option but the field cannot be empty).
- Disclosure provided (Form CRS, fee schedule, prospectus, as applicable).
- Attestation by advisor.
- Date.

**The constraint that matters:** The note **cannot be generated** until
the prerequisite records (IPS, thesis if applicable, event) exist. The
advisor cannot "make a note and back-fit a trade." The order of operations
is enforced by the data contracts.

**Sign-off:** See `templates/reg-bi-note-v1.md`. CCO signs the template
itself; once signed, the version is locked per `12-version-lock.md`.

---

## Module 7 — Note Completeness Auditor  [REGULATED]

| Attribute | Value |
|---|---|
| **Terminal surface** | `section-compliance` |
| **Input contract** | A finished trade note |
| **Output contract** | `note-audit/v1` (with `blocking: false`) |
| **Persistence** | Audit result client-side; no override log retained |
| **Regulated** | **Yes — affirmative, non-blocking check.** |
| **Rules touched** | FINRA 3110 (supervision — informs, never substitutes). Reg BI elements list. |

**Deterministic logic:**
- Heuristic text scan for 8 elements (per `reg-bi-checklist/v1`):
  recommendation, profile, care-basis, alternatives, costs, conflicts,
  disclosure, date.
- Each element is **present** or **flagged**.
- The output is informational. `blocking: false` is hard-coded into the
  output contract.

**Design principles (non-negotiable):**
1. **Affirmative.** The auditor never silently passes a note. It always
   names the elements found and the elements flagged.
2. **Non-blocking.** The advisor can always proceed with the note. The
   auditor never prevents filing.
3. **No override log.** If the advisor proceeds despite a flag, no
   "override" record is created. The reason: an override log creates a
   chilling effect on advisor judgment and creates a discoverable record
   of the advisor "disagreeing with the system" that has no actual
   regulatory significance. Principal review under FINRA 3110 is the
   substantive check; the auditor is a preflight aid.
4. **Heuristic, not authoritative.** A flag means "we did not detect the
   cue phrase"; it does not mean the note is wrong. Advisor judgment
   governs.

**Why these principles matter:** A blocking auditor would substitute
software judgment for advisor judgment, which neither the rules nor good
supervisory practice contemplate. A logging auditor would create a
discovery target. The current design informs the advisor and the
principal without doing either.

**Checklist version:** `reg-bi-checklist/v1`. CCO signs the checklist
element list and cue phrases. Locked per `12-version-lock.md`.

---

## Module 8 — Equity Tearsheet Generator

| Attribute | Value |
|---|---|
| **Terminal surface** | `section-research` |
| **Input contract** | Market data, fundamentals, analyst consensus |
| **Output contract** | `equity-tearsheet/v1` |
| **Persistence** | Client-side; exportable as PDF/HTML |
| **Regulated** | No (research summary, not a recommendation; uses standard industry disclosure language) |
| **Rules touched** | FINRA 2210 (communications with the public) if distributed; otherwise internal-use. |

**Deterministic logic:**
- Price, 52-week range, 1-year return, multiples, fundamentals from data
  inputs.
- Implied upside calculated from mean price target.
- Risk-flag display (customer concentration, leverage, regulatory
  overhang, etc.) from input flags.

**Disclosure stack:** Standard industry-style language. **No firm name,
no advisor name, no recommendation in the tearsheet itself.** A tearsheet
becomes a recommendation only when an advisor attaches it to a Reg BI
note via Module 6.

**Why the firm-name omission matters:** If the firm distributes a
tearsheet to retail customers under its own letterhead, FINRA 2210 review
applies. By keeping the firm and advisor names off the tearsheet, the
default state is "internal research note," and the firm makes an explicit
decision to elevate it to a customer-facing communication (with the
attendant 2210 review).

---

## Module 9 — Concentration & Cross-Holdings X-Ray

| Attribute | Value |
|---|---|
| **Terminal surface** | `section-concentration` |
| **Input contract** | Holdings Snapshot, fund look-through data |
| **Output contract** | `concentration-xray/v1` |
| **Persistence** | Client-side |
| **Regulated** | No (operational; output informs regulated work) |
| **Rules touched** | Reg BI Care (risks of recommendation); Adviser Act duty of care; FINRA 2111 customer-specific suitability. |

**Deterministic logic:**
- Look-through analysis: distributes fund values to underlying constituents
  using signed weights.
- Signed weights preserved (negative for inverse exposure; weights > 1 for
  leveraged) so that net and gross exposure are both computable.
- Per-name aggregation across household.
- Threshold flag at single-name net exposure > 10% (configurable).
- Identification of offsetting positions (high gross, low net) that still
  carry cost / tracking risk.

**Why this matters:** A client with three "diversified" funds may have
17% effective exposure to one mega-cap technology name. Reg BI Care
requires the advisor understand this; without a look-through tool, most
advisors cannot. Module 9 surfaces it deterministically.

---

## Module 10 — Workstation

| Attribute | Value |
|---|---|
| **Terminal surface** | The workstation itself |
| **Input contract** | None (composes other modules) |
| **Output contract** | None (it is the integration shell) |
| **Persistence** | None (each module persists its own) |
| **Regulated** | No |
| **Rules touched** | Operational. |

The workstation is the integration surface. It does not duplicate module
logic. Each module is loaded in its own frame and exchanges data only
through the published contracts.

---

## Cross-cutting properties

These properties are true across all modules and are part of what a CCO is
approving:

- **No hidden scoring.** No combined risk score, no proprietary fit
  metric, no AI-derived suitability number.
- **Method assumptions disclosed.** Where math is used (Module 3), the
  assumption is shown next to the result.
- **Versioned contracts.** Every output JSON includes a contract version
  (`/v1`). Templates are locked at sign-off.
- **Append-only where it matters.** Trade thesis timestamps, audit-trail
  entries, recommendation events: immutable. Corrections are superseding
  entries, not edits.
- **Client-side persistence.** No client PII flows to a third-party server
  through Arctic Edge itself. Firm integration (market data, custodian
  feeds, recordkeeping export) is the firm's existing infrastructure
  under its existing Reg S-P program.
- **Affirmative checks, never silent blocks.** Module 7 is the only audit
  module, and it is explicit and non-blocking.
- **No override logs.** The system does not create discoverable records
  of advisor disagreement with software heuristics.
