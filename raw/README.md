# raw/ — Immutable Source Documents

**Rules:**
- This folder is **append-only** from your side and **read-only** for Claude.
- Drop anything you want ingested into the appropriate subfolder (or `inbox/` if unsure).
- Claude reads these files during ingestion but never modifies, moves, or deletes them.

**Subfolders:**
- `inbox/` — default drop zone for anything unsorted
- `urls/` — web clips and articles (save as `.md` with original URL at the top)
- `pdfs/` — PDFs, reports, decks, filings
- `code/` — code snippets, configs, file snapshots
- `notes/` — rough notes, brain-dumps, transcripts, voice memo text

To trigger ingestion, say **`ingest`** or **`compile`** in chat.
See `CLAUDE.md` (root) for the full schema.
