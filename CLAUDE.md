# Financial Services Plugins + Knowledge Wiki

This repository is two things at once:

1. **A Claude Cowork plugin marketplace** for financial services professionals (each subdirectory is a standalone plugin).
2. **A self-evolving knowledge wiki** (Karpathy-style) — `raw/` holds immutable inputs, `wiki/` holds a synthesized, cross-linked, queryable memory layer.

The wiki is the persistent memory; the plugins are tools that operate on the domain the wiki documents.

---

## Part 1 — Plugin Marketplace

### Repository Structure (plugins)
```
├── investment-banking/     # IB productivity
├── equity-research/        # Research workflows
├── financial-analysis/     # Modeling, ratios, fundamentals
├── private-equity/         # PE deal & portfolio work
├── wealth-management/      # WM client & portfolio
├── partner-built/          # Third-party / partner plugins
├── tools/                  # Cross-plugin tooling
├── docs/                   # Plugin docs
└── outputs/                # Generated artifacts
```

### Plugin Layout
```
plugin-name/
├── .claude-plugin/plugin.json   # Manifest (name, description, version)
├── commands/                    # Slash commands (.md)
├── skills/                      # Knowledge for specific tasks
├── hooks/                       # Event-driven automation
├── mcp/                         # MCP server integrations
└── .claude/                     # User settings (*.local.md)
```

### Plugin Key Files
- `marketplace.json` — registers all plugins with source paths
- `plugin.json` — plugin metadata and component discovery
- `commands/*.md` — slash commands, invoked as `/plugin:command-name`
- `skills/*/SKILL.md` — knowledge and workflows for specific tasks
- `*.local.md` — user-specific config (gitignored)
- `mcp-categories.json` — canonical MCP category definitions shared across plugins

### Plugin Dev Workflow
1. Edit markdown directly — changes take effect immediately.
2. Test commands with `/plugin:command-name` syntax.
3. Skills auto-invoke when their trigger conditions match.

---

## Part 2 — Knowledge Wiki Schema

### Purpose
A persistent, queryable memory layer. Raw inputs are ingested into `raw/`; Claude synthesizes them into structured, cross-linked markdown in `wiki/`. The wiki survives across sessions and becomes more valuable the more it absorbs.

### Folder Layers

#### `raw/` — IMMUTABLE source documents
Claude may **READ but NEVER MODIFY, MOVE, OR DELETE** anything here. This is the audit trail.

| Subfolder | Contents |
|---|---|
| `raw/inbox/` | Default drop zone for unsorted material |
| `raw/urls/` | Web clips, articles, links (typically `.md` with original URL preserved at top) |
| `raw/pdfs/` | PDFs, reports, decks, filings |
| `raw/code/` | Code snippets, configs, snapshots of relevant files |
| `raw/notes/` | Rough notes, brain-dumps, transcripts, voice memo text |

#### `wiki/` — SYNTHESIZED knowledge
Claude curates these continuously.

| Path | Role |
|---|---|
| `wiki/index.md` | Master table of contents, organized by domain |
| `wiki/glossary.md` | Terms and short definitions, alphabetized |
| `wiki/log.md` | Append-only ingestion log (date, sources, pages touched) |
| `wiki/concepts/` | Abstract concepts, theories, methods, frameworks |
| `wiki/entities/` | Named things: companies, people, products, tools, regulators |
| `wiki/playbooks/` | Procedural how-tos and SOPs |
| `wiki/domains/` | Top-level domain landing pages (e.g., `finance.md`, `plugins.md`) |
| `wiki/meta/` | Pages about the wiki itself |

### Naming & Linking Conventions
- **Filenames**: kebab-case, descriptive. `discounted-cash-flow.md`, not `DCF.md` or `Discounted_Cash_Flow.md`.
- **Internal links**: Obsidian-style wikilinks — `[[discounted-cash-flow]]` or `[[discounted-cash-flow|DCF]]` for an aliased label.
- **Cross-link aggressively** — every page should link to related concepts, entities, and at least one parent `domains/` page.
- **Dangling links create stubs**: if a `[[wikilink]]` target doesn't exist, immediately create a stub page with title + `status: stub` frontmatter + a "first mentioned in" backlink. Never leave a broken link.

