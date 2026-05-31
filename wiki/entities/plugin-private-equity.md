---
title: Private Equity Plugin
type: entity
domain: plugins
tags: [plugin, pe, buy-side, diligence, ic]
sources:
  - private-equity/.claude-plugin/plugin.json
  - private-equity/skills/dd-checklist/SKILL.md
  - private-equity/skills/dd-meeting-prep/SKILL.md
  - private-equity/skills/deal-screening/SKILL.md
  - private-equity/skills/deal-sourcing/SKILL.md
  - private-equity/skills/ic-memo/SKILL.md
  - private-equity/skills/portfolio-monitoring/SKILL.md
  - private-equity/skills/returns-analysis/SKILL.md
  - private-equity/skills/unit-economics/SKILL.md
  - private-equity/skills/value-creation-plan/SKILL.md
updated: 2026-05-31
status: stable
---

# Private Equity Plugin

PE deal sourcing through portfolio management — covers the full buy-side cycle: sourcing, screening, diligence, IC, monitoring, and value creation.

**Plugin path**: `private-equity/`

## Skills (playbooks)
- [[dd-checklist]] — sector-tailored due diligence checklists
- [[dd-meeting-prep]] — prep for management/expert/customer-reference meetings
- [[deal-screening]] — triage inbound CIMs/teasers against fund criteria
- [[deal-sourcing]] — discover targets, check CRM, draft founder outreach
- [[ic-memo]] — Investment Committee memo
- [[portfolio-monitoring]] — track portfolio company KPIs vs plan
- [[returns-analysis]] — IRR/MOIC sensitivity tables
- [[unit-economics]] — ARR cohorts, LTV/CAC, retention
- [[value-creation-plan]] — post-acquisition VCP + EBITDA bridge + 100-day plan

## Commands
`/pe:dd-checklist`, `/pe:dd-prep`, `/pe:ic-memo`, `/pe:portfolio`, `/pe:returns`, `/pe:screen-deal`, `/pe:source`, `/pe:unit-economics`, `/pe:value-creation`

## Related concepts
[[ic-memo-concept]] · [[due-diligence]] · [[moic-irr]] · [[unit-economics-concept]] · [[value-creation-plan-concept]] · [[lbo]]

## See also
- [[plugins]] · [[finance]] · [[plugin-investment-banking]] (sell-side counterpart) · [[plugin-financial-analysis]] (LBO models)
