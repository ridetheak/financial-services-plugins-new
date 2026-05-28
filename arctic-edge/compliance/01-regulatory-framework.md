# Regulatory Framework

**Audience:** CCO, General Counsel, Head of Compliance Testing.
**Purpose:** Direct citations for every rule Arctic Edge touches.

This document does not paraphrase. It cites. Each section names the rule,
identifies the operative language, and states which Arctic Edge module(s)
address it.

---

## 1. Regulation Best Interest (Reg BI) — 17 CFR § 240.15l-1

**Effective:** June 30, 2020.
**Applies to:** Broker-dealers and associated persons making a recommendation
of any securities transaction or investment strategy to a retail customer.

Reg BI imposes a **General Obligation** to act in the retail customer's best
interest at the time the recommendation is made, satisfied by complying with
four component obligations:

### 1a. Disclosure Obligation — § 240.15l-1(a)(2)(i)

> Prior to or at the time of the recommendation, [the broker-dealer must]
> provide the retail customer, in writing, full and fair disclosure of:
> (A) all material facts relating to the scope and terms of the relationship
> with the retail customer …;
> (B) all material facts relating to conflicts of interest that are
> associated with the recommendation.

**Arctic Edge mapping:**
- Module 6 (Reg BI Note Generator) — `disclosure` field required.
- Module 7 (Note Completeness Auditor) — `disclosure` element on checklist.
- Module 1 (IPS Module) — relationship scope captured at engagement.

### 1b. Care Obligation — § 240.15l-1(a)(2)(ii)

> In making the recommendation, [the broker-dealer must] exercise reasonable
> diligence, care, and skill to:
> (A) understand the potential risks, rewards, and costs … and have a
> reasonable basis to believe that the recommendation could be in the best
> interest of at least some retail customers;
> (B) have a reasonable basis to believe that the recommendation is in the
> best interest of a particular retail customer based on that retail
> customer's investment profile and the potential risks, rewards, and
> costs …;
> (C) have a reasonable basis to believe that a series of recommended
> transactions … is not excessive and is in the retail customer's best
> interest.

**Arctic Edge mapping:**
- Module 1 (IPS Module) — investment profile (objectives, risk tolerance,
  risk capacity, time horizon, constraints).
- Module 3 (Portfolio Risk Analyzer) — risks (deterministic).
- Module 4 (Trade Thesis Library) — basis for believing the recommendation
  is in best interest (variant perception, catalyst, exit condition,
  recorded **before** the trade).
- Module 6 — `care-basis` and `alternatives` fields required.
- Module 7 — `care-basis` and `alternatives` elements on checklist.
- Module 9 (Concentration X-Ray) — surfaces concentration risk against
  IPS constraints.

### 1c. Conflict of Interest Obligation — § 240.15l-1(a)(2)(iii)

> Establish, maintain, and enforce written policies and procedures
> reasonably designed to:
> (A) identify and at a minimum disclose, in accordance with the
> Disclosure Obligation, or eliminate, all conflicts of interest …;
> (B) identify and mitigate any conflicts of interest associated with
> recommendations that create an incentive for the natural person … to
> place the interest of the broker-dealer or such natural person ahead of
> the interest of the retail customer …

**Arctic Edge mapping:**
- Module 6 — `conflicts` field required; affirmative statement required
  (cannot be left blank; must say "none identified" if applicable).
- Module 7 — `conflicts` element on checklist.

### 1d. Compliance Obligation — § 240.15l-1(a)(2)(iv)

> Establish, maintain, and enforce written policies and procedures
> reasonably designed to achieve compliance with Regulation Best Interest.

**Arctic Edge mapping:** This obligation is the firm's, not Arctic Edge's.
Arctic Edge is a tool that makes compliance with the other three
obligations operationally enforceable. The CCO sign-off in
`11-sign-off-template.md` evidences the firm's written-policies adoption
of Arctic Edge as a tool in its Reg BI program.

---

## 2. SEC Form CRS — 17 CFR § 240.17a-14 and Schedule § 249.640

Form CRS (Customer Relationship Summary) must be delivered at or before the
earliest of: (a) making a recommendation to a retail investor, (b) opening
an account, (c) placing an order, or (d) entering into an investment
advisory contract.

**Arctic Edge mapping:**
- Module 6 — `disclosure` cue phrases include "Form CRS"; the auditor flags
  notes that do not reference Form CRS delivery if applicable.
- This is firm-by-firm; the template should be tailored to reflect the
  firm's CRS delivery process.

