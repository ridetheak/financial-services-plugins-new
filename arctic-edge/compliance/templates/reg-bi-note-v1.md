# Template — Reg BI Note (`reg-bi-note/v1`)

**Status:** Generic template. Firms tailor before CCO sign-off.
**Regulated:** YES. Subject to `11-sign-off-template.md` Exhibit A.

This is the structure of a Reg BI trade note as produced by Module 6.
Each field is specified with: name, purpose, required, format, audit
cue phrases (for `reg-bi-checklist/v1`), and tailoring guidance.

The producer module (`modules/reg-bi-note-generator.html`) enforces:

- Required fields must be populated to generate the note.
- Conflict field cannot be empty (an explicit "none identified"
  selection is required).
- Output status is `draft-pending-compliance-review` until firm process
  marks principal-reviewed.
- Output carries the template version tag.

---

## JSON shape

```json
{
  "contract": "reg-bi-note/v1",
  "noteId": "ae-rbn-2026-05-28-001",
  "status": "draft-pending-compliance-review",
  "createdAt": "2026-05-28T10:30:00-08:00",
  "advisorId": "ADV-12345",
  "clientRef": "C-7821",
  "ipsRecordId": "ips-2026-01-15-7821",
  "recommendationEventId": "evt-2026-05-28-7821-001",
  "tradeThesisId": "thesis-2026-05-27-7821-MSFT",

  "recommendation": {
    "action": "buy",
    "security": "MSFT",
    "quantity": 100,
    "notional": 40000.00,
    "accountType": "IRA"
  },

  "clientProfile": {
    "objective": "long-term growth with moderate risk",
    "timeHorizon": "9 years to retirement target",
    "riskTolerance": "moderate",
    "riskCapacity": "moderate",
    "ipsReference": "ips-2026-01-15-7821"
  },

  "careBasis": "...",
  "alternatives": [
    { "security": "GOOGL", "rejectedReason": "..." },
    { "security": "XLK", "rejectedReason": "..." }
  ],
  "costs": {
    "expenseRatio": null,
    "commission": 0.00,
    "twelveB1": null,
    "totalCostBps": 0,
    "costConsideration": "..."
  },
  "conflicts": {
    "identified": ["..."],
    "noneIdentified": false,
    "mitigation": "..."
  },
  "disclosure": {
    "formCRS": { "delivered": true, "deliveredAt": "2026-01-15" },
    "feeSchedule": { "delivered": true, "deliveredAt": "2026-01-15" },
    "prospectus": null
  },
  "attestation": {
    "advisorName": "[name on file]",
    "signedAt": "2026-05-28T10:30:00-08:00",
    "text": "..."
  },

  "templateVersion": "reg-bi-note/v1",
  "tailoringHash": "<sha256 of firm-tailored exhibit>"
}
```

---

## Fields

### 1. `recommendation`

**Purpose:** Identifies the specific action and security.
**Required:** Yes.
**Format:** action (buy / sell / hold / add / trim / reallocate), security
identifier, quantity or notional, account type.
**Audit cue:** Any of: "recommend", "buy", "sell", "hold", "add to",
"trim", "position".

### 2. `clientProfile`

**Purpose:** Customer-specific suitability anchor (Reg BI Care
Obligation, 15l-1(a)(2)(ii)(B)).
**Required:** Yes.
**Format:** Reference to active `ips-record/v1` by ID. Summary fields
populated from the IPS for display.
**Audit cue:** Any of: "objective", "risk tolerance", "risk capacity",
"time horizon", "investment profile".

### 3. `careBasis`

**Purpose:** The reasonable-basis statement — why this recommendation
is in the client's best interest given the profile and the alternatives.
**Required:** Yes.
**Format:** Free text, minimum 100 characters (configurable).
**Audit cue:** Any of: "best interest", "basis for", "fits the",
"care obligation", "suitable".

