# Schema — IPS Record (`ips-record/v1`)

**Status:** Operational contract. Not regulated work product per se;
referenced by regulated work product (Modules 6, 7) and central to the
firm's Care-Obligation and customer-specific suitability record.

**Producer:** Module 1 (IPS Module).
**Consumers:** Modules 2, 3, 5, 6, 7, 9.

---

## JSON shape

```json
{
  "contract": "ips-record/v1",
  "ipsRecordId": "ips-2026-01-15-7821",
  "clientRef": "C-7821",
  "advisorId": "ADV-12345",
  "createdAt": "2026-01-15T14:00:00-08:00",
  "effectiveFrom": "2026-01-15",
  "effectiveUntil": null,
  "supersedes": null,
  "reasonForChange": null,

  "client": {
    "type": "individual | joint | trust | entity",
    "ageOrEstablished": 58,
    "taxStatus": "..."
  },

  "objectives": {
    "primary": "long-term growth with moderate risk",
    "secondary": "...",
    "withdrawalNeeds": {
      "regularDistribution": null,
      "lumpSum": null
    }
  },

  "timeHorizon": {
    "primary": "9 years to retirement target",
    "yearsToPrimary": 9
  },

  "riskTolerance": "moderate",
  "riskCapacity": "moderate",

  "liquidity": {
    "minimumLiquidReserve": 50000,
    "ineligibleForIlliquid": false
  },

  "assetClassTargets": [
    { "class": "US Equity", "target": 50, "min": 40, "max": 60 },
    { "class": "International Equity", "target": 10, "min": 5, "max": 15 },
    { "class": "Fixed Income", "target": 35, "min": 30, "max": 45 },
    { "class": "Cash & Equivalents", "target": 5, "min": 0, "max": 15 }
  ],

  "constraints": {
    "maxSingleNameNet": 5,
    "maxSingleNameGross": 8,
    "maxSectorConcentration": 30,
    "prohibitedHoldings": ["tobacco-direct", "..."],
    "esgScreens": null
  },

  "rebalancing": {
    "method": "calendar | threshold | both",
    "calendarCadence": "quarterly",
    "thresholdBand": 5
  }
}
```

---

## Field notes

| Field | Notes |
|---|---|
| `ipsRecordId` | Stable identifier. Referenced by recommendation events and notes. |
| `clientRef` | ID or initials, not full name. Maps to firm CRM. |
| `effectiveFrom` / `effectiveUntil` | A non-superseded record has `effectiveUntil: null`. When superseded, `effectiveUntil` set to the new record's `effectiveFrom`. |
| `supersedes` | If this record supersedes a prior IPS, the prior `ipsRecordId`. |
| `reasonForChange` | Free text. Why the IPS changed. |
| `assetClassTargets` | Validated by Module 1: sum of targets = 100%; for each class, min ≤ target ≤ max. |
| `constraints.maxSingleNameNet` | Used by Module 9 (Concentration X-Ray) to flag look-through breaches. |

---

## Validation (Module 1)

The IPS Module rejects a record that fails:

- Sum of asset-class targets ≠ 100%.
- Any class with min > target or target > max.
- Missing required field: `objectives.primary`, `timeHorizon.primary`,
  `riskTolerance`, `riskCapacity`.
- `effectiveFrom` in the future (configurable).

---

## Supersession

When a client's circumstances change (retirement, inheritance, divorce,
revised goals), the advisor creates a new IPS record:

1. New record carries a new `ipsRecordId` and a new `effectiveFrom`.
2. New record's `supersedes` field references the prior `ipsRecordId`.
3. The prior record is updated to set `effectiveUntil` = new record's
   `effectiveFrom`.
4. Both records remain in the firm's records system.

A `recommendation-event/v1` references the IPS by ID that was active at
the event timestamp — not the latest IPS. This is what lets a regulator
trace what the client's profile was at the moment of recommendation.

---

## What this record proves

A versioned, timestamped IPS record proves:

- The client's investment profile (Reg BI Care 15l-1(a)(2)(ii)(B)).
- The basis against which recommendations are measured.
- The firm's customer-specific suitability analysis (FINRA 2111).
- The advisory relationship's documented scope (Adviser Act).
- The CFP professional's documented analysis (CFP A.10, C.1, C.2).

A recommendation made when no IPS exists, or when the active IPS is
materially out of date, is a Reg BI Care gap — and Arctic Edge's
workflow surfaces this (Module 5 will not let a recommendation event be
logged without a `ipsRecordId` reference).
