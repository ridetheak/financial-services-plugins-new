# 90-Day Pilot Plan

**Audience:** CCO, Head of Supervision, Pilot Sponsor.
**Purpose:** Concrete plan for a 90-day pilot. Read this as a runbook.

---

## Pilot principles

1. **Real work, real records.** The pilot produces actual Reg BI records
   filed in the firm's recordkeeping system. It is not a sandbox. The
   templates are CCO-signed before pilot start.
2. **Small team, mixed profile.** 3–5 advisors covering different seniority
   levels, book sizes, and product mixes. Mixed signal beats clean signal.
3. **Time-boxed.** 90 days. Decision at Day 90: expand, extend, or
   discontinue.
4. **Bound by the sign-off.** Pilot operates inside the executed sign-off.
   Any template change during the pilot triggers re-sign-off under
   `12-version-lock.md` before the change goes live.

---

## Pre-pilot (Day −14 to Day 0)

| Activity | Owner | Output |
|---|---|---|
| Select 3–5 advisors | Sponsor + Head of Supervision | Pilot roster |
| Identify principal reviewer(s) for pilot | Head of Supervision | Principal assignment |
| Confirm sign-off executed | CCO | Filed sign-off |
| Confirm templates locked | CCO | Version manifest |
| IT provisioning | Head of IT | Advisor access |
| Training for pilot cohort | Training Coordinator | Training completion |
| Pre-pilot internal-audit baseline | Internal Audit | Baseline metrics |

The pre-pilot internal-audit baseline is important. Pull a sample of the
last 30 Reg BI notes from each pilot advisor. Score them against the
`reg-bi-checklist/v1` manually. This establishes the "before" picture.

---

## Pilot operations

### Day 1
- Advisors begin using Arctic Edge for **all** new Reg BI documentation.
- Existing in-flight workflows complete under prior process; new
  recommendations use Arctic Edge.
- Daily standup check-in (10 minutes) for the first five business days.

### Days 2–14 — Stabilization
- Daily standups continue through Day 5; then weekly.
- Track friction issues (UI confusion, missing template options, slow
  workflows) in a shared issue log.
- Track Module 7 flag false-positive patterns — if a specific cue phrase
  consistently misses the firm's note style.

### Days 15–60 — Steady state
- Weekly pilot meeting (30 minutes): advisors + principal + CCO.
- Standing agenda:
  - Volume by module.
  - Auditor flag distribution.
  - Principal return rate.
  - Open issues.
- Internal audit pulls a sample of notes weekly and scores against the
  checklist manually (independent of the auditor).

### Days 60–90 — Decision preparation
- Internal audit produces a Day-75 interim report.
- CCO drafts the Day-90 go / no-go memo.
- Pilot advisors complete the satisfaction survey (template below).

---

## Metrics

### Lead indicators (track weekly)

| Metric | Definition | Target |
|---|---|---|
| Volume — notes generated | Count of `reg-bi-note/v1` per advisor per week | Baseline ± 10% |
| Volume — events logged | Count of `recommendation-event/v1` per advisor per week | Baseline or higher |
| Auditor flag rate | Notes with ≥1 flag / total notes | Track trend (expected: declining as advisors learn template) |
| Time to first flag resolution | Hours from auditor result to principal queue submission | < 24 hours |

### Outcome indicators (Day-90 evaluation)

| Metric | Definition | Target |
|---|---|---|
| Principal return rate | Notes returned by principal / total reviewed | At or below pre-pilot baseline |
| Time to principal approval | Hours from advisor submission to principal approve | At or below pre-pilot baseline |
| Internal-audit completeness score | Manual checklist score on sampled notes | ≥ 90% of elements present |
| Advisor satisfaction | 5-point scale, post-pilot | ≥ 3.5 average |
| Principal satisfaction | 5-point scale, post-pilot | ≥ 3.5 average |
| Records-system ingestion errors | Count of failed ingestions | Zero |

### Disqualifying signals

If any of the following happens during the pilot, **escalate to CCO and
sponsor immediately**:

- Module 7 reported as "blocking" advisors. (This indicates a UX or
  training issue; the module is non-blocking by design.)
- A pilot advisor opts out claiming the system makes notes worse.
- A principal reviewer reports that Arctic Edge notes are harder to
  review than free-form notes.
- Any records-system data-integrity issue.
- Any apparent regulatory deficiency in a pilot record that would not
  have existed in the firm's prior process.

---

## Day-90 decision

### Expand — criteria
- Outcome indicators at or better than target.
- No disqualifying signals.
- Advisor and principal feedback constructive.
- CCO endorses firm-wide rollout.

### Extend — criteria
- Mixed indicators; some targets missed but trend is improving.
- Specific issues identified that need 30–60 days of additional work.
- No disqualifying signals.

### Discontinue — criteria
- Disqualifying signals not remediable.
- Outcome indicators substantially below target with no clear remediation
  path.
- CCO declines to endorse firm-wide rollout.

The decision is made jointly by the CCO, the sponsor (CEO or COO), and
the Head of Supervision. The decision and rationale are documented and
filed.

---

## Advisor satisfaction survey (template)

Provide as a one-page survey at Day 85.

> 1. Compared to your prior Reg BI note process, Arctic Edge is
>    [much easier / easier / about the same / harder / much harder].
>
> 2. The Module 7 auditor's flags were
>    [very useful / useful / neutral / annoying / very annoying].
>
> 3. The structured note template made my notes
>    [more thorough / about the same / less thorough] than my prior style.
>
> 4. Time spent on note generation, on average, has
>    [decreased significantly / decreased / stayed flat / increased / increased significantly].
>
> 5. If the firm rolled this out to everyone tomorrow, my reaction would be
>    [positive / cautiously positive / neutral / cautiously negative / negative].
>
> 6. What is one thing about Arctic Edge that should change?
>    [free text]
>
> 7. What is one thing about Arctic Edge that should not change?
>    [free text]

---

## Principal satisfaction survey (template)

> 1. Reviewing a structured Arctic Edge note vs. a free-form note is
>    [faster / about the same / slower].
>
> 2. The `note-audit/v1` result was
>    [useful in directing my review / occasionally useful / not useful].
>
> 3. The IPS / thesis / event back-references that the advisor populated were
>    [accurate and helpful / mostly accurate / sometimes inaccurate / not helpful].
>
> 4. Notes I returned to advisors during the pilot, on average, had
>    [fewer / about the same / more] substantive issues than pre-pilot notes.
>
> 5. If the firm rolled this out to everyone tomorrow, my reaction would be
>    [positive / cautiously positive / neutral / cautiously negative / negative].
>
> 6. What additional information would make my review easier?
>    [free text]
