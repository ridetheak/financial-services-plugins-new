# Monitoring and Testing

**Audience:** CCO, Internal Audit, Compliance Testing.
**Purpose:** The annual testing program for Arctic Edge under Adviser Act
Rule 206(4)-7 (RIA) and the equivalent FINRA 3120 / 3130 framework (BD).
This is the substance the firm reports in its annual compliance review.

---

## Annual testing program

### Testing universe
The annual review covers:

1. **Signed templates.** Are `reg-bi-note/v1` and `reg-bi-checklist/v1`
   still appropriate given current regulatory guidance and firm
   business?
2. **Auditor effectiveness.** Are the cue phrases catching the gaps
   they were designed to catch?
3. **Note quality.** Are the produced notes substantively complete?
4. **Workflow adherence.** Are advisors using the modules in the
   intended order (IPS → thesis → event → note → audit)?
5. **Principal review.** Are principals catching what they should?

### Testing methods

| Test | Method | Frequency | Sample |
|---|---|---|---|
| **Template currency** | CCO + GC review of signed templates against any new SEC/FINRA guidance, staff bulletins, examination priorities | Annually + on guidance change | All locked templates |
| **Auditor effectiveness** | Internal audit manually scores a sample of notes against the checklist; compares to Module 7 results | Quarterly | 5% of notes per advisor, minimum 5 per advisor |
| **Note substantive quality** | Compliance testing reviews a sample for substantive Reg BI elements (not just cue presence) | Quarterly | 5% of notes per advisor, minimum 5 per advisor |
| **Workflow adherence** | Pull `recommendation-event/v1` events and confirm linked IPS and (where applicable) thesis exist at correct timestamps | Quarterly | All events for sampled advisors |
| **Principal review timeliness** | Pull principal queue metrics | Monthly | All notes |
| **Principal return reasons** | Categorize return reasons; identify training opportunities | Quarterly | All returns |

### Testing report

The annual report includes:

- Universe size (notes, events, IPSes, theses) for the period.
- Sampling methodology and sample size.
- Findings, categorized as:
  - **Material:** rule or template breach; remediation required.
  - **Process:** workflow drift or training gap; coaching response.
  - **Observation:** improvement opportunity; logged for next cycle.
- Trend data vs. prior year.
- Recommendations.

The report is filed with the firm's compliance records and made available
to regulators on request.

---

## What "auditor effectiveness" testing looks like

Pull a sample of 20 notes per advisor for the quarter. For each note:

1. Run the Module 7 audit. Record the result.
2. A compliance reviewer manually scores against the checklist (without
   reference to the Module 7 result).
3. Compare:
   - **True positive:** Auditor flagged; reviewer also identifies gap.
   - **False positive:** Auditor flagged; reviewer says element is
     adequately present. (Indicates cue phrase needs supplementation.)
   - **True negative:** Auditor passed; reviewer confirms present.
   - **False negative:** Auditor passed; reviewer identifies gap.
     **This is the important one.**

Targets:
- False negatives: < 2% (substantive failures the auditor missed).
- False positives: < 15% (acceptable cost of an affirmative system).

If false negatives are above target, the cue phrase list needs revision.
The CCO drafts an update, re-signs, version-bumps under
`12-version-lock.md`.

---

## Workflow adherence testing

For each sampled recommendation event:

| Check | Pass criteria |
|---|---|
| IPS exists | A non-superseded `ips-record/v1` exists with effective date ≤ event timestamp |
| IPS referenced | Event's `ipsRecordId` matches the active IPS |
| Thesis (if applicable for the trade type) | A `trade-thesis/v1` exists with timestamp ≤ event timestamp |
| Note produced | A `reg-bi-note/v1` exists referencing the event ID |
| Audit run | A `note-audit/v1` exists referencing the note |
| Note approved | Principal review record exists |

Gaps are categorized:

- **Material:** Event with no note (Reg BI documentation gap).
- **Process:** Note generated without thesis on a discretionary
  recommendation (not a Reg BI gap per se; a workflow gap).
- **Observation:** Note generated with a thesis whose exit condition is
  vague.

---

## Continuous monitoring (between annual reviews)

Quarterly dashboards reviewed by the CCO:

- Notes generated per advisor per period.
- Auditor flag distribution (which element, how often).
- Principal return rate, return reasons.
- Time-to-approval distribution.
- Volume of `recommendation-event/v1` by origin (solicited vs.
  unsolicited).

Triggers for ad-hoc review:

- Advisor with auditor flag rate > 2x firm average.
- Advisor with principal return rate > 2x firm average.
- Note volume drop > 30% month-over-month without explanation.
- Recommendation-event volume sustained > 2x peer benchmark (potential
  excessive trading; FINRA 2111 quantitative suitability).

---

## Regulatory-development monitoring

The CCO maintains a watch on:

- **SEC**: Reg BI staff bulletins, examination priorities, enforcement
  actions citing Reg BI.
- **FINRA**: Regulatory notices on AI use, suitability, supervision.
- **CFP Board**: Standards revisions and Disciplinary actions citing
  documentation.
- **States**: NAIC Model #275 adoption status, state Best Interest rules
  (e.g., NJ, MA).
- **Litigation**: Civil cases against advisors/firms on Reg BI grounds.

Any material development triggers a template review under
`12-version-lock.md`.

---

## Documentation

All testing and monitoring documentation is filed in the firm's
compliance records, retained for the firm's records-retention period
(generally 5 years for IA; 3 / 6 years for BD).
