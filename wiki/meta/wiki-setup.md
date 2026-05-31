---
title: Wiki Setup
type: meta
domain: general
tags: [bootstrap, karpathy, wiki-pattern, knowledge-management]
sources: []
updated: 2026-05-31
status: stable
---

# Wiki Setup

This page records the bootstrap of the knowledge wiki living inside the `financial-services-plugins-new` repository. It is the first wiki entry — a deliberate meta-acknowledgement of the system itself.

## What this wiki is

A two-layer, self-evolving knowledge base modeled on Andrej Karpathy's LLM-wiki pattern:

- **`raw/`** — immutable inputs (notes, URLs, PDFs, code, transcripts). The audit trail.
- **`wiki/`** — synthesized, cross-linked markdown that Claude curates. The memory layer.

The full schema and operating rules live in `CLAUDE.md` at the repository root.

## Scope

Decided at bootstrap:

- **Topic**: financial services domain knowledge **+** Claude Cowork plugin engineering. Hybrid by design — the plugins in this repo (`investment-banking/`, `equity-research/`, `financial-analysis/`, `private-equity/`, `wealth-management/`) operate on the financial domain the wiki documents, so cross-linking between a `[[concept]]` and an `[[entity]]` and a plugin pattern is the point.
- **Sources**: open — anything the user is interested in (web URLs, PDFs, code, rough notes, transcripts). The schema allows a future split into separate `wiki-<topic>/` trees if any single domain grows beyond ~50 pages or becomes thematically distinct. Until then, one unified wiki maximizes serendipitous links.

See [[finance]] and [[plugins]] for the two top-level domain landing pages.

## How to use it

| You do | Claude does |
|---|---|
| Drop a file into `raw/` (any subfolder, or `inbox/`) | Nothing yet — waits for trigger |
| Type `ingest` or `compile` | Reads new `raw/` files, synthesizes into `wiki/` pages, cross-links, updates `[[index]]` and `[[glossary]]`, appends to `[[log]]` |
| Ask a substantive question | Treats `wiki/` as primary memory; cites pages; offers to ingest anything still sitting raw |
| Type `audit` | Surfaces orphan pages, broken wikilinks, stale stubs |
| Type `graph` | Renders a markdown summary of the link structure |

## Invariants worth re-stating

- `raw/` is **never** modified by Claude.
- `[[wiki/log.md|log]]` is **append-only**.
- Every wiki page must be reachable from `[[index]]`.
- Dangling `[[wikilinks]]` are not allowed — every reference either resolves to an existing page or creates a stub on the spot.

## What happens next

The wiki is empty (apart from this meta page and two domain stubs). To make it useful: drop notes, PDFs, code, or URLs into `raw/` and say `ingest`. The synthesis loop will fill `[[concepts]]`, `[[entities]]`, and `[[playbooks]]` from there.

## See also

- `CLAUDE.md` (root) — the full schema
- [[index]] — master table of contents
- [[glossary]] — term definitions
- [[log]] — ingestion changelog
- [[finance]] — financial domain landing
- [[plugins]] — plugin engineering landing
