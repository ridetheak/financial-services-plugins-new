# Implementation Playbook

**Audience:** CEO, COO, CCO, Head of IT.
**Purpose:** Day-by-day plan from initial review to firm-wide rollout.

This playbook assumes a mid-sized RIA or broker-dealer (10–200 advisors).
Larger firms scale the timeline; smaller firms compress it.

---

## Phase A — Review and Sign-Off (Days 0–30)

### Week 1 — Read and route
- CEO/President reads `00-executive-summary.md` and `07-implementation-playbook.md`.
- CCO and General Counsel receive the full package via the `INDEX.html` portal.
- IT receives `13-data-handling.md` for security review.

### Week 2 — Compliance deep read
- CCO reads:
  - `01-regulatory-framework.md`
  - `02-module-compliance-matrix.md`
  - `03-reg-bi-deep-dive.md`
  - `04-cfp-standards-mapping.md` (if applicable)
  - `06-supervision.md`
- CCO compiles questions; if not answered by `15-faq.md`, escalates.

### Week 3 — Template tailoring
- CCO and General Counsel (or outside counsel) tailor:
  - `templates/reg-bi-note-v1.md` — firm-specific disclosure stack,
    conflict inventory, product mix, share-class structure.
  - `templates/reg-bi-checklist-v1.md` — firm-specific cue phrases that
    match the tailored note template.
- IT confirms `13-data-handling.md` posture is consistent with firm's
  existing Reg S-P / NY DFS Part 500 program.

### Week 4 — Sign-off
- CCO executes `11-sign-off-template.md`.
- Templates are version-locked per `12-version-lock.md`.
- A copy of the executed sign-off is filed in the firm's compliance
  records.

**Exit criteria for Phase A:**
- Executed sign-off on file.
- Two regulated templates tailored and locked.
- IT integration plan agreed.
- Pilot advisor team identified.

---

## Phase B — Pilot (Days 30–120)

Detailed plan in `08-pilot-rollout.md`. Summary:

- **3–5 advisors**, ideally including a mix of seniority and book mix.
- **Real client work** (the pilot is not a sandbox; the artifacts produced
  are real Reg BI records, filed in the firm's records system).
- **Weekly check-ins** between pilot advisors, supervising principals,
  and the CCO.
- **Module 7 calibration** — if the firm's note style consistently
  triggers false-positive flags on a specific element, the cue phrase
  list for that element may need supplementation (a checklist revision,
  re-signed by CCO under the version-lock policy).

**Pilot success criteria:**
- Zero blocked workflows (Module 7 is non-blocking by design; this is
  verifying advisors do not perceive it as blocking).
- Principal review time per note decreases or stays flat.
- Module 7 flag-resolution rate at principal review > 95% (i.e.,
  principals are not finding gaps the auditor missed at substantive rates).
- Pilot advisors complete the satisfaction survey
  (`09-training-curriculum.md` template).
- No exam-eligible deficiencies in pilot records (the firm tests this in
  Day-90 internal audit).

---

## Phase C — Firm-wide adoption (Days 120–240)

### Wave 1 (Days 120–150) — Early adopters
- All advisors who volunteered during pilot.
- Standard training (see `09-training-curriculum.md`).
- Workstation deployed to their machines (or web access enabled).

### Wave 2 (Days 150–210) — Mandated rollout, branch by branch
- One branch per week. Branch manager + supervising principal lead.
- Training is mandatory; CE credit if the firm's CE program offers it.
- Supervisory dashboards configured to consume Arctic Edge artifacts.

### Wave 3 (Days 210–240) — Stragglers and stabilization
- Final advisors brought online.
- Quarterly review of metrics (see below).

---

## Phase D — Steady state (Day 240 onward)

### Ongoing supervisory operations
- Every Reg BI note flows through Module 6 → Module 7 → principal review.
- Every recommendation logs through Module 5.

### Quarterly metrics review
The CCO reviews:
- Volume by module (notes generated, audits run, events logged).
- Auditor flag distribution (which elements flag most often).
- Principal-review return rate (notes returned to advisor).
- Time-to-approval at principal review.
- Exception report: any module usage anomalies (e.g., advisor not using
  Module 4 for trades > $X — not a violation, but a coaching opportunity).

### Annual review under 206(4)-7 / 3120
See `10-monitoring-and-testing.md`.

### Template review
Annually (or sooner if regulatory guidance changes), the CCO reviews the
locked templates and re-signs if no changes, or revises and re-signs per
`12-version-lock.md`.

---

## IT integration checklist

For Phase A Week 4 IT integration plan, the checklist:

- [ ] How does Arctic Edge get **holdings data**? (Schwab websocket, custodian
      file, manual entry — Phase 1 default is manual entry; firm-side
      integration is recommended.)
- [ ] How does Arctic Edge get **market data**? (OpenBB MCP, firm-provided
      market data feed, or manual entry.)
- [ ] How are **exported JSON artifacts** ingested into the firm's records
      system? (API push, file drop, manual upload — firm-side process.)
- [ ] What is the **client identity mapping** (`clientRef` → CRM record)?
- [ ] Is the firm **hosting** Arctic Edge or running it from a hosted URL?
      (Phase 1 is single-file HTML; can be hosted internally or on a
      vendor URL.)
- [ ] What **authentication** gates Arctic Edge access? (Firm SSO is
      recommended.)
- [ ] What **backup and disaster recovery** posture covers Arctic Edge?
      (Inherits the firm's existing program.)

---

## Cost framing

Status quo:
- Advisor time on note writing (hours per note × notes per advisor × rate).
- Principal review time.
- Compliance review and remediation on exam findings.
- Cost of exam findings (monetary sanctions, remediation projects,
  reputation).

With Arctic Edge:
- License / deployment cost (firm-specific).
- Advisor time per note typically lower (fields are structured; thesis is
  often already captured for the advisor's own use).
- Principal review time typically lower (structured records are easier to
  review).
- Compliance exam exposure lower (records are pre-organized).

A formal ROI analysis is not part of this package; the firm models it
against its own benchmarks.

---

## Communication plan

The firm should announce the Arctic Edge rollout internally with messaging
that emphasizes:

1. This is a **support tool**, not a constraint on advisor judgment.
2. Module 7 is **non-blocking**. Advisors are never prevented from filing
   a note they believe is complete.
3. Principal review remains the authoritative substantive review.
4. The CCO has signed off; the firm's compliance position is that Arctic
   Edge supports — and does not modify — the firm's existing fiduciary
   duties.
5. Advisor questions go to [training coordinator]; compliance questions go
   to the CCO.

What the announcement should not say:
- It should not claim Arctic Edge "ensures Reg BI compliance" (no tool can;
  the firm's program does).
- It should not claim Arctic Edge "makes notes defensible" (the underlying
  recommendation is what makes a note defensible; Arctic Edge documents
  the recommendation).
- It should not be framed as a response to regulatory criticism of the
  firm (it is not; it is forward-looking).
