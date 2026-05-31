---
title: Investment Banking Plugin
type: entity
domain: plugins
tags: [plugin, ib, m&a, sell-side]
sources:
  - investment-banking/.claude-plugin/plugin.json
  - investment-banking/skills/buyer-list/SKILL.md
  - investment-banking/skills/cim-builder/SKILL.md
  - investment-banking/skills/datapack-builder/SKILL.md
  - investment-banking/skills/deal-tracker/SKILL.md
  - investment-banking/skills/merger-model/SKILL.md
  - investment-banking/skills/pitch-deck/SKILL.md
  - investment-banking/skills/process-letter/SKILL.md
  - investment-banking/skills/strip-profile/SKILL.md
  - investment-banking/skills/teaser/SKILL.md
updated: 2026-05-31
status: stable
---

# Investment Banking Plugin

Investment banking productivity tools — client/market insights, deck creation, financial analysis, and transaction management. Focused on sell-side M&A workflow.

**Plugin path**: `investment-banking/`

## Skills (playbooks)
- [[buyer-list]] — universe of potential acquirers for sell-side
- [[cim-builder]] — draft Confidential Information Memorandum
- [[datapack-builder]] — standardized Excel data packs from CIMs / SEC filings
- [[deal-tracker]] — live deal pipeline + milestones
- [[merger-model]] — accretion / dilution for M&A
- [[pitch-deck]] — populate IB pitch deck templates from source data
- [[process-letter]] — process letters, IOI instructions, final-bid letters
- [[strip-profile]] — 1-4 slide company profiles for pitch books
- [[teaser]] — anonymous one-page sell-side teaser

## Commands
`/ib:buyer-list`, `/ib:cim`, `/ib:deal-tracker`, `/ib:merger-model`, `/ib:one-pager`, `/ib:process-letter`, `/ib:teaser`

## Related concepts
[[cim]] · [[teaser]] · [[merger-model]] · [[pitch-deck]] · [[buyer-list-concept]] · [[sell-side-process]]

## See also
- [[plugins]] · [[finance]] · [[plugin-financial-analysis]] (modeling complement) · [[plugin-private-equity]] (buy-side counterpart)
