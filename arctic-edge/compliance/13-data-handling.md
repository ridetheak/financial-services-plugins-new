# Data Handling

**Audience:** CCO, General Counsel, CISO, Head of IT.
**Purpose:** Where data lives, where it moves, and how Arctic Edge fits the
firm's existing Reg S-P, GLBA Safeguards Rule, and (if applicable) NY DFS
Part 500 cybersecurity program.

---

## Position

Arctic Edge does not transmit client PII to any third-party service through
its own operation. All client-side persistence in Phase 1 is browser
localStorage. Market data ingress and firm-side recordkeeping integration
are the firm's existing infrastructure, operating under the firm's existing
security program. The firm assesses Arctic Edge as a service provider under
the firm's vendor-management framework (Reg S-P § 248.30(b); NY DFS
§ 500.11).

---

## Data inventory

### Data Arctic Edge handles

| Data | Source | Stored | Transmitted to | PII level |
|---|---|---|---|---|
| Client identification (`clientRef`) | Advisor entry | localStorage | Firm records system on export | Low (ID or initials by default) |
| Client investment profile (IPS) | Advisor entry | localStorage | Firm records system on export | Medium (objectives, risk capacity, constraints) |
| Holdings | Custodian feed or manual | localStorage | None during use; firm system on export | Low–Medium (positions, no balances) |
| Market data | OpenBB MCP, Schwab websocket, or firm data feed | Transient (computation only) | None | None |
| Trade thesis | Advisor entry | localStorage | Firm records system on export | None (security analysis) |
| Recommendation event | Advisor entry | localStorage | Firm records system on export | Medium (links to client) |
| Reg BI note | Module 6 output | localStorage | Firm records system on export | Medium (links to client) |
| Note audit | Module 7 output | localStorage | Firm records system on export | None (heuristic result) |
| Portfolio risk | Module 3 output | localStorage | Firm records system on export | Low (composite metrics) |
| Concentration X-Ray | Module 9 output | localStorage | Firm records system on export | Low (composite exposures) |
| Equity tearsheet | Module 8 output | localStorage | Firm records system on export (if exported) | None (security data only) |

**Notes:**

1. "Stored" = where Arctic Edge writes the data. localStorage is per-
   browser, per-origin, per-user — not shared across machines.
2. "Transmitted" = where Arctic Edge causes the data to move. Arctic Edge
   does not initiate any third-party transmission of client data.
3. The firm's recordkeeping export pipeline is firm-controlled
   infrastructure and operates under the firm's existing security
   posture.

### Data Arctic Edge does NOT handle

- **Account numbers** — not required by any module.
- **Tax IDs / Social Security numbers** — not required by any module.
- **Bank routing or account information** — not required by any module.
- **Full client name in note body** — the template default uses
  `clientRef`. Firms whose policy requires full name in the body should
  configure the template at sign-off, with the data-handling
  implications considered.

---

## Data flow diagram

```
   ┌──────────────────────┐                          ┌────────────────────────┐
   │ Advisor workstation  │ ◄─── Market data ───────┤ Market data source     │
   │ (Arctic Edge HTML)   │      (security data;    │ (OpenBB / Schwab /     │
   │                      │       no client PII)    │  firm feed)            │
   │  ┌─────────────────┐ │                          └────────────────────────┘
   │  │ localStorage    │ │
   │  │ (client data)   │ │ ─── JSON export ────►   ┌────────────────────────┐
   │  └─────────────────┘ │                          │ Firm records system    │
   └──────────────────────┘                          │ (17a-4 / 4511 store)   │
                                                     └────────────────────────┘
```

Data path from market data source to advisor workstation: security
data only; no client PII flows in this direction.

Data path from advisor workstation to firm records: standard
JSON export; firm-controlled.

There is no path from advisor workstation to any Arctic Edge–operated
server with client data.

---

## Reg S-P / Safeguards Rule fit

Regulation S-P (17 CFR § 248.30) requires written policies and
procedures addressing safeguards for customer records. The firm's
existing Reg S-P policy covers:

- Administrative safeguards (training, access control).
- Technical safeguards (encryption, authentication).
- Physical safeguards (workstation security, paper records).

**Where Arctic Edge fits:**

- **Administrative:** Advisor training on Arctic Edge use is covered in
  `09-training-curriculum.md`. Sign-on access is governed by the firm's
  existing SSO posture.
