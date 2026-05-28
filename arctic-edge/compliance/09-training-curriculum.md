# Training Curriculum

**Audience:** Training Coordinator, Advisors, Principal Reviewers.
**Purpose:** What advisors and principals need to know to use Arctic Edge
correctly.

---

## Advisor curriculum

### Length
- **Initial training:** 90 minutes (live or recorded).
- **Refresher:** 30 minutes annually.

### Format
- Module-by-module walkthrough with real (anonymized) examples.
- Hands-on workstation time on day of training.
- Q&A with the supervising principal present.

### Learning objectives
By the end of training, an advisor can:

1. Open the workstation, navigate the tabs, and identify each Phase 1
   module.
2. Capture a new IPS Record (Module 1) including objectives, risk
   tolerance, risk capacity, time horizon, asset-class targets and bands,
   prohibited holdings, and rebalancing rules.
3. Log a pre-trade thesis (Module 4) for a recommended trade, articulating
   variant perception, catalyst, time horizon, and exit condition.
4. Log a recommendation event (Module 5) correctly tagging origin
   (solicited or unsolicited), citing alternatives considered, and
   referencing the IPS by ID.
5. Generate a Reg BI note (Module 6) populating every required field.
6. Run the Module 7 completeness check, read the flag result, and either
   resolve the flags or proceed with a documented rationale.
7. Read the Module 3 Portfolio Risk Analyzer output, including method
   assumptions, and confirm or override the suggested Quadrant 1 rating.
8. Run the Module 9 Concentration X-Ray and interpret the look-through
   exposure result.

### Materials
- Workstation training environment with anonymized sample client data.
- Training slide deck (firm-tailored — references the firm's signed
  templates, not the generic templates).
- One-page laminated workflow reminder card.
- Access to `15-faq.md` and this curriculum.

### Assessment
- Hands-on exercise: from a client profile and proposed trade, produce a
  full record set (IPS reference, thesis, event, note, audit). Reviewed
  by the supervising principal.
- Brief written quiz (10 multiple-choice items) on the regulatory
  framework — what each module supports, what Module 7 does and does
  not do, where the principal's role begins.

---

## Principal reviewer curriculum

### Length
- **Initial training:** 60 minutes.
- **Refresher:** 30 minutes annually.

### Learning objectives
By the end of training, a principal can:

1. Open a submitted note in their review queue and identify all linked
   records (IPS, thesis, event, audit).
2. Interpret a `note-audit/v1` result and decide whether the flagged
   elements warrant questioning the advisor or not.
3. Identify common false-positive patterns (e.g., "alternatives" flagged
   because the advisor used "I compared" without the word "alternative").
4. Apply the firm's WSPs to approve, return, or escalate a note.
5. Document their review consistent with the firm's existing supervisory
   record practice.

### Key teaching points

**The auditor is preflight, not adjudication.**
A clean auditor result does not mean the note is adequate. A flagged
auditor result does not mean the note is inadequate. The principal's
judgment is what determines adequacy under FINRA 3110.

**The cross-references are the point.**
The structured back-references (IPS ID, thesis ID, event ID) make the
review faster. Confirm the references are accurate; don't take them on
faith.

**Patterns matter.**
A single flagged auditor result is information. Repeated flags on the
same element from the same advisor is a coaching signal. Surface to the
CCO.

**Returning a note is constructive, not punitive.**
Returning a note for a missing element is the system working. The
principal-advisor dynamic should not become adversarial; reframe returns
as collaboration.

---

## CCO curriculum

The CCO does not need a training course. They need:

- This compliance package, read carefully.
- Time set aside to tailor the regulated templates.
- Sign-off authority on the version manifest.
- Access to the quarterly metrics dashboard.

---

## Sample exercise — Advisor

**Setup:**

> Client: Sarah Reilly, 58, $1.2M IRA, retirement target 67.
>
> IPS objective: long-term growth with moderate risk; 60% equity / 40%
> fixed income target; ±10% bands; no individual stock concentration >5%.
>
> Proposed trade: Solicited recommendation to add $40,000 of MSFT to
> existing 3% MSFT position, funded by trimming an actively-managed
> large-cap equity fund.

**Tasks:**

1. Confirm or update the IPS Record (Module 1).
2. Document the trade thesis (Module 4): why MSFT, why now, what would
   prove this wrong.
3. Log the recommendation event (Module 5): origin = solicited;
   alternatives considered = (e.g., GOOGL, broad tech ETF); rationale.
4. Run Module 9 to verify the post-trade MSFT exposure remains under
   the IPS 5% single-name cap.
5. Generate the Reg BI note (Module 6).
6. Run Module 7 completeness check; address any flags.
7. Submit to principal queue.

**Expected output:** A linked set of 6 artifacts (IPS reference + 5 new
records) that, read together, tell the full story of the recommendation.

---

## Sample exercise — Principal

**Setup:** A submitted note from the Advisor Exercise above.

**Tasks:**

1. Open the note. Identify all linked records.
2. Confirm the IPS reference is the correct version (not superseded).
3. Read the thesis. Does the exit condition actually fall within the
   stated time horizon?
4. Read the event. Does "alternatives considered" name specific
   alternatives, or is it generic?
5. Read the note. Does the conflict statement specifically identify the
   advisor's compensation on the actively-managed fund being trimmed
   (which generated a 12b-1)?
6. Read the audit. What was flagged? Does each flag reflect a real gap?
7. Approve, return, or escalate.
8. Document the review.

---

## Common pitfalls (cover in training)

**Advisor pitfalls:**

- "Solicited" vs. "unsolicited" miscoding. Often "unsolicited" is used
  defensively when in fact the advisor introduced the security. Train on
  the definition.
- Generic "alternatives considered." "Other large-cap names were
  considered" is not specific. Train on naming the alternatives.
- "Conflict: none" without thinking. The advisor's share-class selection,
  the firm's revenue-sharing arrangements, the 12b-1 — these are
  conflicts even if disclosed and accepted. Train on the affirmative
  inventory.
- Date format. ISO 8601 (`2026-05-28`) is preferred for the audit
  heuristic. Other formats are detected but ISO is unambiguous.

**Principal pitfalls:**

- Relying on the auditor pass as substitute review. Read the note.
- Approving without checking the IPS reference is current. A superseded
  IPS in the file but a different IPS at recommendation time is a gap.
- Letting return notes accumulate. Return at the moment of review with
  specific feedback.

---

## Refresher curriculum (annual)

The 30-minute annual refresher covers:

- Any template changes since the last training (re-signed versions).
- Patterns from the past year's auditor flag distribution.
- Patterns from principal returns and exam findings (if any).
- Regulatory developments affecting the templates (SEC guidance, FINRA
  rule changes, state rule changes).
- Refresher on the affirmative non-blocking philosophy of Module 7.
