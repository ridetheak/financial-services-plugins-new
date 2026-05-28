# Template — Reg BI Checklist (`reg-bi-checklist/v1`)

**Status:** Generic checklist. Firms tailor before CCO sign-off.
**Regulated:** YES. Subject to `11-sign-off-template.md` Exhibit B.

This is the element list and cue-phrase set Module 7 uses to scan
finished trade notes. It is a heuristic and affirmative; it does not
substitute for principal review under FINRA 3110.

The producer module (`modules/note-completeness-auditor.html`)
enforces:

- All elements are scanned.
- `blocking: false` is hardcoded in the output.
- No override is logged when an advisor proceeds despite a flag.
- The output references the checklist version.

---

## Element list

Each element has:

- `id` — stable identifier.
- `name` — display name.
- `desc` — what the element is about (advisor-facing).
- `cues` — array of lowercase substrings; if ANY is found in the note,
  the element is marked **present**. Empty array means a special-case
  detection (see `date`).

### Element 1 — `recommendation`

| Field | Value |
|---|---|
| `name` | Recommendation stated |
| `desc` | The specific action and security are identified. |
| `cues` | `["recommend", "buy", "sell", "hold", "add to", "trim", "position"]` |

### Element 2 — `profile`

| Field | Value |
|---|---|
| `name` | Client investment profile |
| `desc` | Objective, risk tolerance, and time horizon are documented. |
| `cues` | `["objective", "risk tolerance", "risk capacity", "time horizon", "investment profile"]` |

### Element 3 — `care-basis`

| Field | Value |
|---|---|
| `name` | Care Obligation — basis for recommendation |
| `desc` | Why the recommendation is in the client's best interest. |
| `cues` | `["best interest", "basis for", "fits the", "care obligation", "suitable"]` |

### Element 4 — `alternatives`

| Field | Value |
|---|---|
| `name` | Reasonably available alternatives considered |
| `desc` | Other options were weighed — a core Reg BI requirement. |
| `cues` | `["alternative", "other options", "considered", "reasonably available"]` |

### Element 5 — `costs`

| Field | Value |
|---|---|
| `name` | Cost consideration |
| `desc` | Costs/fees of the recommendation were factored in. |
| `cues` | `["cost", "fee", "expense", "expense ratio", "commission"]` |

### Element 6 — `conflicts`

| Field | Value |
|---|---|
| `name` | Conflict of interest |
| `desc` | Material conflicts identified — or affirmatively stated as none. |
| `cues` | `["conflict", "no conflict", "none identified", "compensation"]` |

### Element 7 — `disclosure`

| Field | Value |
|---|---|
| `name` | Disclosure |
| `desc` | Disclosures provided to the client (Form CRS, fee schedule, etc.). |
| `cues` | `["disclos", "form crs", "fee schedule", "prospectus"]` |

### Element 8 — `date`

| Field | Value |
|---|---|
| `name` | Date |
| `desc` | The note is dated. |
| `cues` | `[]` — special detection |
| Detection | Regex: `\b\d{4}-\d{2}-\d{2}\b` OR `\b(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?\s+\d{1,2}` (case-insensitive) |

---

## Heuristic semantics

For elements 1–7:

- The note text is lowercased.
- For each element, if ANY substring in `cues` appears in the lowercased
  text, the element is marked **present**.
- Otherwise, the element is **flagged**.

For element 8 (`date`):

- The note text (preserving case) is matched against the regex.
- Match → present; no match → flagged.

The auditor returns a `note-audit/v1` document with each element as
present or flagged, the checklist version tag, the audited-at
timestamp, and the immutable `blocking: false` flag.

---

## What a "flag" means and what it does not mean

| What a flag means | What it does not mean |
|---|---|
| The cue phrase set did not detect this element in the note. | The element is missing from the note. |
| The advisor should review the note for this element. | The note is non-compliant. |
| The principal should consider this element during review. | The advisor must change the note. |
| Possible false positive — try paraphrase. | The system has rejected the note. |

The principal's substantive review is what determines whether an
element is adequately present, regardless of the auditor result.

---

## Tailoring guidance

When a firm tailors this checklist, the firm:

1. **May add cues**, never remove the defaults (without explicit
   discussion and re-sign-off). Adding firm-specific phrases that the
   firm's advisors actually use reduces false-positive flags. Examples:
   - For `care-basis`: add `["best interests", "appropriate for"]`.
   - For `conflicts`: add the firm's compensation terminology (e.g.,
     `["service fee", "asset-based"]`).
   - For `disclosure`: add firm-specific disclosure document names.

2. **May add an element** if the firm's product mix introduces a
   regulated factor not in the defaults. Examples:
   - For options recommendations: `options-disclosure` element with
     cues referencing the OCC OCD.
   - For variable annuities: `surrender-charge` element with cues for
     surrender period disclosure.

3. **Must not weaken detection thresholds.** An element is present if
   ANY cue matches; the firm cannot require multiple cues to match
   (that would create false negatives — gaps the auditor misses).

4. **Tailoring is locked at sign-off.** Once signed, the cue set and
   element list are locked until re-sign-off under
   `12-version-lock.md`.

---

## Testing the checklist

`10-monitoring-and-testing.md` describes the quarterly auditor-
effectiveness test. The firm's compliance testing should specifically
validate:

- False-negative rate: < 2%. (Notes the auditor passed but a manual
  reviewer scores incomplete.)
- False-positive rate: < 15%. (Notes the auditor flagged but a manual
  reviewer confirms complete.)

False-negative findings drive cue-phrase supplementation (and a
checklist version bump). False-positive findings drive training
(advisors writing in a style the cues don't match) or — if persistent —
also drive cue supplementation.

---

## What gets signed at CCO sign-off

The CCO signs:

1. The element list (above, plus any firm additions).
2. The cue phrase set for each element (defaults plus firm additions).
3. The detection logic for `date` (regex above).
4. The hardcoded `blocking: false` posture.
5. The no-override-log posture.

The signed version is **Exhibit B** to the executed
`11-sign-off-template.md`.
