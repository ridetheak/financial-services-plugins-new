---
title: Ingestion Log
type: meta
domain: general
tags: [changelog, append-only]
sources: []
updated: 2026-05-31
status: stable
---

# Ingestion Log

Append-only record of every ingestion pass. Newest entries at the top.

---

## 2026-05-31 (3) — Translate Chinese SKILL.md and commands to English (Phase 1)

**Sources translated** (overwritten in place — these are the canonical plugin source files):
- 8 × Chinese `equity-research/skills/*/SKILL.md` files:
  - `catalyst-calendar`, `earnings-analysis`, `earnings-preview`, `idea-generation`, `model-update`, `morning-note`, `sector-overview`, `thesis-tracker`
- 6 × Chinese `equity-research/commands/*.md` files:
  - `catalysts.md`, `earnings-preview.md`, `initiate.md`, `model-update.md`, `morning-note.md`, `screen.md`

(`initiating-coverage/SKILL.md` and `earnings.md` were already in English and untouched.)

**Wiki updates**:
- 8 playbook pages: removed Chinese title parentheticals and the "SKILL.md is in Chinese" disclaimers
- `wiki/entities/plugin-equity-research.md`: removed the "Most SKILL.md content is in Chinese..." caveat and Chinese parens in the skill list

**Summary**: First translation pass per user request "translate them to English and get rid of the Chinese." Preserved structure, trigger phrases (re-rendered in English), and financial domain terminology. Verified: no CJK Unified Ideograph (`[一-龯]`) characters remain in any translated file or wiki page.

**Phase 2 queued** (not yet translated): 11 large reference / asset files (~6,700 lines):
- `equity-research/skills/earnings-analysis/references/{best-practices,report-structure,workflow}.md`
- `equity-research/skills/initiating-coverage/assets/{quality-checklist,report-template}.md`
- `equity-research/skills/initiating-coverage/references/{task1-company-research,task2-financial-modeling,task3-valuation,task4-chart-generation,task5-report-assembly,valuation-methodologies}.md`

---

## 2026-05-31 (2) — Ingest in-repo plugin content

**Sources processed** (treated as authoritative in-repo source, not duplicated into `raw/`):
- `.claude-plugin/marketplace.json`
- 7 × `*/.claude-plugin/plugin.json` (investment-banking, equity-research, financial-analysis, private-equity, wealth-management, partner-built/lseg, partner-built/spglobal)
- 52 × `*/skills/*/SKILL.md` (full list cited in each playbook page's `sources:` frontmatter)
- Selected reference templates inside skill folders (initiating-coverage report template, pitch-deck slide templates, tear-sheet style spec, earnings-preview-beta report template)

**Pages created** (108 total):
- **Plugin entity pages (7)**: `wiki/entities/plugin-investment-banking.md`, `plugin-equity-research.md`, `plugin-financial-analysis.md`, `plugin-private-equity.md`, `plugin-wealth-management.md`, `plugin-lseg.md`, `plugin-spglobal.md`
- **Data-source entity stubs (2)**: `wiki/entities/kensho.md`, `wiki/entities/capital-iq.md`
- **Stable concept pages (17)**: `tear-sheet`, `dcf`, `lbo`, `comps-analysis-concept`, `3-statement-model`, `wacc`, `cim`, `teaser`, `merger-model`, `pitch-deck`, `ic-memo-concept`, `due-diligence`, `moic-irr`, `unit-economics-concept`, `value-creation-plan-concept`, `yield-curve`, `fx-carry`, `tax-loss-harvesting-concept`, `financial-plan-concept`
- **Stub concept pages (29)**: sell-side-process, catalyst, investment-thesis, earnings-preview-concept, morning-note-concept, initiating-coverage-concept, sector-overview-concept, competitive-analysis-concept, buyer-list-concept, process-letter-concept, check-deck-concept, check-model-concept, dd-checklist-concept, deal-screening-concept, portfolio-monitoring-concept, portfolio-rebalance-concept, client-review-concept, investment-proposal-concept, bond-futures-basis-concept, bond-relative-value-concept, fixed-income-portfolio-concept, swap-curve, option-vol, macro-rates, ebitda-bridge, asset-allocation, wash-sale-rule, plugin-engineering — *(all flagged `status: stub`, ready for expansion on next ingest)*
- **Playbook pages (53)**: one per SKILL.md across all 7 plugins; structure: trigger phrases, one-paragraph description, key-concept links, source path

**Pages updated**:
- `wiki/index.md` — added entity + concept + playbook sections, organized by category; total page count
- `wiki/glossary.md` — populated A-W with the term-level vocabulary surfaced during ingestion
- `wiki/domains/finance.md` and `wiki/domains/plugins.md` — replaced stub content with curated landing pages

**Naming collision resolved**: `tear-sheet` exists as both a concept and a skill. Renamed the playbook to `tear-sheet-skill.md`; concept remains `tear-sheet.md`. Updated `[[plugin-spglobal]]` references accordingly.

**Summary**: First substantive ingest. Took the existing plugin marketplace (7 plugins, 52 skills, 46 commands) and synthesized it into a navigable wiki of 115 pages. The wiki now describes WHAT each plugin does (entity pages), WHAT financial concepts they operate on (concept pages), and HOW each skill is triggered/used (playbook pages). Cross-linking is dense — every playbook links to its plugin entity + 2-4 concept pages, every concept links to the playbooks that use it. Tear-sheet treatment is richer per user emphasis: a dedicated concept page captures the style spec, audience variants, and S&P Capital IQ data sourcing constraints.

**Not yet ingested** (queued for future passes):
- `outputs/` — generated artifacts (alibaba competitive analysis, apple 3-statement model, baidu comps). Useful as worked examples; not knowledge per se.
- `docs/analysis/` — architectural analysis docs, several in Chinese (MCP discovery, datapack-builder analysis, skills inference). Substantive but dense; would benefit from a dedicated pass.
- `docs/base/LOCAL_FILES_INVENTORY.md` and `docs/base/README_CN.md` — local inventory + Chinese README.
- `outputs/alibaba_competitive_analysis.md` — could become a worked-example reference page.

**Outstanding stub concepts** (28 listed above): all are real concepts that earned a stub because something linked to them, but they're awaiting source material to flesh out. Drop relevant notes/PDFs/URLs into `raw/` and run `ingest` to populate.

---

## 2026-05-31 — Wiki bootstrap
- **Sources processed**: *(none — this is the bootstrap entry)*
- **Pages created**:
  - `wiki/index.md`
  - `wiki/glossary.md`
  - `wiki/log.md` (this file)
  - `wiki/meta/wiki-setup.md`
  - `wiki/domains/finance.md` (stub)
  - `wiki/domains/plugins.md` (stub)
- **Pages updated**: *(none — initial creation)*
- **Summary**: Scaffolded the wiki schema in `CLAUDE.md`, created `raw/` and `wiki/` directory trees, and seeded the meta pages. Topic scope: financial services domain knowledge + Claude Cowork plugin engineering, unified in one wiki with namespaced subfolders so concepts can cross-link freely. Ready to ingest `raw/` material on next prompt.
