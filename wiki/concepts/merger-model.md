---
title: Merger Model (Accretion / Dilution)
type: concept
domain: finance
tags: [m&a, modeling, accretion-dilution, pro-forma]
sources:
  - investment-banking/skills/merger-model/SKILL.md
updated: 2026-05-31
status: stable
---

# Merger Model (Accretion / Dilution)

A model that projects the **pro forma** financial impact of an M&A transaction on the acquirer. Answers: "after this deal, is the acquirer's EPS higher or lower than standalone?"

## Mechanics

1. **Standalone EPS** for acquirer and target
2. **Purchase price** and **consideration mix** (cash / stock / debt)
3. **Pro forma combined**:
   - Combined revenues and operating income
   - Plus expected **synergies** (revenue + cost)
   - Less new **interest expense** (debt financing)
   - Less **transaction costs**
   - Adjusted for **share issuance** (stock consideration)
4. **Pro forma EPS** = pro forma net income ÷ pro forma share count
5. **Accretion / dilution** = pro forma EPS vs standalone acquirer EPS

A deal is **accretive** if pro forma EPS > standalone, **dilutive** if lower.

## Key sensitivities

- Synergy assumptions (often the swing factor)
- Consideration mix (more stock = more dilution)
- Cost of debt for financing
- Purchase price / premium

## In this repo

- **Skill**: [[merger-model]] (in [[plugin-investment-banking]])
- **Often paired with**: [[pitch-deck]] (the model output drives the "deal impact" slide)
- **Sister model**: [[lbo]] (PE buy-side analog), [[dcf]] (intrinsic valuation that anchors the bid)

## Related concepts
- [[lbo]] · [[pitch-deck]] · [[cim]] · [[buyer-list-concept]] · [[synergies]]

## See also
- [[finance]] · [[plugin-investment-banking]] · [[plugin-financial-analysis]]
