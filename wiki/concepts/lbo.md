---
title: Leveraged Buyout (LBO)
type: concept
domain: finance
tags: [pe, lbo, modeling, returns]
sources:
  - financial-analysis/skills/lbo-model/SKILL.md
updated: 2026-05-31
status: stable
---

# Leveraged Buyout (LBO)

An LBO is an acquisition financed with significant debt, where the target's own cash flows service the debt. The sponsor (typically a PE firm) puts up equity for the gap between purchase price and debt capacity. Returns come from a combination of debt paydown, EBITDA growth, and multiple expansion.

## LBO returns equation (intuition)

Sponsor returns are driven by three levers:
1. **Debt paydown** — equity grows as debt amortizes
2. **EBITDA growth** — drives both cash for paydown and exit value
3. **Multiple expansion** (or contraction) — exit multiple vs entry multiple

Captured numerically as [[moic-irr]] on the sponsor's equity check over the hold period.

## Standard LBO model components

- **Sources & uses** — where the money comes from / where it goes at close
- **Debt schedule** — tranches, amortization, mandatory + sweep paydowns
- **Operating model** — typically a [[3-statement-model]] with focus on EBITDA and FCF
- **Returns waterfall** — IRR/MOIC at the equity level
- **Sensitivity** — entry multiple × exit multiple × leverage × hold period

## In this repo

- **Skill**: [[lbo-model]] (in [[plugin-financial-analysis]]) — completes LBO model templates
- **Related skill**: [[returns-analysis]] (in [[plugin-private-equity]]) — quick IRR/MOIC sensitivity tables
- **Related skill**: [[ic-memo]] — the LBO model feeds the IC memo
- **Related skill**: [[value-creation-plan]] — post-close operating improvements driving EBITDA growth

## Related concepts
- [[moic-irr]] · [[3-statement-model]] · [[dcf]] · [[merger-model]] (M&A counterpart)

## See also
- [[finance]] · [[plugin-private-equity]] · [[plugin-financial-analysis]]
