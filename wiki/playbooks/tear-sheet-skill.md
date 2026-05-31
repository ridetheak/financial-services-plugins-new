---
title: Tear Sheet (skill)
type: playbook
domain: finance
tags: [tear-sheet, company-profile, sp-global, kensho, capital-iq, docx]
sources:
  - partner-built/spglobal/skills/tear-sheet/SKILL.md
updated: 2026-05-31
status: stable
---

# Tear Sheet (skill)

**Plugin**: [[plugin-spglobal]] (S&P Global)
**Triggers**: "tear sheet", "company one-pager", "company profile", "fact sheet", "company snapshot", "company overview document", equity research summaries, M&A company profiles, corp dev target profiles, sales/BD meeting prep documents, any concise single-company financial summary

Generate audience-specific company tear sheets using S&P Capital IQ data via the Kensho LLM-ready API MCP server. Output: professional Word document (.docx).

**Four audience templates**:
- Equity research
- Investment banking / M&A
- Corporate development
- Sales / business development

If audience is unspecified, the skill asks. Works for both public and private companies.

For the full concept page covering style spec, structure, and design intent see **[[tear-sheet]]** (the concept page is the canonical reference; this playbook is the skill entry point).

**Key concepts**: [[tear-sheet]] (concept) · [[strip-profile]] · [[kensho]] · [[capital-iq]] · [[plugin-spglobal]]
**Source**: `partner-built/spglobal/skills/tear-sheet/SKILL.md`