### Page Frontmatter (required on every wiki page)
```yaml
---
title: Discounted Cash Flow
type: concept           # concept | entity | playbook | domain | meta | glossary
domain: finance         # finance | plugins | general
tags: [valuation, modeling]
sources:
  - raw/notes/2026-05-31-dcf-notes.md
  - raw/urls/damodaran-dcf.md
updated: 2026-05-31
status: stub            # stub | draft | stable | deprecated
---
```

### Ingestion Workflow
Triggered when the user says **"ingest"**, **"compile"**, **"compile wiki"**, or **"ingest <file>"**.

1. **Scan** `raw/` for files added or modified since the last `wiki/log.md` entry.
2. For each new/changed raw file:
   - **Read** it fully.
   - **Identify** concepts, entities, procedures, and terms.
   - For each unit of knowledge: **update** an existing wiki page (merging, preserving prior content) **or create** a new one in the right subfolder.
   - **Append** the raw file path to the `sources:` frontmatter of every page it informed.
   - **Insert `[[wikilinks]]`** to related pages; create stubs for any link with no target.
   - **If a new term appears**, append it to `wiki/glossary.md` (alphabetized).
3. **Update** `wiki/index.md` so new pages are reachable.
4. **Append** one dated entry to `wiki/log.md`:
   ```
   ## 2026-05-31
   - **Sources processed**: raw/notes/foo.md, raw/urls/bar.md
   - **Pages created**: wiki/concepts/foo.md, wiki/entities/bar.md
   - **Pages updated**: wiki/glossary.md, wiki/index.md
   - **Summary**: one or two sentences on what changed and why.
   ```
5. **Never** touch files in `raw/`.

### Query Workflow
Triggered when the user asks a substantive question (or says **"query: <q>"**).

1. Treat `wiki/` as primary memory. Start at `wiki/index.md` or `wiki/glossary.md`.
2. Follow `[[wikilinks]]` to gather context across pages.
3. If the wiki is silent or thin on the topic, check `raw/` for unprocessed material and **offer to ingest** before answering from raw directly.
4. **Cite** wiki pages in answers using their path: e.g. *"see `wiki/concepts/dcf.md`"*.

### Maintenance Invariants
- `raw/` is **append-only** from the user, **read-only** to Claude.
- Every wiki page must be reachable from `wiki/index.md` — no orphans.
- `wiki/log.md` is **append-only**; never rewrite history.
- Never delete a wiki page without explicit instruction — mark `status: deprecated` and add a forwarding `[[link]]` instead.
- If any single domain grows past ~50 pages or becomes thematically distinct, **propose spinning it off** into its own `wiki-<topic>/` tree rather than letting `wiki/` bloat. Until then, prefer one unified wiki for cross-domain linking.
- PDFs in `raw/pdfs/` can be large; if commit size becomes a concern, the user may gitignore that subfolder — Claude must still treat referenced PDFs as authoritative when present.

### Command Shortcuts (just type these in chat)
| Phrase | Action |
|---|---|
| `ingest` / `compile` | Run the Ingestion Workflow on all unprocessed `raw/` |
| `ingest <path>` | Process just one raw file |
| `query: <question>` | Run the Query Workflow |
| `stub <topic>` | Create a placeholder wiki page for future fill-in |
| `graph` | Render a markdown summary of the wiki's link structure |
| `audit` | Check for orphan pages, broken `[[wikilinks]]`, stale stubs |

---

## How the Two Parts Relate
- A plugin in `investment-banking/` can reference wiki pages as its knowledge source (e.g., a skill that explains DCF can cite `wiki/concepts/discounted-cash-flow.md`).
- Conversely, plugin engineering decisions are themselves documented in `wiki/domains/plugins.md` and child pages — the wiki is meta-aware of the marketplace it lives inside.
