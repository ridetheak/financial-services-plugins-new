---
title: MOIC and IRR (PE Returns Metrics)
type: concept
domain: finance
tags: [pe, returns, performance, moic, irr]
sources:
  - private-equity/skills/returns-analysis/SKILL.md
updated: 2026-05-31
status: stable
---

# MOIC and IRR

The two canonical PE return metrics. **MOIC** answers "how many times did we multiply our money?" **IRR** answers "what was the annualized return?"

## MOIC (Multiple on Invested Capital)

```
MOIC = total cash returned to LPs ÷ total cash invested
```

Also called "money multiple" or "cash-on-cash." A 3x MOIC means $1 invested returned $3 total.

- Includes both realized and unrealized value (DPI vs TVPI distinction)
- Ignores time — a 3x in 3 years vs 3x in 10 years look identical
- Easy to communicate, harder to compare across hold periods

## IRR (Internal Rate of Return)

The discount rate at which the NPV of cash flows = 0. The time-adjusted return.

- Penalizes long hold periods, rewards early distributions
- Heavily influenced by timing (a quick partial sale can spike IRR)
- Standard target: 20%+ gross, ~15% net for buyout funds
- Can be misleading when there are very small early inflows or very late outflows

## Why both

PE funds report both because each tells half the story. A short hold can produce high IRR but low MOIC; a long hold can produce high MOIC but middling IRR. Investment Committees want to see the deal across the MOIC × IRR plane.

## In this repo

- **Skill**: [[returns-analysis]] (in [[plugin-private-equity]]) — IRR/MOIC sensitivity tables across entry × leverage × exit × growth × hold
- **Used by**: [[ic-memo]], [[lbo-model]]

## Related concepts
- [[lbo]] · [[ic-memo-concept]] · [[hold-period]] · [[dpi-tvpi]]

## See also
- [[finance]] · [[plugin-private-equity]]
