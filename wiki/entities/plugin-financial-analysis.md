---
title: Financial Analysis Plugin
type: entity
domain: plugins
tags: [plugin, modeling, valuation, qc]
sources:
  - financial-analysis/.claude-plugin/plugin.json
  - financial-analysis/skills/3-statements/SKILL.md
  - financial-analysis/skills/check-deck/SKILL.md
  - financial-analysis/skills/check-model/SKILL.md
  - financial-analysis/skills/competitive-analysis/SKILL.md
  - financial-analysis/skills/comps-analysis/SKILL.md
  - financial-analysis/skills/dcf-model/SKILL.md
  - financial-analysis/skills/lbo-model/SKILL.md
  - financial-analysis/skills/ppt-template-creator/SKILL.md
  - financial-analysis/skills/skill-creator/SKILL.md
updated: 2026-05-31
status: stable
---

# Financial Analysis Plugin

Core financial modeling and analysis — DCF, comps, LBO, 3-statement models, competitive analysis, and presentation QC. The shared modeling toolkit used across IB, ER, and PE workflows.

**Plugin path**: `financial-analysis/`

## Skills (playbooks)
- [[3-statements]] — populate 3-statement model templates (IS/BS/CF)
- [[check-deck]] — QC IB presentations across 4 dimensions
- [[check-model]] — debug financial models (circulars, balance breaks, etc.)
- [[competitive-analysis]] — competitive landscape framework
- [[comps-analysis]] — comparable company analysis (multiples + benchmarking)
- [[dcf-model]] — institutional DCF with WACC + sensitivity
- [[lbo-model]] — LBO model template completion for PE deals
- [[ppt-template-creator]] — **meta-skill**: turns PPT templates into reusable skills
- [[skill-creator]] — **meta-skill**: guide for creating new skills

## Commands
`/fa:3-statements`, `/fa:check-deck`, `/fa:competitive-analysis`, `/fa:comps`, `/fa:dcf`, `/fa:debug-model`, `/fa:lbo`, `/fa:ppt-template`

## Related concepts
[[dcf]] · [[lbo]] · [[comps-analysis-concept]] · [[3-statement-model]] · [[wacc]] · [[merger-model]]

## See also
- [[plugins]] · [[finance]] · [[plugin-investment-banking]] · [[plugin-private-equity]] · [[plugin-equity-research]] (all consume this plugin's models)
