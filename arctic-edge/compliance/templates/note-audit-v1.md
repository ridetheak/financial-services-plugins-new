# Schema — Note Audit (`note-audit/v1`)

**Status:** Output of Module 7 (Note Completeness Auditor). Operational
record of the affirmative, non-blocking pre-submission check.

**Producer:** Module 7.
**Consumer:** Principal review queue; firm compliance testing.

---

## JSON shape

```json
{
  "contract": "note-audit/v1",
  "auditId": "audit-2026-05-28-7821-001",
  "checklistVersion": "reg-bi-checklist/v1",
  "auditedAt": "2026-05-28T10:32:00-08:00",
  "noteId": "ae-rbn-2026-05-28-001",
  "advisorId": "ADV-12345",

  "blocking": false,

  "elements": [
    { "id": "recommendation", "name": "Recommendation stated",        "present": true },
    { "id": "profile",        "name": "Client investment profile",    "present": true },
    { "id": "care-basis",     "name": "Care Obligation — basis ...",  "present": true },
    { "id": "alternatives",   "name": "Reasonably available ...",     "present": false },
    { "id": "costs",          "name": "Cost consideration",           "present": true },
    { "id": "conflicts",      "name": "Conflict of interest",         "present": true },
    { "id": "disclosure",     "name": "Disclosure",                   "present": true },
    { "id": "date",           "name": "Date",                         "present": true }
  ],

  "flaggedCount": 1
}
```

---

## Field notes

| Field | Notes |
|---|---|
| `auditId` | Stable identifier. |
| `checklistVersion` | The version of the checklist used. Anchors the audit to the version-locked element list. |
| `auditedAt` | When the heuristic ran. |
| `noteId` | The note that was audited. |
| `blocking` | **Hardcoded `false`**. The auditor never blocks. |
| `elements` | The full element list from the checklist version. Each element is present or not. |
| `flaggedCount` | Count of elements with `present: false`. |

---

## Hardcoded posture

The output **always** has:

- `blocking: false`.
- The full element list (none omitted).
- No `override` field. No `advisorAcknowledgedFlag` field. No record of
  advisor action on the flags.

These are non-negotiable design positions, documented in
`03-reg-bi-deep-dive.md` and signed by the CCO in
`11-sign-off-template.md` Section 2c.

---

## How this record is used

| Consumer | Use |
|---|---|
| Advisor (immediately after running) | Decide whether to address flags or proceed |
| Principal reviewer | Inform substantive review |
| Compliance testing | Audit the auditor (false-negative rate) |
| Records system | Retained alongside the audited note |
| Regulator (exam) | Evidence that the firm runs an affirmative pre-submission check |

---

## What this record is NOT

- It is not a quality score.
- It is not a "pass" or "fail" judgment.
- It is not a substitute for principal review.
- It is not a record of advisor disagreement with software.
- It is not adjudicative.

It is a structured statement: "of the eight elements the firm's CCO has
identified as Reg BI requirements, the heuristic scan detected N of
them in the audited note." Everything beyond that statement is for the
principal and the firm's compliance program.
