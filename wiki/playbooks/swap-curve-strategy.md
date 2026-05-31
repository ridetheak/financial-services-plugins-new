---
title: Swap Curve Strategy
type: playbook
domain: finance
tags: [rates, swaps, curve-trades, dv01-neutral, lseg]
sources:
  - partner-built/lseg/skills/swap-curve-strategy/SKILL.md
updated: 2026-05-31
status: stable
---

# Swap Curve Strategy

**Plugin**: [[plugin-lseg]] (LSEG)
**Triggers**: swap curve analysis, swap spreads, real rate decomposition, steepener/flattener/butterfly trades, cross-currency swap rate comparison

Analyze the IRS curve by pricing swaps at multiple tenors, overlaying government and inflation curves, identifying curve trade opportunities. Curve metrics (2s10s, 5s30s, butterfly) and historical context drive trade ideas. Trade recommendations always include DV01-neutral sizing and carry/roll-down estimates.

**Key concepts**: [[swap-curve]] · [[yield-curve]] · [[dv01]] · [[macro-rates]] · [[breakevens]]
**Source**: `partner-built/lseg/skills/swap-curve-strategy/SKILL.md`
