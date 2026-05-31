---
title: Tax-Loss Harvesting (TLH)
type: concept
domain: finance
tags: [wm, tax, tlh, wash-sale, taxable-account]
sources:
  - wealth-management/skills/tax-loss-harvesting/SKILL.md
updated: 2026-05-31
status: stable
---

# Tax-Loss Harvesting (TLH)

A wealth-management technique: realize losses on depreciated positions in **taxable accounts** to offset realized gains and (up to limits) ordinary income, while maintaining target exposure by purchasing a non-substantially-identical replacement security.

## Core mechanics

1. **Identify candidates** — positions held at a loss in taxable accounts
2. **Validate** — confirm holding period (short-term vs long-term loss matters for offset hierarchy)
3. **Sell** — realize the loss
4. **Replace** — buy a similar-but-not-identical security to maintain market exposure
5. **Track wash-sale window** — 30 days before and after the sale; no repurchase of the same or substantially-identical security in that window or the loss is disallowed

## Wash-sale rule

The IRS disallows a loss if the same or substantially-identical security is purchased within **30 days before or after** the sale, in any account owned by the taxpayer or their spouse (including IRAs). Critical edge cases:
- Buying the same ETF in an IRA after selling at a loss in a taxable account → wash sale
- Buying a near-identical ETF (e.g., S&P 500 → Russell 1000) — gray area; conservative practice avoids it
- Reinvested dividends within the window can also trigger wash-sale

## Optimization

- Use loss to offset realized gains first (short-term losses → short-term gains, long-term → long-term)
- Excess losses offset up to $3,000 of ordinary income per year
- Remaining losses carry forward indefinitely

## In this repo

- **Skill**: [[tax-loss-harvesting]] (in [[plugin-wealth-management]])
- **Related skill**: [[portfolio-rebalance]] — rebalancing in taxable accounts should integrate TLH opportunities

## Related concepts
- [[wash-sale-rule]] · [[portfolio-rebalance-concept]] · [[asset-allocation]] · [[capital-gains]]

## See also
- [[finance]] · [[plugin-wealth-management]]
