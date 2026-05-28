# Version Lock Policy

**Audience:** CCO, Compliance Operations.
**Purpose:** How template versions are locked, changed, and tracked.

---

## Why version lock matters

Reg BI compliance records must reflect the rules and the firm's procedures
as they existed **at the time of the recommendation**. A note written
against an old template that the firm has since revised must remain
auditable against the version under which it was written.

Version lock also creates a clear chain of CCO accountability: each
template version has a signed sign-off, and every record produced under
that version carries the version tag.

---

## Locked artifacts

The version lock applies to:

1. **Regulated templates** (require CCO sign-off):
   - `reg-bi-note/v1` (and any tailored variant, e.g., `/annuity-v1`)
   - `reg-bi-checklist/v1`

2. **Operational contracts** (do not require sign-off but are tagged):
   - `ips-record/v1`
   - `recommendation-event/v1`
   - `trade-thesis/v1`
   - `portfolio-risk/v1`
   - `four-quadrant-risk/v1`
   - `equity-tearsheet/v1`
   - `concentration-xray/v1`
   - `note-audit/v1`

3. **Module source code** for the two regulated modules (Modules 6, 7).
   Tracked by git commit SHA at sign-off.

---

## Version manifest

The firm maintains a version manifest, owned by the CCO, listing:

| Field | Description |
|---|---|
| Artifact | The named template or contract |
| Version | Semantic version (`v1`, `v1.1`, `v2`) |
| Effective from | Date the version goes live |
| Effective until | Date superseded (blank if current) |
| Sign-off doc | Path or reference to executed `11-sign-off-template.md` for this version |
| Source SHA | Git commit SHA of the module source at the time of sign-off |
| Notes | Free-text — what changed and why |

The manifest is updated at every sign-off and superseding.

---

## Semantic versioning

| Change type | Bump | Example |
|---|---|---|
| Wording in template that does not change required fields or substantive disclosure | Patch / no version bump if material; firm decides | "Best regards" → "Sincerely" |
| Addition or removal of a required field | Minor version bump (`v1` → `v1.1`) | Adding "Form CRS delivered Y/N" field |
| Change to checklist element list or cue phrases | Minor version bump | Adding "share class" to cost cue list |
| Material change in disclosure language driven by regulatory change | Major version bump (`v1` → `v2`) | Updating conflict disclosure to reflect new SEC guidance |
| Adding a separate template variant (e.g., annuity) | New version stream (`annuity-v1`) | Annuity Reg BI note template |

Major version bumps **always require a new sign-off**. Minor bumps
require a new sign-off when the change is regulated work product. Patch
changes (e.g., typo fixes) require CCO review but may be batched into
the next sign-off rather than triggering an immediate one — firm policy.

---

## Supersession workflow

1. **Draft.** The CCO or designate drafts the proposed new version.
2. **Review.** General Counsel and (if applicable) outside counsel
   review.
3. **Sign-off.** A new `11-sign-off-template.md` is executed referencing
   the new version. The prior sign-off remains in effect for records
   produced under the prior version.
4. **Deploy.** The new version is deployed to the workstation. Old
   versions remain available in source control.
5. **Update manifest.** Effective dates updated. Old version's
   "effective until" is set to the new version's effective date.
6. **Training.** Advisor and principal training reflects the new
   version. The annual refresher curriculum
   (`09-training-curriculum.md`) covers version changes.
7. **Existing records.** Records produced under the old version
   **remain valid records under the old version**. They are not
   reissued. The version tag in the record is the audit anchor.

---

## What gets retained from prior versions

- The prior sign-off document, permanently.
- The prior template source, permanently (in source control).
- The prior records, per the firm's records-retention policy applicable
  to the artifact type.

The firm should never delete a prior version. The version is what
defends a record produced under it.

---

## Operational example

> **Day 0:** Firm signs off on `reg-bi-note/v1` and
> `reg-bi-checklist/v1`. Manifest entry created.
>
> **Day 200:** SEC publishes new staff bulletin on conflict disclosure
> in proprietary product recommendations.
>
> **Day 210:** CCO drafts `reg-bi-note/v1.1` and `reg-bi-checklist/v1.1`
> reflecting the new guidance.
>
> **Day 220:** GC reviews. CCO executes new sign-off.
>
> **Day 225:** Deployment. New notes produced from Day 225 onward use
> `v1.1`. Notes produced from Day 0 through Day 224 remain valid records
> under `v1` — the version tag in the record references the Day-0
> sign-off.
>
> **Day 240:** Advisor training refresher includes the `v1.1` changes.
>
> **Future SEC exam:** Examiner requests Reg BI records covering Day 0
> through Day 350. The firm produces records tagged `v1` (Day 0–224) and
> `v1.1` (Day 225–350), with both sign-off documents and both template
> versions, in a self-describing package.

---

## What does not require a version bump

- Cosmetic UI changes that do not affect the produced record.
- Bug fixes in non-regulated modules (Modules 1, 3, 4, 5, 8, 9).
- Performance improvements.
- Workstation chrome (the tab shell).

These changes are tracked in source control but do not flow through the
sign-off workflow. The CCO reviews quarterly module changelogs to
confirm no regulated logic changed silently. A change to a regulated
module that the CCO did not approve **is itself a finding** — the firm's
change-management process must catch it.
