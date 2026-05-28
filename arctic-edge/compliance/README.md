# Arctic Edge — Compliance Package

This package is the dossier a Chief Compliance Officer (CCO) needs to review,
approve, and operationalize Arctic Edge inside a broker-dealer or RIA. It
exists because Modules 6 (Reg BI Note Generator) and 7 (Note Completeness
Auditor) generate or audit regulatory work product, and because the rest of
the workstation produces records that are subject to SEC books-and-records
rules.

**The position taken throughout this package:** Arctic Edge is not a tool that
"makes a trade defensible." It is a tool that *constrains the advisor to
document the elements of a recommendation that the rules already require*.
The order of operations matters — the note follows the recommendation, but the
elements of the recommendation must already exist before the note can be
written. Arctic Edge enforces that order.

## Who reads what

| Audience | Read first | Then |
|---|---|---|
| **Chief Executive Officer** | `00-executive-summary.md` | `07-implementation-playbook.md` |
| **Chief Compliance Officer** | `01-regulatory-framework.md`, `02-module-compliance-matrix.md` | `03-reg-bi-deep-dive.md`, `11-sign-off-template.md` |
| **General Counsel** | `01-regulatory-framework.md` | `03-reg-bi-deep-dive.md`, `13-data-handling.md` |
| **Head of Supervision** | `06-supervision.md` | `10-monitoring-and-testing.md` |
| **Head of IT / CISO** | `13-data-handling.md` | `07-implementation-playbook.md` |
| **Advisor / Supervisor** | `09-training-curriculum.md` | `templates/reg-bi-note-v1.md` |
| **Regulator (exam)** | `01-regulatory-framework.md`, `02-module-compliance-matrix.md`, `11-sign-off-template.md` (executed) | — |

## Contents

### Strategic
- `00-executive-summary.md` — One-page case for the CEO/CCO.
- `01-regulatory-framework.md` — Direct citations: Reg BI, CFP Standards, Adviser Act §206, FINRA 2111/2210/3110/4511, SEC 17a-3/17a-4, NY DFS Part 500.
- `02-module-compliance-matrix.md` — Module ↔ rule mapping for every Phase 1 module.

### Regulated work product (Modules 6 & 7)
- `03-reg-bi-deep-dive.md` — How Modules 6 & 7 implement Reg BI's four obligations.
- `04-cfp-standards-mapping.md` — CFP Board Code of Ethics & Standards of Conduct mapping.

### Books, records, supervision
- `05-recordkeeping.md` — SEC 17a-3/17a-4 and FINRA 4511 fit; what gets retained, in what form, for how long.
- `06-supervision.md` — FINRA 3110 supervisory framework: who reviews what, when.

### Rollout
- `07-implementation-playbook.md` — From day 0 to firm-wide adoption.
- `08-pilot-rollout.md` — 90-day pilot plan with success criteria.
- `09-training-curriculum.md` — Advisor and supervisor training.

### Ongoing
- `10-monitoring-and-testing.md` — Annual compliance testing program (Rule 206(4)-7).
- `11-sign-off-template.md` — The CCO sign-off form (this is what gets signed).
- `12-version-lock.md` — Template versioning policy.

### Operational
- `13-data-handling.md` — PII, data residency, GLBA Safeguards Rule, NY DFS Part 500.
- `14-incident-response.md` — If a template is found defective.
- `15-faq.md` — Anticipated CCO and exam questions, with answers.

### Templates (the artifacts being signed off on)
- `templates/reg-bi-note-v1.md` — Trade note template (regulated).
- `templates/reg-bi-checklist-v1.md` — Completeness checklist (regulated).
- `templates/ips-record-v1.md` — IPS data contract schema.
- `templates/recommendation-event-v1.md` — Audit trail event schema.
- `templates/portfolio-risk-v1.md` — Risk analyzer output schema.
- `templates/note-audit-v1.md` — Auditor output schema.

### Portal
- `INDEX.html` — Visual compliance portal that ties this together.

## What a CCO is actually signing off on

When the CCO executes `11-sign-off-template.md`, they are approving:

1. The `reg-bi-note/v1` template (`templates/reg-bi-note-v1.md`).
2. The `reg-bi-checklist/v1` element list and cue phrases (`templates/reg-bi-checklist-v1.md`).
3. The position that Module 7 is affirmative and non-blocking by design and keeps no override logs.
4. The data-handling posture in `13-data-handling.md`.
5. The supervisory model in `06-supervision.md`.
6. The version-lock policy in `12-version-lock.md`.

Anything outside that scope is not signed off and should not be presented to a regulator as approved.

## What this package deliberately does NOT do

- It does **not** claim Arctic Edge replaces the advisor's judgment.
- It does **not** claim the Module 7 auditor is a substitute for principal review under FINRA 3110.
- It does **not** claim that following Arctic Edge guarantees a defensible record. The advisor's recommendation must already be in the client's best interest *before* the note documents it.
- It does **not** retain or transmit client PII to any third party. All client-side persistence is local; firm-side integration is the firm's responsibility under their existing GLBA Safeguards program.

## Status

This package is a build artifact. The templates referenced are functional
drafts. Before any use on real client files, a qualified compliance
professional at the implementing firm must:

1. Read `01-regulatory-framework.md` and `02-module-compliance-matrix.md` to
   confirm the rule mapping is consistent with the firm's interpretation.
2. Review and edit `templates/reg-bi-note-v1.md` and
   `templates/reg-bi-checklist-v1.md` to fit the firm's product mix, share
   classes, conflict inventory, and disclosure stack.
3. Execute `11-sign-off-template.md`.
4. Lock the executed template versions per `12-version-lock.md`.

Only then is Arctic Edge production-eligible at that firm.
