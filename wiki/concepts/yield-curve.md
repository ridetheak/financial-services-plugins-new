---
title: Yield Curve
type: concept
domain: finance
tags: [fixed-income, rates, curve, macro, swap-curve]
sources:
  - partner-built/lseg/skills/swap-curve-strategy/SKILL.md
  - partner-built/lseg/skills/macro-rates-monitor/SKILL.md
  - partner-built/lseg/skills/bond-relative-value/SKILL.md
updated: 2026-05-31
status: stable
---

# Yield Curve

A plot of yield against maturity for a given issuer (or curve type). The shape encodes the market's expectations for future short-term rates, inflation, credit, and term premium.

## Curve types in this repo

- **Government / Treasury curve** — risk-free, sovereign issuer
- **Swap curve** — fixed-vs-floating IRS rates at each tenor; bank credit (LIBOR/SOFR-based)
- **Inflation breakeven curve** — nominal − real (TIPS), implies expected inflation
- **Real-rate curve** — TIPS yields, isolates the real return
- **Credit curves** — corporate IG / HY at various tenors and ratings

## Key shapes

- **Normal / upward** — long > short; typical for growth + positive term premium
- **Inverted** — short > long; classic recession signal
- **Flat** — convergence; transition phase or policy uncertainty
- **Steepening / flattening** — directional curve trades

## Common metrics

- **2s10s slope** = 10Y yield − 2Y yield (recession indicator)
- **5s30s slope** — long-end steepness
- **Butterfly** = (2 × belly) − (front + back) — curvature trade
- **DV01-neutral sizing** — required for curve trades

## In this repo

- **Skills**: [[swap-curve-strategy]], [[macro-rates-monitor]], [[bond-relative-value]] (all in [[plugin-lseg]])
- **Related skill**: [[fixed-income-portfolio]] — uses curves for duration positioning

## Related concepts
- [[swap-curve]] · [[bond-futures-basis-concept]] · [[macro-rates]] · [[dv01]] · [[duration]]

## See also
- [[finance]] · [[plugin-lseg]]
