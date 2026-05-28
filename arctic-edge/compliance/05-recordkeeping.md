# Recordkeeping

**Audience:** CCO, Head of Operations, IT.
**Purpose:** How Arctic Edge outputs fit the firm's existing books-and-records
program under SEC Rules 17a-3 and 17a-4 (broker-dealers), Adviser Act Rule
204-2 (RIAs), and FINRA Rule 4511.

---

## Position

**Arctic Edge does not constitute the firm's books-and-records system.** It
produces records; the firm's existing records system retains them. The firm's
17a-4 / 204-2 program — including the storage medium, retention schedule,
indexing, and accessibility requirements — is unchanged in scope. Arctic Edge
augments that program with structured, contemporaneous records that fit
cleanly into it.

---

## Outputs and their record category

| Arctic Edge artifact | Likely BD record category (17a-3) | Likely IA record (204-2) | Retention floor |
|---|---|---|---|
| `ips-record/v1` | Customer account information | Documents prepared for use with clients | Life of account + 3 years (BD); 5 years (IA) |
| `trade-thesis/v1` | Memoranda of brokerage orders / IA work papers | Records evidencing basis for recommendation | 3 years easy-access, 6 total (BD); 5 years (IA) |
| `recommendation-event/v1` | Order memoranda / IA records of recommendations | Records of recommendations | 3 / 6 years (BD); 5 years (IA) |
| `portfolio-risk/v1` | Work papers supporting recommendation | Records supporting investment advice | 3 / 6 years (BD); 5 years (IA) |
| `reg-bi-note/v1` | Reg BI compliance record (15l-1 record) | Documents prepared for clients | 6 years (BD); 5 years (IA) |
| `note-audit/v1` | Compliance review record | Compliance review record | Aligned with the note it audited |
| `equity-tearsheet/v1` | Communications with public (if distributed) | Communications with clients/prospects | 3 years (FINRA 2210); 5 years (IA 204-2(a)(11)) |
| `concentration-xray/v1` | Work papers | Records supporting investment advice | 3 / 6 years (BD); 5 years (IA) |

Retention floors are general defaults from the rules; firm policy may be
longer. The firm's General Counsel and CCO confirm the retention category
for each artifact type at sign-off.

---

## Format and accessibility

### Format

All Arctic Edge outputs are JSON conforming to a versioned contract (`/v1`).
JSON is text and qualifies as electronic record under both 17a-4 and 204-2.

### Accessibility

17a-4(b)(4) requires records be promptly accessible. JSON in the firm's
records system meets this requirement assuming the firm's system indexes
the artifact (client ID, advisor ID, date, contract type). Recommended index
fields:

- `clientRef` (ID or initials; never PHI)
- `advisorId`
- `createdAt` (ISO 8601)
- `contract` (e.g., `reg-bi-note/v1`)
- For notes: `recommendationEventId` (back-reference to Module 5 event)

### Audit-trail alternative (2022 17a-4 amendment)

The 2022 amendment to Rule 17a-4 permits an **audit-trail alternative** to
the original WORM (write-once-read-many) requirement. Under the audit-trail
alternative, records must:

- Be retained in a manner that ensures completeness and accuracy.
- Be capable of being prepared for review by examination staff.
- Have an audit trail of all changes including who, what, when.

The Arctic Edge architecture is **compatible with both regimes**:

- **WORM regime:** The firm exports the JSON artifact to its WORM store at
  the time of creation. Subsequent corrections appear as new records
  (supersession), not in-place edits.
- **Audit-trail regime:** Module 5 (Audit Trail) is itself append-only;
  Modules 1, 4, 6 produce versioned records where corrections supersede the
  prior version with a back-reference. The firm's records system retains
  the chain.

The firm chooses which regime its overall books-and-records program
operates under. Arctic Edge fits either.

---

## Versioning and supersession

Some Arctic Edge records can be superseded (e.g., a corrected IPS record
when a client's circumstances change). The rule: never edit in place. Always
write a new record that:

1. Has a new `createdAt` timestamp.
2. References the superseded record's ID in a `supersedes` field.
3. Carries a `reasonForChange` field (recommended).

The chain is preserved. The original record is not deleted from the firm's
records system; the firm's records policy governs how long the superseded
chain is retained (typically the same retention period as the current
version).

---

## Client PII handling

The note generator template uses `clientRef` (ID or initials) rather than
full name in the note body by default. This is a deliberate design choice:

- Notes are reviewed by principals, exported to firm systems, and may be
  produced to regulators. Minimizing PII in the body reduces exposure.
- The advisor system maps `clientRef` → client identity via the firm's CRM,
  which already operates under the firm's Reg S-P program.

A firm whose policy requires full name in the body can edit the template
default at sign-off. The data-handling implications are documented in
`13-data-handling.md`.

---

## What the firm operationalizes

To make Arctic Edge fit the records program, the firm operationalizes:

1. **Export pipeline.** When an Arctic Edge artifact is finalized, it
   exports as JSON into the firm's records system. This is the firm's IT
   integration responsibility.

2. **Index mapping.** The firm's records system indexes the artifact by
   the recommended fields above (clientRef, advisorId, createdAt, contract).

3. **Retention schedule.** The firm assigns each contract type to a
   retention bucket. The defaults above are starting points; the firm's
   GC/CCO confirms.

4. **Supersession policy.** The firm's records system retains superseded
   versions for the same period as current versions.

5. **Backup / disaster recovery.** Arctic Edge artifacts are included in
   the firm's existing backup / DR program. No special handling required.

---

## What an SEC / FINRA exam request looks like

A typical request would be:

> Produce all Reg BI compliance records for accounts opened between
> [date] and [date] for advisor [name].

With Arctic Edge integration, the firm's records system can produce, for
each account:

- The IPS record(s) covering the period.
- Every `recommendation-event/v1` in the period.
- Every `reg-bi-note/v1` in the period, with referenced `note-audit/v1`.
- Every superseding record with full chain.

Each record is timestamped, version-tagged, and references the others by ID.
The package is internally consistent and self-describing.

This is the kind of production that ends an exam quickly. The alternative —
producing assorted CRM notes, screenshots, and reconstructed timelines — is
the kind that draws follow-up requests and findings.