- **Technical:** Arctic Edge runs in the browser. The firm's existing
  endpoint security (browser sandboxing, OS encryption, data-loss
  prevention) covers Arctic Edge as it covers any browser-based tool.
- **Physical:** Same as the firm's existing workstation security.

**What the firm should confirm before deployment:**

- Workstations running Arctic Edge are firm-managed (managed endpoint,
  full-disk encryption, screen lock, device wipe on loss).
- localStorage is included in the firm's data-loss-prevention scope.
- Off-firm-network use of Arctic Edge (advisor's home machine) is
  consistent with the firm's remote-work policy.

---

## NY DFS Part 500 fit

For firms regulated by NY DFS or whose practice extends to NY clients,
23 NYCRR Part 500 applies.

| Part 500 Section | Requirement | Arctic Edge posture |
|---|---|---|
| § 500.02 | Cybersecurity Program | Inherits firm's program; no separate program required |
| § 500.03 | Cybersecurity Policy | Reference Arctic Edge in firm's policy |
| § 500.04 | CISO | Firm CISO reviews per § 500.11 |
| § 500.05 | Penetration Testing | Firm's existing program; Arctic Edge is a single-file HTML asset, no separate pen-test domain |
| § 500.06 | Audit Trail | Firm's existing program; Arctic Edge artifacts are audit-trail inputs |
| § 500.07 | Access Privileges | Firm SSO governs |
| § 500.09 | Risk Assessment | Firm includes Arctic Edge in periodic assessment |
| § 500.11 | Third-Party Service Provider | **See vendor assessment below** |
| § 500.13 | Limitations on Data Retention | Firm's records-retention policy applies |
| § 500.14 | Training & Monitoring | Firm's existing training; Arctic Edge added to curriculum per doc 09 |
| § 500.15 | Encryption | localStorage encrypted at rest if OS / browser enforces; in-transit encryption depends on deployment (firm-hosted vs. vendor URL) |
| § 500.16 | Incident Response | Firm's existing IR plan applies; see doc 14 |

### § 500.11 Vendor Assessment Checklist

For Arctic Edge as a third-party service provider (or as
firm-hosted software):

- ☐ **Identify the third party.** If Arctic Edge is firm-deployed
  from source, the "vendor" is the firm itself. If deployed from a
  vendor URL, identify the vendor.
- ☐ **Risk assessment.** What is the data Arctic Edge handles? See
  inventory above.
- ☐ **Minimum security practices.** Document expected practices in the
  vendor contract (or for firm-deployed: in the firm's policies).
- ☐ **Periodic reassessment.** Annual.
- ☐ **Incident notification.** Define who notifies whom in an incident.

---

## GLBA Safeguards Rule (FTC version)

If the firm is subject to the FTC Safeguards Rule (16 CFR Part 314) —
e.g., an RIA that is also a tax-prep firm — the same posture as Reg S-P
applies, plus the 2021 amendments' additional requirements:

- Qualified individual to oversee the information security program.
- Risk assessment in writing.
- Access controls.
- Encryption of customer information at rest and in transit.
- Multi-factor authentication.
- Periodic testing.

Arctic Edge does not change the firm's obligations; the firm's existing
Safeguards program absorbs Arctic Edge as another tool.

---

## Cross-border considerations

If the firm has clients or operations outside the U.S. — particularly
EU/UK (GDPR), Canada (PIPEDA), or California (CCPA) — additional
considerations may apply. These are firm-by-firm and outside the scope
of this generic package. The firm's GC determines fit.

---

## Operational recommendations

1. **Deploy Arctic Edge from firm infrastructure.** Hosting the
   workstation HTML on a firm-controlled URL (intranet or internal
   web app) is operationally cleanest. Vendor hosting introduces a
   § 500.11 vendor relationship.

2. **Enforce SSO.** Browser-based workstation access should require
   firm SSO. Local file:// access should be disabled in firm policy.

3. **Clear localStorage on logout.** Firm policy or browser extension
   to clear localStorage on session end reduces residual PII on the
   endpoint.

4. **Encrypted endpoints.** Full-disk encryption on every workstation
   that runs Arctic Edge. Standard practice; restated here because
   localStorage data inherits endpoint-level protections.

5. **Export to firm records on completion.** The advisor's workflow
   ends with export of finalized artifacts to the firm's records
   system. Don't leave records in localStorage long-term.

6. **Vendor management documentation.** If deploying Arctic Edge from
   any vendor-hosted URL, complete the § 500.11 / Safeguards vendor
   checklist before go-live.
