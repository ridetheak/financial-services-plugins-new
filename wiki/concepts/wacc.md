---
title: Weighted Average Cost of Capital (WACC)
type: concept
domain: finance
tags: [valuation, cost-of-capital, discount-rate, dcf]
sources:
  - financial-analysis/skills/dcf-model/SKILL.md
updated: 2026-05-31
status: stable
---

# Weighted Average Cost of Capital (WACC)

The blended cost of a firm's financing — used as the discount rate in [[dcf]]. Combines after-tax cost of debt and cost of equity, weighted by capital structure.

## Formula

```
WACC = (E/V) × Re + (D/V) × Rd × (1 − T)
```

- `E/V`, `D/V` = market-value weights of equity and debt
- `Re` = cost of equity (typically CAPM: risk-free + β × equity risk premium)
- `Rd` = pre-tax cost of debt
- `T` = marginal tax rate (debt is tax-deductible, so multiply by `(1−T)`)

## Inputs and judgment calls

- **Risk-free rate**: 10Y Treasury yield (US), match-maturity to FCF horizon
- **Beta**: levered beta of comparable companies (delever → average → relever)
- **Equity risk premium**: typically 5-7% (US); Damodaran publishes country-by-country updates
- **Cost of debt**: yield on outstanding bonds or comparable issuers' yields
- **Capital structure weights**: target structure (not just current) is usually more appropriate

## In this repo

- **Used by**: [[dcf-model]] skill (in [[plugin-financial-analysis]]) — WACC sensitivity is a standard output

## Related concepts
- [[dcf]] · [[cost-of-equity]] · [[capm]] · [[capital-structure]]

## See also
- [[finance]] · [[plugin-financial-analysis]]