**Tailoring note:** Firms may pre-populate with a structured starter
("This recommendation is in the client's best interest because…")
that the advisor completes. Pre-populated starter text alone is not
sufficient; the advisor's reasoning is required.

### 4. `alternatives`

**Purpose:** Reasonably available alternatives considered. Required
under Reg BI Care Obligation — this is new vs. FINRA 2111.
**Required:** Yes (must include at least one alternative, OR an explicit
note that the transaction was unsolicited and tied to a specific client
direction — in which case the `recommendation-event/v1` origin must be
`unsolicited`).
**Format:** Array of `{ security, rejectedReason }`. Free text reason.
**Audit cue:** Any of: "alternative", "other options", "considered",
"reasonably available".

**Tailoring note:** Firms with a defined product menu may populate a
picker. The picker is a convenience; the advisor still selects.

### 5. `costs`

**Purpose:** Cost consideration. Required under Reg BI Care Obligation.
**Required:** Yes. At minimum, the relevant cost type for the product
must be populated (commission for a stock, expense ratio + 12b-1 for a
mutual fund, etc.).
**Format:** Structured numeric where known; `costConsideration` free
text explains the cost frame.
**Audit cue:** Any of: "cost", "fee", "expense", "expense ratio",
"commission".

### 6. `conflicts`

**Purpose:** Conflict of interest. Reg BI Conflict Obligation
(15l-1(a)(2)(iii)) and Adviser Act duty of loyalty.
**Required:** Yes. The field **cannot be empty**. Either:
- `identified` array is non-empty, OR
- `noneIdentified` is explicitly `true`.

The advisor cannot leave the field blank. "None identified" is an
explicit affirmative choice.
**Format:** Structured.
**Audit cue:** Any of: "conflict", "no conflict", "none identified",
"compensation".

**Tailoring note:** This field benefits the most from firm tailoring.
The firm's GC and CCO should enumerate the firm's known conflict
types as a picker:
- Share-class selection (where applicable).
- 12b-1 fees (where applicable).
- Revenue sharing.
- Proprietary product.
- Rep compensation by product type.
- Solicitor / referral arrangements.

The picker reduces the chance of an advisor honestly missing a
conflict that the firm knows about.

### 7. `disclosure`

**Purpose:** Reg BI Disclosure Obligation (15l-1(a)(2)(i)) — material
facts disclosed to the client.
**Required:** Yes.
**Format:** Structured booleans for the firm's disclosure stack (Form
CRS, fee schedule, prospectus, etc.), each with a delivery date.
**Audit cue:** Any of: "disclos", "form crs", "fee schedule",
"prospectus".

**Tailoring note:** Firm-specific. List the firm's standard disclosure
stack.

### 8. `attestation`

**Purpose:** Advisor's electronic attestation that the note accurately
reflects the recommendation. Operational integrity.
**Required:** Yes.
**Format:** Advisor name (from session), signed timestamp, attestation
text (locked at sign-off).
**Audit cue:** Date detection (regex on the note body).

**Tailoring note:** The attestation text is a firm policy choice.
Common text:

> I attest that this note accurately reflects the recommendation made
> to the client, the basis for the recommendation, the reasonably
> available alternatives considered, the costs evaluated, the conflicts
> identified or affirmatively determined to be absent, and the
> disclosures provided. The recommendation has been or will be reviewed
> by a registered principal in accordance with the firm's supervisory
> procedures.

---

## What gets signed at CCO sign-off

The CCO signs:

1. The field list (above).
2. The required / optional / cardinality rules.
3. The default text for any pre-populated fields (e.g., the
   `careBasis` starter, the attestation text).
4. The firm-tailored picker contents (conflicts, alternatives,
   disclosure stack).
5. The cue-phrase list for `reg-bi-checklist/v1` (which references
   this template).

The signed version is **Exhibit A** to the executed
`11-sign-off-template.md`. Until that exists, the template above is
generic and is not eligible for production use.
