# Arctic Edge — Platform Framework

Stage one of the AE platform: the framework and the module-wrapper pattern that
every Phase 1 module is built against. This document is the build contract —
each module below is implemented to the same wrapper shape so the terminal
(`ae_terminal.html`) can host them consistently.

## Architecture

Arctic Edge is, today, a single-file client terminal (`ae_terminal.html`) with
tabbed sections. Each Phase 1 module is a **wrapped unit** with four parts:

1. **Input contract** — the structured data the module consumes.
2. **Compute layer** — deterministic logic; no hidden scoring.
3. **Output artifact** — a standalone, reviewable result (PDF, worksheet, note).
4. **Terminal surface** — the tab/section that hosts it.

A module never reaches into another module's internals. Modules communicate
only through the shared data contracts in the next section.

## Shared data contracts

These are the interfaces every module reads from or writes to. They are fixed
early so modules can be built in parallel later.

- **IPS Record** — client objectives, constraints, asset-class targets,
  rebalancing rules, prohibited holdings, risk capacity. Produced by the IPS
  Module; consumed by Reg BI Note Generator, Note Completeness Auditor, Audit
  Trail, and the Phase 2 Suitability Bridge.
- **Four-Quadrant Risk** — four independent values: portfolio risk, valuation
  risk, behavioral risk, suitability overlay. Never collapsed into one score.
  Each quadrant is written by exactly one producer module.
- **Holdings Snapshot** — positions from custodian sync, used by Portfolio Risk
  Analyzer and Concentration X-Ray.
- **Recommendation Event** — origin (solicited/unsolicited), IPS context at the
  time, alternatives considered, rationale. Written by the Audit Trail.

## Phase 1 modules — build order

Order is dependency-driven, not roadmap-list order.

| # | Module | Depends on | Notes |
|---|--------|-----------|-------|
| 1 | IPS Module | — | Foundation. Build first. |
| 2 | Four-Quadrant Risk Framework | — | Data contract; lock early. |
| 3 | Portfolio Risk Analyzer | Holdings, market data | Feeds Quadrant 1. Math must be test-covered. |
| 4 | Trade Thesis Library | Security ref | Immutable timestamps. |
| 5 | Solicited/Unsolicited Audit Trail | IPS Module | High compliance value, low complexity. |
| 6 | Reg BI Note Generator | IPS Module | **Regulated — output templates need compliance review before live use.** |
| 7 | Note Completeness Auditor | Versioned Reg BI checklist | **Regulated.** Affirmative check, non-blocking, no override logs. |
| 8 | Equity Tearsheet Generator | Market data | Partially built (Research tab). Standard disclosure language only. |
| 9 | Concentration & Cross-Holdings X-Ray | Holdings, fund look-through | Surfaces true single-name/factor exposure. |
| 10 | Workstation | All of the above | The terminal itself; integrate last. |

## Module-wrapper template

Every module is documented and built to this shape:

```
Module: <name>
Terminal surface: <section id in ae_terminal.html>
Input contract: <data contract(s) consumed>
Compute: <deterministic logic summary>
Output artifact: <standalone reviewable result>
Compliance: <regulated? review requirement?>
Dependencies: <modules / data sources>
```

## Compliance posture

Modules 6 and 7 generate or audit regulatory work product (Reg BI, CFP
Standards of Conduct). Their logic and output templates must be reviewed by a
qualified compliance professional before any use on real client files. The
framework treats these as affirmative checks — they inform the advisor, they
never silently block or auto-file.

## Status

- [x] Framework and module-wrapper pattern defined
- [x] Module 1 — IPS Module (`modules/ips-module.html`)
- [x] Module 2 — Four-Quadrant Risk Framework (`modules/four-quadrant-risk.html`)
- [x] Module 3 — Portfolio Risk Analyzer (`modules/portfolio-risk-analyzer.html`)
- [x] Module 4 — Trade Thesis Library (`modules/trade-thesis-library.html`)
- [x] Module 5 — Solicited/Unsolicited Audit Trail (`modules/audit-trail.html`)
- [x] Module 6 — Reg BI Note Generator (`modules/reg-bi-note-generator.html`) — **regulated; needs compliance sign-off**
- [x] Module 7 — Note Completeness Auditor (`modules/note-completeness-auditor.html`) — **regulated; checklist needs compliance ownership**
- [x] Module 8 — Equity Tearsheet Generator (`modules/equity-tearsheet-generator.html`)
- [x] Module 9 — Concentration & Cross-Holdings X-Ray (`modules/concentration-xray.html`)
- [x] Module 10 — Workstation (`workstation.html`) — multi-tab shell hosting Modules 1–9

**Phase 1 — Section One complete.** All 10 modules built to the wrapper
contract. `workstation.html` is the integration surface. Remaining follow-on
work: (1) compliance sign-off on Modules 6–7, (2) wiring the market-data MCP
into Modules 3 and 8, (3) deeper embedding into the legacy `ae_terminal.html`.

> Modules 6 and 7 are functional drafts. Their output language, the
> `reg-bi-note/v1` template, and the `reg-bi-checklist/v1` element list must be
> reviewed and owned by a qualified compliance professional before any use on
> real client files. Module 7 is affirmative and non-blocking by design.

### Module 1 — IPS Module

- **Terminal surface:** `section-ips` (terminal integration is Module 10)
- **Input contract:** advisor entry
- **Compute:** validation + asset-class target consistency (bands, 100% sum)
- **Output artifact:** `ips-record/v1` JSON
- **Compliance:** not regulated work product; PII held client-side only
- **Dependencies:** none — this is the foundation
