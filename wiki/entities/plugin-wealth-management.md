---
title: Wealth Management Plugin
type: entity
domain: plugins
tags: [plugin, wm, advisory, planning]
sources:
  - wealth-management/.claude-plugin/plugin.json
  - wealth-management/skills/client-report/SKILL.md
  - wealth-management/skills/client-review/SKILL.md
  - wealth-management/skills/financial-plan/SKILL.md
  - wealth-management/skills/investment-proposal/SKILL.md
  - wealth-management/skills/portfolio-rebalance/SKILL.md
  - wealth-management/skills/tax-loss-harvesting/SKILL.md
updated: 2026-05-31
status: stable
---

# Wealth Management Plugin

Financial advisory tools — client reviews, financial planning, portfolio analysis, client reporting. Covers the advisor's full client workflow from prospect to ongoing review.

**Plugin path**: `wealth-management/`

## Skills (playbooks)
- [[client-report]] — quarterly/annual performance reports
- [[client-review]] — review meeting prep
- [[financial-plan]] — retirement + education + estate + cash flow planning
- [[investment-proposal]] — prospect-facing investment proposal
- [[portfolio-rebalance]] — drift analysis + tax-aware rebalancing trades
- [[tax-loss-harvesting]] — TLH opportunity scan with wash-sale tracking

## Commands
`/wm:client-report`, `/wm:client-review`, `/wm:financial-plan`, `/wm:proposal`, `/wm:rebalance`, `/wm:tlh`

## Related concepts
[[financial-plan-concept]] · [[tax-loss-harvesting-concept]] · [[portfolio-rebalance-concept]] · [[asset-allocation]] · [[wash-sale-rule]]

## See also
- [[plugins]] · [[finance]] · [[plugin-equity-research]] (idea source for proposals)
