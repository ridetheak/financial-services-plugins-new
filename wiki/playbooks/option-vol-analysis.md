---
title: Option Vol Analysis
type: playbook
domain: finance
tags: [derivatives, options, vol-surface, greeks, lseg]
sources:
  - partner-built/lseg/skills/option-vol-analysis/SKILL.md
updated: 2026-05-31
status: stable
---

# Option Vol Analysis

**Plugin**: [[plugin-lseg]] (LSEG)
**Triggers**: option pricing, vol surface analysis, Greeks computation, vol premiums, vol trading strategies

Analyze option volatility by combining vol surface data, option pricing with Greeks, and historical price data to assess implied vs realized volatility. Always start from the vol surface — it encodes market expectations across strikes and expiries. The **vol premium** (implied minus realized) is the key metric for option richness/cheapness.

**Key concepts**: [[option-vol]] · [[volatility-surface]] · [[greeks]] · [[fx-carry]]
**Source**: `partner-built/lseg/skills/option-vol-analysis/SKILL.md`