---

## 3. Investment Advisers Act of 1940 — Fiduciary Duty

**Applies to:** Registered investment advisers (federal- and state-registered).

The Adviser Act § 206 prohibits fraudulent, deceptive, or manipulative acts.
The SEC's 2019 Interpretation Regarding the Standard of Conduct for
Investment Advisers (Release No. IA-5248) codifies the federal fiduciary
duty as comprising:

- **Duty of Care:** to provide advice that is in the best interest of the
  client, to seek best execution, and to provide advice and monitoring over
  the course of the relationship.
- **Duty of Loyalty:** to eliminate or make full and fair disclosure of all
  material conflicts of interest.

**Arctic Edge mapping:**
- Module 1 (IPS Module) — establishes the client's profile against which
  advice is measured.
- Module 4 (Trade Thesis Library) — duty of care: the basis for the advice
  is documented before the advice is acted on.
- Module 6 — duty of loyalty: conflicts field is required.
- Module 5 (Audit Trail) — duty of care over the relationship: every
  recommendation event is logged with IPS context at the time.

The reg-bi-note template can be configured to satisfy both the Reg BI Care
Obligation and the Adviser Act duty of care in a single record; firms
operating in a dual-registered capacity should confirm this with their
General Counsel.

---

## 4. FINRA Rule 2111 — Suitability

**Applies to:** Member broker-dealers and associated persons for
recommendations not subject to Reg BI (e.g., recommendations to
institutional customers, or non-retail recommendations).

FINRA 2111 imposes three suitability obligations:

- **Reasonable basis** (the recommendation could be suitable for at least
  some investors)
- **Customer-specific** (the recommendation is suitable for this customer
  based on profile)
- **Quantitative** (a series of transactions is not excessive)

**Arctic Edge mapping:**
- Same modules as Reg BI Care Obligation. Module 6's template can produce
  a "FINRA 2111 suitability note" variant for non-retail recommendations.
- Phase 2 of the platform includes a Suitability Bridge contract; this is
  noted but out of scope for Phase 1 sign-off.

---

## 5. FINRA Rule 3110 — Supervision

**Applies to:** All FINRA members.

FINRA 3110(b) requires written supervisory procedures (WSPs) reasonably
designed to achieve compliance with applicable rules. Rule 3110(b)(2)
specifically requires review of:

> incoming and outgoing written (including electronic) correspondence and
> internal communications relating to the member's investment banking or
> securities business.

Trade notes generated by Module 6 fall within "internal communications
relating to securities business" and are subject to principal review.

**Arctic Edge mapping:**
- Module 7 (Note Completeness Auditor) is **affirmative and non-blocking
  by design**. It does not substitute for principal review under Rule 3110.
  See `06-supervision.md` for the supervisory model.
- The auditor flags apparent gaps; the principal still reviews.
- Module 5 (Audit Trail) is append-only, supporting the supervisory record.

---

## 6. FINRA Rule 4511 — General Recordkeeping

**Applies to:** All FINRA members.

> Members shall make and preserve books and records as required under the
> FINRA rules, the Exchange Act and the applicable Exchange Act rules.

**Arctic Edge mapping:**
- See `05-recordkeeping.md`. Every Arctic Edge output is exportable JSON
  with embedded timestamps and version tags suitable for ingestion into
  the firm's books-and-records system.

---

## 7. SEC Rule 17a-3 and 17a-4 — Broker-Dealer Records

**Applies to:** Broker-dealers.

- **Rule 17a-3** prescribes the records to be made.
- **Rule 17a-4** prescribes retention periods (generally 3–6 years; some
  records permanently) and format requirements (originally
  WORM/write-once; amended in 2022 to allow audit-trail alternative).

**Arctic Edge mapping:**
- Output artifacts are versioned JSON. The firm's recordkeeping system
  ingests them and applies the 17a-4 retention regime. Arctic Edge does
  not itself constitute the firm's recordkeeping system. See
  `05-recordkeeping.md`.

---

## 8. SEC Rule 204-2 — Investment Adviser Records

**Applies to:** Registered investment advisers.

Records to be maintained include written communications received and
copies of written communications sent, and records evidencing the basis
for recommendations to clients.

**Arctic Edge mapping:**
- Module 4 (Trade Thesis Library) and Module 6 (Reg BI Note Generator)
  jointly produce the "basis for recommendation" record. Module 5
  (Audit Trail) provides the immutable event log.

---

