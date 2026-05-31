---
title: Earnings Preview Beta (single-company)
type: playbook
domain: finance
tags: [equity-research, earnings-preview, sp-global, html, kensho]
sources:
  - partner-built/spglobal/skills/earnings-preview-beta/SKILL.md
  - partner-built/spglobal/skills/earnings-preview-beta/report-template.md
updated: 2026-05-31
status: stable
---

# Earnings Preview Beta (single-company)

**Plugin**: [[plugin-spglobal]] (S&P Global)
**Skill name**: `earnings-preview-single`
**Triggers**: single-company equity research earnings preview requests

Generate a concise 4-5 page equity research earnings preview for a single company. Analyzes the most recent earnings transcript, competitor landscape, valuation, and recent news. **Output is a self-contained HTML file** targeting 4-5 printed pages. Dense with figures and data, tight narrative.

**Strict data source constraint**: ONLY Kensho Grounding MCP (`search`) and S&P Global MCP (`kfinance`). NO WebSearch, WebFetch, browser, or any other web/internet tool — even if Kensho is slow or returns nothing.

**Reference template**: `partner-built/spglobal/skills/earnings-preview-beta/report-template.md`

**Key concepts**: [[earnings-preview-concept]] · [[kensho]] · [[capital-iq]] · [[earnings-preview]] (the Chinese sister skill)
**Source**: `partner-built/spglobal/skills/earnings-preview-beta/SKILL.md`
