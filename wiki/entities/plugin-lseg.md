---
title: LSEG Plugin
type: entity
domain: plugins
tags: [plugin, partner-built, lseg, fixed-income, rates, fx, derivatives]
sources:
  - partner-built/lseg/.claude-plugin/plugin.json
  - partner-built/lseg/skills/bond-futures-basis/SKILL.md
  - partner-built/lseg/skills/bond-relative-value/SKILL.md
  - partner-built/lseg/skills/equity-research/SKILL.md
  - partner-built/lseg/skills/fixed-income-portfolio/SKILL.md
  - partner-built/lseg/skills/fx-carry-trade/SKILL.md
  - partner-built/lseg/skills/macro-rates-monitor/SKILL.md
  - partner-built/lseg/skills/option-vol-analysis/SKILL.md
  - partner-built/lseg/skills/swap-curve-strategy/SKILL.md
updated: 2026-05-31
status: stable
---

# LSEG Plugin

Partner-built plugin from **LSEG** (London Stock Exchange Group). Bond pricing, yield curves, FX carry, options vol, fixed income portfolio analytics, and macro/rates dashboards. Pattern: route MCP tool outputs into structured analyses (let the tools compute, the skill interprets).

**Plugin path**: `partner-built/lseg/`  
**Vendor**: LSEG

## Skills (playbooks)
- [[bond-futures-basis]] — basis trading, CTD identification, implied repo
- [[bond-relative-value]] — spread decomposition (risk-free / credit / residual)
- [[lseg-equity-research]] — IBES consensus + fundamentals snapshots (distinct from the [[plugin-equity-research]] internal plugin)
- [[fixed-income-portfolio]] — portfolio DV01, duration, cashflow waterfalls
- [[fx-carry-trade]] — carry-to-vol, forward curve, optimal tenor
- [[macro-rates-monitor]] — yield curves, breakevens, swap rates, financial conditions
- [[option-vol-analysis]] — vol surface, implied vs realized, Greeks
- [[swap-curve-strategy]] — curve shape, swap spreads, steepener/flattener/butterfly trades

## Related concepts
[[yield-curve]] · [[fx-carry]] · [[bond-futures-basis-concept]] · [[swap-curve]] · [[option-vol]] · [[fixed-income-portfolio-concept]] · [[macro-rates]]

## See also
- [[plugins]] · [[finance]] · [[plugin-spglobal]] (other partner-built plugin)
