# Schema — Portfolio Risk (`portfolio-risk/v1`)

**Status:** Operational contract. Output of Module 3 (Portfolio Risk
Analyzer). Not regulatory work product per se; consumed by Module 6
when the Reg BI Care Obligation requires documented risk understanding.

**Producer:** Module 3.
**Consumers:** Module 2 (Quadrant 1 input — suggested rating only),
Module 6 (referenced for "risks" element of Care Obligation).

---

## JSON shape

```json
{
  "contract": "portfolio-risk/v1",
  "analysisId": "risk-2026-05-28-7821",
  "clientRef": "C-7821",
  "advisorId": "ADV-12345",
  "computedAt": "2026-05-28T09:00:00-08:00",
  "ipsRecordId": "ips-2026-01-15-7821",

  "holdingsSnapshotId": "snap-2026-05-28-7821",
  "asOfDate": "2026-05-27",

  "metrics": {
    "expectedReturn":     { "value": 0.082, "unit": "annualized", "method": "position-weighted" },
    "volatility":         { "value": 0.142, "unit": "annualized", "method": "parametric, single-correlation" },
    "beta":               { "value": 0.91,  "vs": "SPX",          "method": "position-weighted" },
    "sharpe":             { "value": 0.36,  "rf": 0.045 },
    "var95_1y":           { "value": -0.151, "method": "parametric, mean excluded, 1-year horizon" },
    "var99_1y":           { "value": -0.243, "method": "parametric, mean excluded, 1-year horizon" },
    "maxDrawdown":        { "value": -0.187, "lookback": "5y", "source": "historical" }
  },

  "methodAssumptions": [
    "Single average pairwise correlation across positions (avg = 0.42).",
    "VaR mean excluded — conservative; produces higher VaR than mean-adjusted variant.",
    "Risk-free rate 4.5% from input field.",
    "1-year horizon for VaR (configurable)."
  ],

  "sectorConcentration": [
    { "sector": "Technology", "weight": 0.31 },
    { "sector": "Financials", "weight": 0.18 }
  ],

  "componentRiskContributions": [
    { "position": "MSFT", "weight": 0.04, "contribution": 0.061 },
    { "position": "VTI",  "weight": 0.28, "contribution": 0.184 }
  ],

  "sameDirectionFlags": [
    { "type": "concentration",    "what": "Technology sector at 31% > 30% IPS soft limit" },
    { "type": "high-weight-beta", "what": "MSFT 4% weight × beta 1.31 = high amplification" }
  ],

  "suggestedQuadrant1Rating": "moderate",
  "advisorConfirmedRating": null,
  "advisorConfirmedAt":     null
}
```

---

## Field notes

| Field | Notes |
|---|---|
| `metrics.*.method` | Each metric carries its method assumption. **No metric is reported without its method.** |
| `methodAssumptions` | Full enumeration of assumptions used. Shown in UI alongside the metrics. |
| `componentRiskContributions` | Sum to 100%. Identifies what positions drive the portfolio's risk. |
| `sameDirectionFlags` | Affirmative flags for sizable positions / sectors that amplify market exposure together. |
| `suggestedQuadrant1Rating` | The module suggests; the advisor confirms or overrides. |
| `advisorConfirmedRating` | Populated when the advisor accepts or overrides the suggestion. |

---

## Why method assumptions are surfaced

Reg BI Care requires the advisor "understand the potential risks." If
the risk numbers depend on hidden method assumptions, the documented
"understanding" is incomplete. Module 3's UI shows the assumption next
to the result; this record carries them in writing.

Specifically:

- **Single average correlation:** A simplifying assumption. A full
  covariance matrix would be more accurate for a heterogeneous
  portfolio. The simplifying assumption is conservative for many
  portfolios but not all; the assumption is disclosed.
- **Mean excluded from VaR:** Conservative — produces a larger VaR
  than mean-adjusted VaR. The advisor sees both the metric and the
  method.

These are not flaws; they are choices. The record documents that the
choice was disclosed.

---

## Advisor confirmation flow

1. Module 3 computes and surfaces a `suggestedQuadrant1Rating`.
2. The advisor reviews the metrics, flags, and assumptions.
3. The advisor confirms the suggested rating OR overrides with a
   different rating and a free-text reason.
4. The confirmed rating becomes the Quadrant 1 input to Module 2
   (Four-Quadrant Risk Framework).

The system never sets Quadrant 1 silently. Module 2's collapse guard
will not accept a Quadrant 1 input that lacks an advisor confirmation.

---

## What this record proves

A versioned, timestamped `portfolio-risk/v1` record proves:

- The advisor reviewed the deterministic risk metrics at a specific
  point in time.
- The method assumptions were disclosed in writing.
- The advisor exercised judgment on the resulting risk rating.
- Reg BI Care Obligation "risks" element was documented (15l-1(a)(2)(ii)(A)).

The principal reviewing a Reg BI note that references this record can
trace from "the recommendation is in the client's best interest given
the risks" back to the actual numbers, methods, and advisor judgment.
