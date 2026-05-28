# FAQ — Anticipated Questions and Answers

**Audience:** CCO, GC, CEO, exam staff, advisor leadership.
**Purpose:** Pre-empt the questions a serious reviewer asks. Honest answers,
not marketing.

---

## Strategic

### Q: Is Arctic Edge an AI tool?

Arctic Edge contains **no generative AI** in its current build. The
modules execute deterministic logic — math, validation, heuristic text
scans — that the firm's CCO can read, test, and explain. The "AI"
concern that the SEC and FINRA have publicly raised (post-hoc generative
rationale, opaque scoring, hallucinated facts) does not apply to the
Phase 1 build.

A future phase may introduce an LLM-assisted drafting helper for free-text
fields. If that happens, the helper will (a) operate only on advisor
input the advisor has already entered, (b) leave the deterministic
modules unchanged, and (c) require its own CCO sign-off.

### Q: How is this different from the AI chatbot tools advisors are using today?

| Aspect | General-purpose AI | Arctic Edge |
|---|---|---|
| Output | Free-form prose | Structured record against a versioned template |
| Inputs | Conversational | IPS, thesis, event — captured before the note |
| Substitutes for advisor judgment | Implicitly (it picks words and frames the case) | No (template asks structured questions; advisor answers) |
| Auditability | Low (no source for the rationale) | High (each field traces to a captured record) |
| Regulatory posture | Regulator-flagged | Designed to the rules |

### Q: Why isn't this just a CRM feature?

Most CRMs have free-text note fields. Some have suggested-text templates.
None enforce the workflow order (IPS → thesis → event → note → audit)
because none own the underlying records. A CRM note is a record of
*what the advisor wrote*. Arctic Edge is a record of *what the advisor
considered and when*.

The two are complementary. The CRM is the system of record for client
relationships. Arctic Edge produces the artifacts that go into it. A
firm-side integration would push Arctic Edge artifacts into the CRM
record automatically.

### Q: What's stopping a firm from just copying this idea?

Nothing. The rules are public. The approach is right because it follows
the rules; that's not novel, that's correct. Two things create durable
advantage anyway:

1. **First-mover on standards.** The reference implementation gets cited
   by other firms and (eventually) regulators. Being first matters.
2. **Implementation depth.** Templates tailored to a specific firm's
   product mix, share-class structure, and conflict inventory are not
   trivial to reproduce. The tailored templates are firm IP.

---

## Compliance / regulatory

### Q: Does using Arctic Edge satisfy Reg BI?

No tool satisfies Reg BI by itself. The firm's program satisfies Reg BI.
Arctic Edge is a tool that makes the program operationally enforceable.
The CCO's sign-off in `11-sign-off-template.md` documents the firm's
position that Arctic Edge is part of its Reg BI program.

### Q: If the auditor passes a note, is it Reg BI–compliant?

No. The auditor is a heuristic preflight. It confirms the cue phrases are
present. It does not confirm the substance is adequate. **Principal
review under FINRA 3110 is the substantive check.** The audit pass is
information; the principal's review is the supervisory record.

### Q: What if an advisor consistently passes auditor flags by adding cue phrases without substance?

The principal catches it (substance review). Compliance testing catches
it (sampling against the checklist by manual review per
`10-monitoring-and-testing.md`). The CCO addresses it (coaching,
discipline, or — if pattern — workstation revocation).

The auditor is not adversarial software. An advisor gaming the auditor
is the advisor's choice; the firm's supervisory structure catches it.

### Q: Why don't you log auditor overrides?

Three reasons (detailed in `03-reg-bi-deep-dive.md`):

1. **Substitution.** A logged override implies the auditor's judgment
   matters as a decision; it does not. The principal's review is the
   decision.
2. **Discoverability.** An override log creates a record of advisor
   disagreement with software. The record is operationally useless and
   litigation-hazardous.
3. **Chilling effect.** Advisors aware of an override log will avoid
   acting on judgment even when they should.

A non-logging design is the deliberate choice. The trade-off is that the
firm cannot show "advisors override the auditor X% of the time" — which
is fine, because that metric is also not useful.

### Q: Does this work for both broker-dealers and RIAs?

Yes. The reg-bi-note template can satisfy Reg BI (BD) and the
Adviser Act fiduciary duty of care (RIA) in a single record. Dual-
registered firms operate under both, with the template tailored
appropriately. See `04-cfp-standards-mapping.md` for CFP overlay.

### Q: What about annuities, options, structured products?

Annuities have their own best-interest regime under NAIC Model #275 (2020).
The reg-bi-note template can be configured with an annuity variant; that
variant requires separate CCO sign-off (see `11-sign-off-template.md`
section 2f).

Options recommendations are subject to FINRA 2360 in addition to Reg BI.
The template can be configured with an options variant; separate sign-off.

Structured products are subject to FINRA Regulatory Notice 12-03 and
related guidance. Template variant; separate sign-off.

