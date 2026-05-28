# CFP Standards of Conduct Mapping

**Audience:** CCO at a firm employing CFP® professionals; CFP® professionals
themselves.
**Source:** Certified Financial Planner Board of Standards, Inc., *Code of
Ethics and Standards of Conduct*, effective October 1, 2019 (as amended).

CFP Board Standards apply to CFP® professionals at all times when providing
Financial Advice (Standard A.1.a) — not only at the time of a transaction.
This is a broader scope than Reg BI. A firm employing CFP® professionals must
ensure its tooling supports their personal duty as CFP® holders, even when
the firm itself is not subject to fiduciary duty under Reg BI alone.

---

## Standard A.1 — Fiduciary Duty

> At all times when providing Financial Advice to a Client, a CFP®
> professional must act as a fiduciary, and therefore, act in the best
> interests of the Client. The following duties must be fulfilled:
> (a) Duty of Loyalty
> (b) Duty of Care
> (c) Duty to Follow Client Instructions

| CFP Sub-duty | Arctic Edge module(s) | How |
|---|---|---|
| A.1.a Duty of Loyalty | Module 6 (conflicts field, affirmative) | Required conflict statement; cannot be blank |
| A.1.b Duty of Care | Modules 1, 3, 4, 6 | IPS profile; deterministic risk; pre-trade thesis; care-basis field |
| A.1.c Duty to Follow Client Instructions | Module 5 (origin = unsolicited) | Captures when the client directed the transaction |

---

## Standard A.2 — Integrity

Honesty and candor. Not a process duty; not implemented in software. Arctic
Edge supports integrity by making the record visible — an advisor cannot
quietly omit material facts because the templates and audit prompt for them.

---

## Standard A.3 — Competence

The CFP® professional must have the relevant knowledge and skill. Not a
process duty; Arctic Edge does not substitute for competence. It provides
the structure that lets the competent CFP® professional record their work
efficiently.

---

## Standard A.4 — Diligence

> A CFP® professional must provide Professional Services, including
> responding to reasonable Client inquiries, in a timely and thorough manner.

| Element | Arctic Edge module |
|---|---|
| Timeliness of record | All modules timestamp at write |
| Thoroughness of record | Module 6 + 7 (required fields + completeness check) |

---

## Standard A.5 — Disclose and Manage Conflicts of Interest

> A CFP® professional must:
> (a) Make Full Disclosure of all Material Conflicts of Interest with
>    the CFP® professional's Client that could affect the professional
>    relationship.
> (b) Provide the Client with sufficiently specific facts so that a
>    reasonable Client would be able to understand the CFP®
>    professional's Material Conflicts of Interest.

| Element | Arctic Edge module |
|---|---|
| Affirmative disclosure | Module 6 `conflicts` field, required |
| Specificity | Template tailoring at sign-off — firm enumerates known conflict types in the conflict picker |

The default Module 6 template provides a structured conflict input rather
than a free-text box, so the advisor is prompted with the firm's known
conflict inventory (e.g., "12b-1 fee on this share class," "proprietary
product," "rep selects share class"). This drives the specificity required
by A.5(b).

---

## Standard A.6 — Sound and Objective Professional Judgment

> A CFP® professional must exercise professional judgment on behalf of the
> Client that is not subordinated to the interest of the CFP® professional
> or others.

Arctic Edge does not exercise judgment for the advisor. The Four-Quadrant
Risk Framework explicitly refuses to produce a single score. The Portfolio
Risk Analyzer suggests but does not set Quadrant 1. The Module 7 auditor is
non-blocking.

---

## Standard A.8 — Provide Information to a Client

> A CFP® professional must provide the following information to the Client …
> in writing:
> (a) Description of the Services and Products to be provided.
> (b) How the Client pays for the Products and Services, and the cost
>    to the Client …
> (c) How the CFP® professional, the CFP® Professional's Firm, and any
>    Related Party are compensated for providing the Products and
>    Services.
> (d) Existence of any public disciplinary history, any bankruptcy …
> (e) Conflicts of interest.

| A.8 Element | Arctic Edge module |
|---|---|
| (a) Products / services | Module 6 `recommendation` field |
| (b) Cost to client | Module 6 `costs` field |
| (c) Compensation | Module 6 `conflicts` field (compensation conflicts) |
| (d) Public disciplinary / bankruptcy | Firm-side; not module-level |
| (e) Conflicts | Module 6 `conflicts` field |

---

## Standard A.10 — Documentation

> Where required to comply with the Practice Standards for the Financial
> Planning Process … a CFP® professional must act prudently in documenting
> information.

Arctic Edge produces structured, versioned, timestamped, machine-readable
documentation across all six steps of the CFP financial-planning process
(Standard C):

| CFP Step | Arctic Edge support |
|---|---|
| C.1 Understanding the Client's Personal and Financial Circumstances | Module 1 (IPS Record) |
| C.2 Identifying and Selecting Goals | Module 1 (objectives, constraints) |
| C.3 Analyzing the Client's Current Course of Action | Modules 3, 9 (current portfolio risk and concentration) |
| C.4 Developing the Financial Planning Recommendation(s) | Module 4 (thesis), Module 6 (note) |
| C.5 Presenting the Financial Planning Recommendation(s) | Module 6 output |
| C.6 Implementing the Financial Planning Recommendation(s) | Module 5 (event log) |
| C.7 Monitoring Progress and Updating | Modules 3, 5 (ongoing) |

---

## Bringing it together for a CFP® firm

A firm that employs CFP® professionals and chooses to use Arctic Edge is
operationally aligned with:

- The Reg BI obligations its non-CFP advisors face.
- The broader fiduciary duty the CFP® professionals face under Standard A.1.
- The documentation duty under Standard A.10.
- The disclosure duty under Standard A.8.

A single template (`reg-bi-note/v1`) tailored for both Reg BI and CFP
purposes is operationally efficient and avoids parallel documentation
streams. The firm's CCO and the firm's CFP® compliance officer (often the
same person at smaller firms) sign off jointly.
