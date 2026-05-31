---
title: Plugins
type: domain
domain: plugins
tags: [landing, claude-cowork, plugin-engineering]
sources:
  - .claude-plugin/marketplace.json
  - CLAUDE.md
updated: 2026-05-31
status: stable
---

# Plugins

Landing page for the Claude Cowork plugin marketplace that lives in this repo. The architectural counterpart to [[finance]].

## The marketplace

Registered in `.claude-plugin/marketplace.json` (owner: Anthropic). Seven plugins:

| Plugin | Path | Entity |
|---|---|---|
| financial-analysis | `financial-analysis/` | [[plugin-financial-analysis]] |
| investment-banking | `investment-banking/` | [[plugin-investment-banking]] |
| equity-research | `equity-research/` | [[plugin-equity-research]] |
| private-equity | `private-equity/` | [[plugin-private-equity]] |
| wealth-management | `wealth-management/` | [[plugin-wealth-management]] |
| lseg | `partner-built/lseg/` | [[plugin-lseg]] |
| sp-global | `partner-built/spglobal/` | [[plugin-spglobal]] |

The first five are first-party; the last two are partner-built.

## Plugin anatomy

Each plugin follows the same layout (defined in root `CLAUDE.md`):

```
plugin-name/
├── .claude-plugin/plugin.json   # Manifest
├── commands/                    # Slash commands (.md)
├── skills/                      # SKILL.md files (procedural knowledge)
├── hooks/                       # Event-driven automation
├── mcp/                         # MCP integrations
└── .claude/                     # User config
```

- **Skills** map to wiki [[playbooks]] (see [[index]] for the full list of 52)
- **plugin.json** is the entity-page source
- **Commands** are the user-facing CLI surface (`/plugin:command`)

## Meta-skills (skills about building skills)

- [[skill-creator]] — guide for authoring new skills
- [[ppt-template-creator]] — turn a PPT template into a reusable skill

See [[plugin-engineering]] for the stub concept page.

## Cross-plugin patterns

- **Modeling foundation**: [[plugin-financial-analysis]]'s [[dcf-model]] / [[lbo-model]] / [[3-statements]] are consumed by IB, ER, and PE workflows
- **QC layer**: [[check-deck]] and [[check-model]] (in financial-analysis) gate any client-ready deliverable from IB or PE
- **Tear sheets**: [[plugin-spglobal]]'s [[tear-sheet-skill]] is the canonical implementation; [[strip-profile]] (in IB) is the multi-slide cousin
- **Vendor MCP routing**: LSEG and S&P Global skills all share the pattern of routing MCP tool outputs into structured analyses — let the tools compute, the skill interprets

## See also
- [[finance]] · [[index]] · [[wiki-setup]]
- `CLAUDE.md` Part 1 (root) — full marketplace structure
