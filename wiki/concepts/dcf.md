---
title: Discounted Cash Flow (DCF)
type: concept
domain: finance
tags: [valuation, modeling, dcf, intrinsic-value]
sources:
  - financial-analysis/skills/dcf-model/SKILL.md
updated: 2026-05-31
status: stable
---

# Discounted Cash Flow (DCF)

DCF values a company as the present value of its expected future free cash flows, discounted at a rate reflecting the riskiness of those cash flows ([[wacc]]). The canonical intrinsic-value method.

## Core mechanics

1. **Project free cash flow** (typically 5-10 years explicit forecast)
2. **Discount each year's FCF** at [[wacc]]
3. **Compute terminal value** (perpetuity growth or exit multiple)
4. **Sum**: enterprise value = sum of discounted FCFs + discounted terminal value
5. **Bridge to equity value**: EV − net debt − minority interest + cash = equity value
6. **Per-share value**: equity value ÷ diluted shares outstanding

## Sensitivity

DCF outputs are extremely sensitive to WACC and terminal growth/exit multiple. A sensitivity table on those two axes is standard practice and is built into the [[dcf-model]] skill output.

## In this repo

- **Skill**: [[dcf-model]] (in [[plugin-financial-analysis]]) — builds institutional-grade DCF in Excel from SEC filings + analyst reports
- **Used by**: [[plugin-equity-research]] ([[initiating-coverage]]), [[plugin-investment-banking]] ([[pitch-deck]]), [[plugin-private-equity]] (target valuation)

## Related concepts
- [[wacc]] — the discount rate
- [[3-statement-model]] — the underlying financial model FCF projections come from
- [[comps-analysis-concept]] — relative-value complement to DCF's absolute valuation

## See also
- [[finance]] · [[plugin-financial-analysis]]
