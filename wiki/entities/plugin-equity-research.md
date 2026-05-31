---
title: Equity Research Plugin
type: entity
domain: plugins
tags: [plugin, equity-research, sell-side-research, buy-side-research]
sources:
 - equity-research/.claude-plugin/plugin.json
 - equity-research/skills/catalyst-calendar/SKILL.md
 - equity-research/skills/earnings-analysis/SKILL.md
 - equity-research/skills/earnings-preview/SKILL.md
 - equity-research/skills/idea-generation/SKILL.md
 - equity-research/skills/initiating-coverage/SKILL.md
 - equity-research/skills/model-update/SKILL.md
 - equity-research/skills/morning-note/SKILL.md
 - equity-research/skills/sector-overview/SKILL.md
 - equity-research/skills/thesis-tracker/SKILL.md
updated: 2026-05-31
status: stable
---

# Equity Research Plugin

Equity research workflows — earnings analysis, initiating coverage reports, morning notes, thesis tracking, and the daily research cadence.

**Plugin path**: `equity-research/`

## Skills (playbooks)
- [[catalyst-calendar]] — earnings dates, conferences, regulatory events
- [[earnings-analysis]] — 8-12 page post-earnings update reports
- [[earnings-preview]] — pre-earnings bull/bear scenario notes
- [[idea-generation]] — stock screening + idea sourcing
- [[initiating-coverage]] — institutional-quality initiation reports (5-task workflow)
- [[model-update]] — refresh financial models with new data
- [[morning-note]] — 7am meeting briefings
- [[sector-overview]] — industry / sector landscape reports
- [[thesis-tracker]] — maintain investment theses per position

## Commands
`/er:catalysts`, `/er:earnings`, `/er:earnings-preview`, `/er:initiate`, `/er:model-update`, `/er:morning-note`, `/er:screen`, `/er:sector`, `/er:thesis`

## Related concepts
[[morning-note-concept]] · [[earnings-preview-concept]] · [[initiating-coverage-concept]] · [[catalyst]] · [[investment-thesis]]

## See also
- [[plugins]] · [[finance]] · [[plugin-financial-analysis]] (shared modeling) · [[plugin-lseg]] (vendor-built equity-research counterpart)
