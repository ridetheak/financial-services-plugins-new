---
title: S&P Global Plugin
type: entity
domain: plugins
tags: [plugin, partner-built, sp-global, kensho, tear-sheet, earnings]
sources:
  - partner-built/spglobal/.claude-plugin/plugin.json
  - partner-built/spglobal/skills/earnings-preview-beta/SKILL.md
  - partner-built/spglobal/skills/funding-digest/SKILL.md
  - partner-built/spglobal/skills/tear-sheet/SKILL.md
updated: 2026-05-31
status: stable
---

# S&P Global Plugin

Partner-built plugin from **S&P Global**. Financial data and analytics powered by S&P Capital IQ via the Kensho LLM-ready API MCP server. Includes the canonical [[tear-sheet-skill]] the user has explicitly highlighted as wiki-priority content.

**Plugin path**: `partner-built/spglobal/`  
**Vendor**: S&P Global  
**Data backbone**: S&P Capital IQ via Kensho MCP

## Skills (playbooks)
- [[tear-sheet-skill]] — audience-specific company tear sheets (equity research / IB / corp dev / sales-BD), output as Word docx with structured formatting (see [[tear-sheet]] concept for full spec)
- [[earnings-preview-beta]] — 4-5 page single-company earnings preview (HTML output, restricted to Kensho + Capital IQ data only)
- [[funding-digest]] — one-page PPT recap of weekly funding activity and capital markets deals

## Related concepts
[[tear-sheet]] (canonical) · [[earnings-preview-concept]] · [[funding-digest]] · [[capital-iq]] · [[kensho]]

## Tear sheet — special focus
This plugin's [[tear-sheet-skill]] is the wiki's reference implementation for the tear sheet artifact. The skill defines:
- Four audience templates (equity research / IB-M&A / corp dev / sales-BD)
- A precise visual style spec (navy header banner, two-column key-value layout, section rules, bullet conventions, table formatting)
- Style customization points (palette, font, disclaimer)

See [[tear-sheet]] for the distilled concept page.

## See also
- [[plugins]] · [[finance]] · [[plugin-lseg]] (other partner-built plugin)
