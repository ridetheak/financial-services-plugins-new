---
title: FX Carry Trade
type: concept
domain: finance
tags: [fx, carry, rates-differential, volatility, lseg]
sources:
  - partner-built/lseg/skills/fx-carry-trade/SKILL.md
updated: 2026-05-31
status: stable
---

# FX Carry Trade

A position that earns the **interest rate differential** between two currencies by borrowing the lower-yielding ("funding") currency and investing in the higher-yielding ("target") currency. Profitable in stable / low-vol environments; vulnerable to spot moves and vol spikes.

## Mechanics

- Carry income comes from the rate differential, paid via forward points or actual rate accrual
- The trade is **short volatility** by nature — rising vol historically correlates with carry-trade unwinds
- Common funding currencies historically: JPY, CHF, more recently CNH; common target currencies: AUD, NZD, BRL, MXN, INR

## Key metric: Carry-to-vol ratio

```
Carry-to-vol = annualized carry ÷ ATM implied vol
```

Measures **risk-adjusted attractiveness**. Higher = better risk-adjusted carry. Compared across tenors and pairs to find optimal positioning.

## Workflow (from LSEG skill)

1. Pull spot rates, forward curves, rate differentials
2. Map full forward curve to find optimal tenor
3. Overlay vol surface for risk assessment
4. Check historical spot trends for directional context
5. Compute carry-to-vol per candidate pair
6. Recommend pair + tenor + position size

## In this repo

- **Skill**: [[fx-carry-trade]] (in [[plugin-lseg]])

## Related concepts
- [[option-vol]] · [[forward-curve]] · [[interest-rate-parity]] · [[volatility-surface]]

## See also
- [[finance]] · [[plugin-lseg]]
