---
title: 3-Statement Financial Model
type: concept
domain: finance
tags: [modeling, income-statement, balance-sheet, cash-flow]
sources:
  - financial-analysis/skills/3-statements/SKILL.md
updated: 2026-05-31
status: stable
---

# 3-Statement Financial Model

The integrated **Income Statement**, **Balance Sheet**, and **Cash Flow Statement** model — the foundation of nearly every downstream financial analysis ([[dcf]], [[lbo]], [[merger-model]], [[returns-analysis]]).

## Linkages

The model is integrated when:
- **IS → BS**: net income flows to retained earnings
- **IS → CF**: net income is the top of CFO
- **BS changes → CF**: working capital, capex, debt issuance/paydown all reconcile
- **CF ending cash → BS**: cash on BS reconciles to ending cash on CF
- **BS must balance**: assets = liabilities + equity, every period

If BS doesn't balance, something is broken — [[check-model]] is the QC skill.

## In this repo

- **Skill**: [[3-statements]] (in [[plugin-financial-analysis]]) — completes 3-statement model templates with proper linkages
- **QC skill**: [[check-model]] — debug circulars, balance breaks, hardcoded overrides
- **Output example**: `outputs/apple_3_statement_model.xlsx`

## Related concepts
- [[dcf]] — DCF projections come from the 3-statement model's FCF
- [[lbo]] — LBO model is a 3-statement model with a debt schedule + returns waterfall
- [[merger-model]] — accretion/dilution sits on top of a 3-statement model for acquirer and target

## See also
- [[finance]] · [[plugin-financial-analysis]]