## 9. SEC Rule 206(4)-7 — Adviser Compliance Programs

> No investment adviser registered or required to be registered under
> section 203 of the Act … shall provide investment advice to clients
> unless such investment adviser has:
> (1) adopted and implemented written policies and procedures reasonably
> designed to prevent violation of the Act and the rules adopted by the
> Commission under the Act;
> (2) reviewed and assessed, no less frequently than annually, the
> adequacy of the policies and procedures and the effectiveness of their
> implementation; …

**Arctic Edge mapping:**
- `10-monitoring-and-testing.md` provides the annual testing program for
  the Arctic Edge component of the firm's compliance program.

---

## 10. CFP Board Code of Ethics and Standards of Conduct

**Applies to:** CFP® professionals.

The CFP Board's Standards of Conduct (effective October 1, 2019, as
amended) impose a fiduciary duty at all times when providing financial
advice. Relevant duties:

- **Fiduciary Duty** (A.1.) — duty of loyalty, duty of care, duty to
  follow client instructions.
- **Duty to Provide Information to a Client** (A.10.) — material conflicts
  of interest must be disclosed in writing.
- **Duty to Document** — Standard A.8.

See `04-cfp-standards-mapping.md` for full mapping.

---

## 11. Gramm-Leach-Bliley Act / Regulation S-P — Safeguarding

**Applies to:** Broker-dealers, RIAs, and other financial institutions.

Regulation S-P (17 CFR § 248) requires written policies and procedures
that address administrative, technical, and physical safeguards for the
protection of customer records and information.

**Arctic Edge mapping:**
- See `13-data-handling.md`. Arctic Edge holds all client data
  client-side; transmission and integration with custodian/firm systems
  is the firm's responsibility under its existing Reg S-P program.

---

## 12. NY DFS Cybersecurity Regulation — 23 NYCRR Part 500

**Applies to:** NY DFS-regulated entities (most NY-domiciled
broker-dealers and many RIAs).

Part 500 requires risk-based cybersecurity programs, including for
third-party service providers (§ 500.11).

**Arctic Edge mapping:**
- `13-data-handling.md` documents the architecture for third-party
  vendor assessment under § 500.11.

---

## 13. State Trust and Suitability Rules (Annuities, NAIC Model #275)

**Applies to:** Insurance-licensed advisors selling annuities in states
adopting the NAIC Suitability in Annuity Transactions Model Regulation
(Model #275, 2020 revision — the "best interest" amendment).

NAIC Model #275 (2020) imposes a best-interest standard substantively
similar to Reg BI for annuity recommendations. As of 2025, 48 states
have adopted some form.

**Arctic Edge mapping:**
- The reg-bi-note template can be configured with an `annuity` variant
  capturing the four obligations under NAIC Model #275 (care, disclosure,
  conflict, documentation). Phase 1 sign-off does not extend to the
  annuity variant; the firm tailors that template separately.

---

## Summary table

| Citation | Topic | Module(s) |
|---|---|---|
| 17 CFR § 240.15l-1(a)(2)(i) | Reg BI Disclosure | 6, 7 |
| 17 CFR § 240.15l-1(a)(2)(ii) | Reg BI Care | 1, 3, 4, 6, 7, 9 |
| 17 CFR § 240.15l-1(a)(2)(iii) | Reg BI Conflict | 6, 7 |
| 17 CFR § 240.15l-1(a)(2)(iv) | Reg BI Compliance | firm WSPs |
| 17 CFR § 240.17a-14 | Form CRS | 6 (template) |
| Adviser Act § 206 | Fiduciary duty | 1, 4, 5, 6 |
| FINRA 2111 | Suitability | 1, 3, 4, 6 |
| FINRA 3110 | Supervision | 5, 7 (informs, never substitutes) |
| FINRA 4511 | Recordkeeping | all (export contracts) |
| 17 CFR § 240.17a-3, 17a-4 | BD records | all (export contracts) |
| 17 CFR § 275.204-2 | IA records | 4, 5, 6 |
| 17 CFR § 275.206(4)-7 | IA compliance program | testing program (doc 10) |
| CFP Standards A.1, A.8, A.10 | CFP fiduciary | 1, 4, 5, 6 |
| 17 CFR Part 248 (Reg S-P) | Safeguarding | data handling (doc 13) |
| 23 NYCRR Part 500 | NY DFS cyber | data handling (doc 13) |
| NAIC Model #275 | Annuity best interest | 6 (annuity variant — not in Phase 1) |
