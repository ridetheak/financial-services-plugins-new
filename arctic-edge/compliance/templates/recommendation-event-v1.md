# Schema — Recommendation Event (`recommendation-event/v1`)

**Status:** Operational contract; central to FINRA 2111 / 3110 / 4511
record and to Reg BI Care alternatives-considered documentation.

**Producer:** Module 5 (Audit Trail).
**Consumers:** Modules 6, 7; principal review queue.
**Persistence:** Append-only. Immutable once written. Corrections by
supersession.

---

## JSON shape

```json
{
  "contract": "recommendation-event/v1",
  "eventId": "evt-2026-05-28-7821-001",
  "clientRef": "C-7821",
  "advisorId": "ADV-12345",
  "loggedAt": "2026-05-28T10:25:00-08:00",
  "supersedes": null,
  "supersededBy": null,
  "reasonForCorrection": null,

  "ipsRecordId": "ips-2026-01-15-7821",
  "tradeThesisId": "thesis-2026-05-27-7821-MSFT",

  "origin": "solicited",
  "originBasis": "advisor introduced the position",

  "recommendation": {
    "action": "buy",
    "security": "MSFT",
    "quantity": 100,
    "notional": 40000.00,
    "accountId": "acct-7821-IRA-01"
  },

  "alternativesConsidered": [
    { "security": "GOOGL", "rejectedReason": "..." },
    { "security": "XLK", "rejectedReason": "..." }
  ],

  "rationale": "...",

  "executionStatus": "pending | filled | partial | rejected | canceled",
  "filledAt": null,
  "linkedNoteId": "ae-rbn-2026-05-28-001"
}
```

---

## Field notes

| Field | Notes |
|---|---|
| `eventId` | Stable identifier. |
| `loggedAt` | **Immutable** once written. |
| `supersedes` / `supersededBy` | Supports the supersession chain for corrections. |
| `origin` | `solicited` or `unsolicited`. Required. Drives the supervisory regime. |
| `originBasis` | Free text. For unsolicited: "client called and directed purchase." For solicited: "advisor introduced the position." |
| `ipsRecordId` | The active IPS at the event timestamp. The IPS is the customer-specific anchor. |
| `tradeThesisId` | Optional but recommended for solicited recommendations. |
| `alternativesConsidered` | Array. For solicited recommendations, generally non-empty. For unsolicited, may be empty with `originBasis` explaining. |
| `linkedNoteId` | Back-reference to the `reg-bi-note/v1` produced for this event. Populated when the note is generated. |

---

## Append-only semantics

Once written, a `recommendation-event/v1` record:

- Cannot be edited.
- Cannot be deleted.
- Cannot have its `loggedAt` timestamp changed.

Corrections are made by writing a new event that:

- References the prior event in `supersedes`.
- Provides `reasonForCorrection`.
- Carries its own new `loggedAt` timestamp.

The prior event remains in the record. The chain is preserved.

This design is the difference between a regulator-defensible audit
trail and an editable record that can be challenged as
post-hoc-modified.

---

## Origin tagging — why it matters

The single most important field in this record is `origin`.

**Solicited:** The advisor introduced the security or strategy. The
full Reg BI Care Obligation applies, including alternatives considered,
care basis, costs, conflicts.

**Unsolicited:** The client directed the transaction. The Care
Obligation still requires the advisor to ensure the transaction is not
inconsistent with the client's profile, but the alternatives-considered
analysis is different — the alternative is "decline to execute the
client's directed transaction," which is a high bar.

FINRA exams routinely find inconsistent origin tagging. Module 5
enforces the field; the advisor cannot log an event without choosing.
Once chosen, it cannot be changed silently — only superseded with a
recorded reason.

---

## How this interacts with note generation

Module 6 (Reg BI Note Generator) requires:

- A `recommendation-event/v1` to exist.
- The event's `ipsRecordId` to point to an active (non-superseded) IPS.
- For solicited events: the event's `alternativesConsidered` to be
  populated (or the note's `alternatives` field to be populated; the
  note can extend the event's record).
- For unsolicited events: the event's `originBasis` to be populated.

If any are missing, the note generator surfaces them; the advisor
returns to the relevant module to complete the record.