These variants are **not in scope for Phase 1**. Firms doing significant
business in these products will tailor and sign off on variants before
using Arctic Edge for those recommendations.

### Q: Is Arctic Edge a "regulated AI" under any pending state law?

Several states have proposed or enacted AI regulations (e.g., NYC Local
Law 144 on AI in hiring; Colorado AI Act for high-risk AI; CA SB 1047
attempts). The Phase 1 build contains no AI — see first FAQ above. If
a future phase introduces LLM-assisted drafting, the firm's GC assesses
fit with applicable AI law at that time.

---

## Operational

### Q: How long does an advisor's first month with Arctic Edge take?

Initial training is 90 minutes (`09-training-curriculum.md`). After
training, advisors typically reach steady-state within 2–4 weeks.
First-week note generation often takes longer than the advisor's prior
process (learning the template); by week 4, most advisors are at parity
or faster than their prior process.

### Q: What happens to existing notes from before deployment?

They remain valid records under whatever process produced them. Arctic
Edge does not retroactively re-document prior recommendations.

### Q: Can we still hand-write notes when we want to?

The firm decides. The default WSPs that the firm would update at sign-off
typically require Arctic Edge for new Reg BI documentation; the firm
can carve out specific scenarios (e.g., emergency trade conditions where
the advisor logs the event in Arctic Edge but writes a free-form
narrative). Carve-outs are firm policy.

### Q: What if the workstation is unavailable (firm IT outage)?

Arctic Edge runs in the browser. If the firm hosts it from an internal
URL, an outage of that URL is an issue. Recommended posture:

- Host Arctic Edge as a static HTML deployment (high availability, low
  failure surface).
- Maintain a "downtime procedure" — advisors continue to capture the
  same elements in the firm's CRM as free-form fields, and re-enter into
  Arctic Edge when service is restored.
- Records produced during downtime are still valid records; they just
  don't carry the Arctic Edge version tag.

### Q: How is Arctic Edge updated?

See `12-version-lock.md`. Module source updates that affect non-regulated
modules: standard change management. Updates to regulated modules
(Modules 6, 7) or templates: re-sign-off.

### Q: Who owns the source code?

The Arctic Edge code is owned by [Arctic Edge entity]. Firms license use
under terms specified in the license agreement. The compliance package
(this document set) is part of the licensed product.

### Q: Can we self-host?

Yes. Arctic Edge is single-file HTML with no server-side dependency. The
firm can deploy from any static-hosting infrastructure under its
control. Self-hosting eliminates the § 500.11 vendor relationship for
the application; the firm assesses itself instead of an external vendor.

---

## Exam-readiness

### Q: What does an exam look like with Arctic Edge?

Faster. The records are structured, version-tagged, internally
referenced, and exportable. An SEC or FINRA examiner who asks for "the
Reg BI compliance records for accounts opened between X and Y" receives
a self-describing JSON package per account, plus the signed templates
and the version manifest covering the period.

Compare to status quo: assorted CRM notes, screenshots, trade
confirmations, and reconstructed timelines. The Arctic Edge package is
the difference between an exam that closes cleanly and one that draws
follow-up requests.

### Q: What if a regulator says the auditor design (non-blocking,
non-logging) is inadequate?

The position is defensible (see `03-reg-bi-deep-dive.md`). It rests on:

- FINRA 3110 places supervisory authority on the principal, not on
  software.
- Affirmative, non-blocking software aids supervision without
  substituting for it.
- Override logs create discoverable records of advisor-software
  disagreement that have no regulatory significance.

If a regulator challenges the position in a specific exam, the firm
defends it. If a regulator publishes guidance contrary to the position,
the firm reconsiders under `14-incident-response.md`.

### Q: What if a regulator asks why we trust Arctic Edge?

The firm doesn't "trust" Arctic Edge. The firm trusts its own program,
of which Arctic Edge is a tool. The CCO has reviewed and signed off on
the templates and design. The firm tests Arctic Edge usage in its
annual compliance program review. The firm's principal review remains
the substantive check. Arctic Edge is a structured input to the firm's
existing program; the firm owns the program.

---

## Honest limitations

### Q: What can't Arctic Edge do?

- It cannot ensure the underlying recommendation is good. A bad
  recommendation, well-documented, is still a bad recommendation.
- It cannot detect intent. An advisor who fabricates a thesis to fit a
  pre-decided trade can do so; the firm's supervisory program (and the
  advisor's CRD record) is what catches that pattern.
- It cannot replace the principal's substantive review.
- It cannot guarantee an exam will close cleanly. It can only ensure
  the records produced reflect the rules.
- It is not a substitute for competent legal advice on any specific
  recommendation.

### Q: What is it definitively good at?

- Enforcing the order of operations (IPS → thesis → event → note).
- Producing structured, version-tagged, exportable records.
- Reducing variance in documentation quality across advisors.
- Surfacing concentration and risk facts that advisors would otherwise
  miss.
- Making exam production fast and clean.
- Giving principals a richer review picture than free-form notes.
