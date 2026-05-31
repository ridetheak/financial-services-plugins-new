---
title: PPT Template Creator (meta-skill)
type: playbook
domain: plugins
tags: [meta-skill, ppt, template, skill-building]
sources:
  - financial-analysis/skills/ppt-template-creator/SKILL.md
updated: 2026-05-31
status: stable
---

# PPT Template Creator (meta-skill)

**Plugin**: [[plugin-financial-analysis]]
**Triggers**: user wants to turn a PowerPoint template into a reusable skill (NOT for generating presentations — use `pptx` skill for that)

**Meta-skill**: takes a user-provided PowerPoint template and produces a **new self-contained skill** (with `assets/template.pptx` + a generated `SKILL.md` of instructions) that can later generate presentations from that template.

Distinct from [[pitch-deck-playbook]] (which populates IB pitch deck templates) — this one *creates* a skill *from* a template.

**Key concepts**: [[plugin-engineering]] · [[skill-creator-concept]] · [[pitch-deck]]
**Source**: `financial-analysis/skills/ppt-template-creator/SKILL.md`
