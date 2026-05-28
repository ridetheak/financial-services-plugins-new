# Reg BI Deep Dive — Modules 6 and 7

**Audience:** CCO, General Counsel, Principal Reviewers.
**Purpose:** Justify, in detail, the design of the two regulated modules.

---

## What the SEC actually requires

The SEC's adopting release for Reg BI (Release No. 34-86031, June 5, 2019)
and the staff guidance that followed make several points that bear directly
on the Arctic Edge design:

1. **There is no required form for the recommendation record.** The SEC
   declined to prescribe a specific format. Firms must "establish, maintain,
   and enforce written policies and procedures reasonably designed to
   achieve compliance" (15l-1(a)(2)(iv)).

2. **The basis for the recommendation must be documented contemporaneously
   or as part of the firm's recordkeeping system.** The 2020 Risk Alert from
   the SEC's Division of Examinations specifically called out post-hoc or
   templated rationales as a deficiency.

3. **"Reasonably available alternatives" is a *new* obligation under Reg
   BI**, not previously part of FINRA 2111 suitability. The 2022 SEC Staff
   Bulletin on Reg BI emphasizes this point.

4. **Conflicts of interest must be both identified and disclosed (or
   eliminated/mitigated where they create incentives to put the firm's
   interest ahead of the client's).** Silence about conflicts is not
   disclosure.

5. **Costs are a required consideration**, not just a disclosure. The Care
   Obligation specifically references costs as a factor in best interest.

---

## How Module 6 (Reg BI Note Generator) implements each obligation

### Disclosure Obligation

| Reg BI Element | Module 6 Field | Enforcement |
|---|---|---|
| Material facts about scope of relationship | (Tailored to firm; default: cross-references Form CRS and existing engagement letter) | Field required, default text editable by advisor, locked template |
| Material facts about conflicts | `conflicts` field | Field cannot be empty; "none identified" is explicit |
| Form CRS delivery | Disclosure cue phrase | Auditor (Module 7) flags absence |

### Care Obligation

| Reg BI Element | Module 6 Field | Enforcement |
|---|---|---|
| Risks | `care-basis` (must address risk fit) | Field required |
| Rewards | `care-basis` | Field required |
| Costs | `costs` field | Field required; specific cost type identified (commission / fee / expense ratio) |
| Customer profile fit | Referenced to `ips-record/v1` by ID | IPS record must exist before note can be generated |
| Reasonable basis (could be suitable for some) | Implied by recommendation context | Captured via Module 4 Trade Thesis (recommended) |
| Customer-specific best interest | `care-basis` field | Field required |
| Series-of-transactions concern | Pattern surfaced via Module 5 (Audit Trail) | Available to principal review |

### Conflict Obligation

| Reg BI Element | Module 6 Field | Enforcement |
|---|---|---|
| Identify conflicts | `conflicts` field | Required; affirmative |
| Disclose conflicts | Disclosure stack in template | Locked template |
| Mitigate where applicable | Firm-side process — outside scope of Module 6 | Sign-off attests firm has process |

### Reasonably available alternatives

This is the obligation that most current tools handle poorly.

- Module 6 requires an `alternatives` field.
- Module 5 (Audit Trail) records the alternatives considered at the moment
  of recommendation.
- The two records cross-reference by ID.
- "None considered because the security was specifically requested by the
  client" is a valid response — but in that case, the Audit Trail event
  origin is `unsolicited`, which is what drives the supervisory regime.

The alternatives field is what defends the recommendation in an exam. It is
not enough to say "this was the best fund." The record must show "I
compared this to X and Y on cost, performance, fit, and selected this one
because Z."

---

## How Module 7 (Auditor) implements the supervisory aid

### What it is

A heuristic text scan of a finished trade note against the
`reg-bi-checklist/v1` element list. It produces a structured result
identifying which elements were detected and which were flagged.

### What it is *not*

- It is **not** a substitute for FINRA 3110 principal review.
- It is **not** a software adjudication of whether the note is adequate.
- It is **not** a blocker.
- It is **not** a logger of advisor overrides.

### Why "affirmative and non-blocking"

A blocking design would create three problems:

1. **Substitution problem.** A blocker substitutes software judgment for
   principal judgment. FINRA 3110 places responsibility on a registered
   principal, not on software.

2. **Brittleness problem.** Heuristic text scanning is good but not
   perfect. A blocker that misses cues would create false friction; a
   blocker that requires specific phrasing would degrade note quality.

3. **Discoverability problem.** A blocker that logs overrides creates a
   discoverable record of advisor "disagreement with the system." That
   record is operationally useless (the principal is the actual reviewer)
   and litigation-hazardous (the record may be cited as evidence that the
   advisor knew the note had gaps).

The affirmative, non-blocking design solves all three:

- The principal does the real review (FINRA 3110).
- The advisor sees flags and decides what to do; the principal sees the
  flagged elements and applies judgment.
- Nothing is logged that suggests adversarial dynamics between the advisor
  and the system.

### What gets reviewed

The CCO signs `templates/reg-bi-checklist-v1.md`. That document defines:

- The 8 element IDs.
- The plain-language name of each element.
- The cue phrases the heuristic looks for.
- The "what counts as detected" logic.
- Special-case logic (e.g., date is detected by regex, not by cue phrase).

Once signed, the checklist is version-locked. Changes go through the
process in `12-version-lock.md`.

---

## How this beats the status quo

### Status quo: "Make this trade defensible"

An advisor places a trade. After the trade, the advisor opens a
general-purpose AI chatbot and asks "write a trade note for this client
position in [security]." The chatbot produces fluent prose that sounds
defensible. The note goes into the file.

**What's wrong:**

- The "alternatives considered" section is fictional — the chatbot has no
  record of what the advisor actually considered.
- The "best interest" rationale is a story constructed after the fact.
- The IPS reference (if any) is paraphrased, not cited to a versioned
  record.
- The conflict disclosure is generic, not specific to the advisor's
  compensation on this product.
- There is no audit trail of the recommendation event.

If FINRA or the SEC asks, on exam, *what did you consider at the time of
the recommendation*, the only record is the note — which was written
after. The advisor's defense is testimonial, not documentary.

### Arctic Edge: workflow constraint

The same advisor:

1. Opens the IPS Record for the client (Module 1, already on file).
2. (Optional but recommended) Logs a Trade Thesis in Module 4 *before*
   placing the trade — variant perception, catalyst, exit condition.
3. Places the trade.
4. Logs the recommendation event in Module 5 — origin
   (solicited/unsolicited), security, action, alternatives considered,
   rationale. Append-only, timestamped.
5. Generates a Reg BI note in Module 6 — fields populated from IPS,
   thesis, event; advisor adds care basis, costs, conflicts, disclosure
   confirmation.
6. Runs the note through Module 7. Flags resolved or proceed.
7. Note enters firm's principal-review queue (FINRA 3110).

If FINRA or the SEC asks *what did you consider*, the record is:

- Pre-trade IPS (versioned, timestamped).
- Pre-trade or contemporaneous thesis (versioned, timestamped, immutable).
- Contemporaneous recommendation event (append-only, timestamped).
- Post-trade note that cites all three by reference.
- Auditor pass with the checklist version recorded.

The advisor's defense is documentary, not testimonial. The trade may
still go wrong; that is market risk. But the *recommendation process* is
visible end-to-end.

---

## What the firm is taking on

When the CCO signs off, the firm is committing to:

1. **Tailored templates.** The two regulated templates
   (`reg-bi-note/v1`, `reg-bi-checklist/v1`) are tailored to the firm's
   product mix, share-class structure, conflict inventory, and
   disclosure stack before sign-off.

2. **Principal review under FINRA 3110.** Module 7 informs the
   principal; it does not substitute. The firm continues to operate its
   3110 program.

3. **Recordkeeping integration.** Arctic Edge outputs are exportable
   JSON. The firm ingests them into its 17a-4 / 4511 records system.
   Arctic Edge does not itself satisfy the firm's recordkeeping rule.

4. **Annual testing under 206(4)-7.** The firm's annual compliance
   program review covers Arctic Edge usage. See
   `10-monitoring-and-testing.md`.

5. **Version lock.** Once signed, templates are locked. Edits require
   re-sign-off. See `12-version-lock.md`.

---

## Anticipated CCO questions

**Q: Can I be confident the heuristic auditor catches all the gaps?**
A: No, and that's by design. The auditor is preflight; the principal is
the actual reviewer. If the heuristic misses a gap that the principal
catches, the principal catches it — that is the supervisory model
working as intended. If the heuristic flags a non-gap, the advisor reads
the flag and proceeds — no harm done.

**Q: What if an advisor uses the note generator but then edits the note
to weaken it?**
A: The note generator output is the artifact filed in the
firm-side recordkeeping system. If the advisor exports, edits, and
re-imports, the firm's recordkeeping system will show two versions; the
firm's supervisory process is responsible for catching this. Arctic
Edge produces the original; the firm controls the chain of custody after
export.

**Q: How does this hold up if the SEC publishes new Reg BI guidance?**
A: The template is version-locked but not immutable. New guidance
triggers a template review under `12-version-lock.md`. The CCO
re-signs; the new version supersedes; old notes carry the version tag
of the template under which they were written.

**Q: Does Arctic Edge create new compliance risk?**
A: It creates a clear, auditable record. The risk shifts from
"undocumented post-hoc rationale" (regulator-flagged) to "documented
contemporaneous process." If the underlying recommendation was bad,
Arctic Edge will not hide it — and that is the correct outcome.

**Q: What about the firm's existing CRM-integrated note system?**
A: Most CRM note systems are free-form text. They satisfy the
recordkeeping rule (something is recorded) but they do not satisfy the
substance of the Care Obligation (the elements may or may not be
present). Arctic Edge complements the CRM — the structured note can be
attached to or imported into the CRM record.
