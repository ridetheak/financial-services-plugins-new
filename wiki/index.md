---
title: Wiki Index
type: meta
domain: general
tags: [index, navigation]
sources: []
updated: 2026-05-31
status: stable
---

# Wiki Index

Master table of contents. Every wiki page is reachable from here.

## Domains
- [[finance]] — financial services domain knowledge
- [[plugins]] — Claude Cowork plugin engineering

## Meta
- [[wiki-setup]] — how this wiki was bootstrapped and how to use it
- [[glossary|Glossary]] — terms and short definitions
- [[log|Ingestion Log]] — append-only changelog

---

## Entities — Plugins

The seven plugins in this marketplace, each as a wiki entity that lists its skills:

- [[plugin-investment-banking]] — IB productivity, sell-side M&A
- [[plugin-equity-research]] — earnings, coverage, morning notes (mostly Chinese SKILLs)
- [[plugin-financial-analysis]] — DCF, LBO, comps, modeling, QC
- [[plugin-private-equity]] — PE deal cycle: sourcing → IC → portfolio
- [[plugin-wealth-management]] — advisor client workflow
- [[plugin-lseg]] — partner-built: fixed income, FX, vol, macro/rates
- [[plugin-spglobal]] — partner-built: tear sheets, earnings, deal flow

## Entities — Data sources
- [[kensho]] — S&P Global's LLM-ready API MCP (stub)
- [[capital-iq]] — S&P Capital IQ data backbone (stub)

---

## Concepts

### Valuation & modeling
[[dcf]] · [[wacc]] · [[lbo]] · [[comps-analysis-concept]] · [[3-statement-model]] · [[merger-model]]

### M&A artifacts
[[cim]] · [[teaser]] · [[pitch-deck]] · [[buyer-list-concept]] · [[process-letter-concept]] · [[sell-side-process]]

### Private equity
[[ic-memo-concept]] · [[due-diligence]] · [[moic-irr]] · [[unit-economics-concept]] · [[value-creation-plan-concept]] · [[ebitda-bridge]] · [[deal-screening-concept]] · [[dd-checklist-concept]] · [[portfolio-monitoring-concept]]

### Equity research
[[investment-thesis]] · [[catalyst]] · [[earnings-preview-concept]] · [[morning-note-concept]] · [[initiating-coverage-concept]] · [[sector-overview-concept]] · [[competitive-analysis-concept]]

### Wealth management
[[financial-plan-concept]] · [[tax-loss-harvesting-concept]] · [[wash-sale-rule]] · [[portfolio-rebalance-concept]] · [[asset-allocation]] · [[client-review-concept]] · [[investment-proposal-concept]]

### Fixed income, rates, FX, derivatives (LSEG)
[[yield-curve]] · [[swap-curve]] · [[macro-rates]] · [[fx-carry]] · [[option-vol]] · [[bond-futures-basis-concept]] · [[bond-relative-value-concept]] · [[fixed-income-portfolio-concept]]

### QC
[[check-deck-concept]] · [[check-model-concept]]

### Tear sheet (user-prioritized)
[[tear-sheet]] — distilled concept page with style spec and audience templates

### Plugin engineering
[[plugin-engineering]]

---

## Playbooks (skills as wiki pages)

### Investment Banking
[[buyer-list]] · [[cim-builder]] · [[datapack-builder]] · [[deal-tracker]] · [[merger-model-playbook]] · [[pitch-deck-playbook]] · [[process-letter]] · [[strip-profile]] · [[teaser-playbook]]

### Equity Research
[[catalyst-calendar]] · [[earnings-analysis]] · [[earnings-preview]] · [[idea-generation]] · [[initiating-coverage]] · [[model-update]] · [[morning-note]] · [[sector-overview]] · [[thesis-tracker]]

### Financial Analysis
[[3-statements]] · [[check-deck]] · [[check-model]] · [[competitive-analysis]] · [[comps-analysis]] · [[dcf-model]] · [[lbo-model]] · [[ppt-template-creator]] · [[skill-creator]]

### Private Equity
[[dd-checklist]] · [[dd-meeting-prep]] · [[deal-screening]] · [[deal-sourcing]] · [[ic-memo]] · [[portfolio-monitoring]] · [[returns-analysis]] · [[unit-economics]] · [[value-creation-plan]]

### Wealth Management
[[client-report]] · [[client-review]] · [[financial-plan]] · [[investment-proposal]] · [[portfolio-rebalance]] · [[tax-loss-harvesting]]

### LSEG (partner)
[[bond-futures-basis]] · [[bond-relative-value]] · [[lseg-equity-research]] · [[fixed-income-portfolio]] · [[fx-carry-trade]] · [[macro-rates-monitor]] · [[option-vol-analysis]] · [[swap-curve-strategy]]

### S&P Global (partner)
[[earnings-preview-beta]] · [[funding-digest]] · [[tear-sheet-skill]]

---

## Stats
- **Entities**: 9 (7 plugins + 2 data-source stubs)
- **Concepts**: 47 (17 stable, 30 stubs awaiting expansion)
- **Playbooks**: 53 (52 skill playbooks + the tear-sheet-skill rename)
- **Total wiki pages**: 115

To grow the wiki: drop material into `raw/` and say `ingest`.
