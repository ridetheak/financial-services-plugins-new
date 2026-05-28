# Supervision

**Audience:** Head of Supervision, CCO, Principal Reviewers.
**Purpose:** How Arctic Edge fits the firm's FINRA Rule 3110 supervisory
framework. Specifically: what software does, what the principal does, and
what the boundary is.

---

## Position

**Module 7 is not a substitute for principal review.** It is a preflight
aid. The registered principal under FINRA 3110 remains the substantive
reviewer of every Reg BI note before it enters the client file. Arctic Edge
gives the principal a richer, more consistent record to review and a
preflight flag for apparent gaps; it does not relieve the principal of any
duty.

This document is intentionally short. A long supervisory chapter implies
that software is doing supervisory work it should not be doing.

---

## Roles

| Role | Responsibility |
|---|---|
| **Advisor** | Captures IPS, thesis, recommendation event, drafts note via Module 6, addresses Module 7 flags. |
| **Module 7 (auditor)** | Affirmative, non-blocking pre-submission check. Flags apparent gaps for advisor and principal review. |
| **Principal (FINRA 3110)** | Substantive review. Approves or rejects the note for filing. |
| **CCO** | Annual program review under Adviser Act Rule 206(4)-7. |

---

## Workflow

```
                 ┌──────────────────────────┐
  Advisor ─────► │ Capture: IPS / Thesis /  │
                 │ Event (Modules 1, 4, 5)  │
                 └────────────┬─────────────┘
                              │
                              ▼
                 ┌──────────────────────────┐
                 │ Draft note (Module 6)    │
                 └────────────┬─────────────┘
                              │
                              ▼
                 ┌──────────────────────────┐
                 │ Auditor check (Module 7) │  ← flags but does not block
                 └────────────┬─────────────┘
                              │
                              ▼
                 ┌──────────────────────────┐
                 │ Advisor resolves flags   │
                 │ (or proceeds)            │
                 └────────────┬─────────────┘
                              │
                              ▼
                 ┌──────────────────────────┐
                 │ PRINCIPAL REVIEW (3110)  │  ← substantive review
                 └────────────┬─────────────┘
                              │
                  ┌───────────┴───────────┐
                  ▼                       ▼
            ┌──────────┐            ┌──────────┐
            │ Approve  │            │ Return   │
            │ → file   │            │ to adv.  │
            └──────────┘            └──────────┘
```

---

## What the principal sees that they did not see before

Before Arctic Edge, a principal reviewing a Reg BI note typically saw:

- The note (free-form text).
- The trade ticket.
- The CRM client profile (perhaps).

After Arctic Edge, the principal sees:

- The note, structured to the template.
- The `note-audit/v1` result (which elements were flagged at preflight).
- The referenced `ips-record/v1` (the actual investment profile at the time).
- The referenced `recommendation-event/v1` (origin, alternatives considered,
  rationale).
- The `trade-thesis/v1` if applicable (pre-trade variant perception and
  exit condition).
- The `portfolio-risk/v1` and `concentration-xray/v1` if applicable
  (deterministic risk and concentration context).

The principal's review is faster and better-informed. The review is still
the principal's; the artifacts are inputs.

---

## What the principal does about Module 7 flags

A Module 7 flag is information, not a directive. The principal applies
judgment:

| Flag | Possible interpretations |
|---|---|
| `alternatives` not detected | (a) Note has alternatives but no cue phrase. (b) Note has no alternatives but should have. (c) Unsolicited transaction; alternatives not applicable. |
| `costs` not detected | (a) Note discusses costs but cues missed. (b) Costs missing from note. (c) No-fee position (rare but possible). |
| `conflicts` not detected | (a) "None identified" wording used but cues missed. (b) Conflict statement missing. |
| `disclosure` not detected | (a) Reference to delivered disclosures not in cue list. (b) Disclosure missing. |
| `date` not detected | Note is undated. |

The principal reads the note, applies judgment, approves or returns. The
flag is a "double-check this" hint; the principal's review is what
satisfies FINRA 3110.

---

## Sampling and risk-based supervision

Many firms use risk-based supervisory sampling rather than 100% review.
The Arctic Edge structure supports either:

- **100% review.** Every note enters the principal queue. The `note-audit/v1`
  result is shown alongside.
- **Risk-based sampling.** The firm's sampling criteria can incorporate
  Arctic Edge data — e.g., notes with two or more Module 7 flags go to
  100% review; clean notes sample at the firm's standard rate.

Arctic Edge does not prescribe the sampling regime. The firm's WSPs do.

---

## What does not change

- The firm's WSPs.
- The principal's duty and authority.
- The firm's escalation procedures.
- The firm's branch-office supervision program.
- The firm's annual compliance meeting and training program.

Arctic Edge plugs into the supervisory infrastructure the firm already runs.
