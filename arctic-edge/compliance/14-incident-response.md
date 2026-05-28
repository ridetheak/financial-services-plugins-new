# Incident Response

**Audience:** CCO, CISO, Head of Compliance Operations.
**Purpose:** What to do if something goes wrong — a template defect, a
records-system integration failure, an exam-eligible finding traced to
Arctic Edge, a security incident.

---

## Position

Arctic Edge is software with a regulated output footprint. Incidents
involving Arctic Edge fit into the firm's existing incident-response
program; this document specifies the Arctic-Edge-specific handling
that supplements the firm's IR plan.

---

## Incident categories

### Category 1 — Template defect

A defect is identified in `reg-bi-note/v1` or `reg-bi-checklist/v1`
that causes the produced records to be substantively incomplete (e.g.,
a required field is missing from the template, a cue phrase consistently
fails to match a substantively complete element).

**Examples:**
- A new SEC staff bulletin clarifies a Care Obligation element not
  reflected in the template.
- An exam finding from a peer firm cites template language Arctic Edge
  uses as inadequate.
- Internal testing identifies a false-negative rate on the checklist
  above the threshold in `10-monitoring-and-testing.md`.

**Response:**
1. CCO assesses scope: how many records in the field were produced under
   the defective version, over what period.
2. CCO determines whether the defect is **material** (records produced
   are substantively non-compliant) or **process** (records are
   substantively compliant but the tool needs improvement).
3. **Material:** Notify GC. Consider self-reporting per the firm's
   self-reporting policy. Remediate via version bump under
   `12-version-lock.md`. Communicate with affected clients per firm
   policy if disclosures were inadequate.
4. **Process:** Version bump under `12-version-lock.md`. Update training.
5. Document in incident log.

### Category 2 — Records-system integration failure

Exported Arctic Edge artifacts fail to ingest into the firm's records
system, or are corrupted, lost, or duplicated.

**Examples:**
- API failure between Arctic Edge export and records-system import.
- localStorage data loss before export (browser cache cleared, hardware
  failure).
- Records-system data corruption.

**Response:**
1. IT identifies scope: which artifacts, which advisors, which period.
2. Reconstruct from available sources: advisor's local storage,
   firm-side logs, principal-review records.
3. If reconstruction is incomplete, document the gap and remediate per
   the firm's books-and-records gap procedure.
4. Self-reporting consideration if the gap is in mandatory records under
   17a-4 / 204-2 / FINRA 4511.
5. Root-cause analysis; fix the pipeline.

### Category 3 — Security incident

PII exposure traceable to Arctic Edge — e.g., a workstation compromised
with localStorage exfiltrated, an advisor's browser session hijacked.

**Response:**
1. Firm's CISO leads per firm's IR plan.
2. Reg S-P / NY DFS Part 500 incident-notification obligations
   evaluated (§ 500.17 — 72-hour notice to DFS).
3. State breach-notification statutes evaluated per firm's existing
   breach response.
4. Arctic Edge–specific scope: identify which `clientRef` records were
   in the compromised localStorage; map to client identities via firm
   CRM; notify affected clients per applicable statutes.

### Category 4 — Adverse exam finding

An SEC or FINRA exam cites Arctic Edge directly or cites a record
produced by Arctic Edge.

**Response:**
1. GC + CCO lead the firm's exam response per existing protocol.
2. Specific to Arctic Edge:
   - Provide the executed sign-off and version manifest covering the
     period under review.
   - Provide the template versions in force during the period.
   - Provide the monitoring and testing reports for the period.
   - Provide the version history and any superseding sign-offs.
3. If the finding criticizes the template or the auditor design:
   - Assess whether the position taken in this compliance package is
     consistent with the staff position.
   - If not, draft a revised template / checklist under
     `12-version-lock.md`.
   - Communicate the revision to other firms using Arctic Edge (if any),
     and to the package maintainer.

### Category 5 — Module logic defect

A non-template defect in a module — e.g., the Portfolio Risk Analyzer
mis-calculates VaR for a specific input pattern, the Concentration X-Ray
mis-handles a leveraged-fund weight.

**Response:**
1. Confirm and reproduce the defect.
2. Assess records impact: were any records produced under the defective
   logic? If so, scope and assess materiality (note that risk metrics
   are operational inputs to records, not records themselves — the
   defect propagates only if the Reg BI note relied on the defective
   metric).
3. Fix the module. Re-test.
4. If a regulated module changed (6 or 7), trigger re-sign-off.
5. If a non-regulated module changed, version-bump per
   `12-version-lock.md` and update the version manifest.
6. Document in incident log; communicate to advisors.

---

## Incident log

The firm maintains an Arctic Edge incident log, owned by the CCO,
containing:

| Field | Description |
|---|---|
| Incident ID | Sequential or UUID |
| Discovered date | When the firm became aware |
| Category | 1–5 above |
| Description | What happened |
| Scope | Records, advisors, period affected |
| Materiality assessment | Material / process / cosmetic |
| Response | What the firm did |
| Root cause | Why it happened |
| Remediation | What changed |
| Closed date | When fully remediated |
| Cross-references | Sign-off bump, training update, regulatory filing |

The log is retained for the firm's records-retention period applicable
to compliance program documentation.

---

## Notification responsibilities

| Audience | When notified | By whom |
|---|---|---|
| GC | Any Category 1 (material), 3, 4 | CCO |
| CISO | Any Category 3 | CCO or IT |
| Head of Supervision | Any incident affecting records | CCO |
| Affected advisors | Category 1, 2, 5 | CCO or designate |
| Regulators | Per category and statute | GC |
| Clients | Per statute (Category 3) or firm self-reporting policy (Category 1 material) | Firm's existing client-communications protocol |

---

## Drills

The firm runs an Arctic Edge incident drill annually as part of its
incident-response readiness program. A typical drill:

> A Category 1 (template defect) is simulated: the CCO discovers that
> the "alternatives considered" field in `reg-bi-note/v1` does not
> require the alternative to be named (only that "alternatives were
> considered" be asserted). Affected advisors are notified; scope is
> determined; a draft `v1.1` is produced; the re-sign-off workflow is
> exercised end-to-end.

Outcome: timing and process gaps identified; the firm's IR plan updated
if needed.
