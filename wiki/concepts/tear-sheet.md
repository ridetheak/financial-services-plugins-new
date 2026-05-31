---
title: Tear Sheet
type: concept
domain: finance
tags: [tear-sheet, company-profile, one-pager, capital-iq, sp-global]
sources:
  - partner-built/spglobal/skills/tear-sheet/SKILL.md
updated: 2026-05-31
status: stable
---

# Tear Sheet

A **tear sheet** is a one-to-two page financial summary of a single company. The format is institutional, dense with data, and audience-specific. It's the highest-volume artifact in equity research, IB, corporate development, and sales/BD prep.

Origin of the term: in the print era, an analyst would literally tear the relevant company page out of a reference book to bring to a meeting.

## Audience variants

The [[plugin-spglobal]] `tear-sheet` skill defines four audiences. Each variant emphasizes different sections:

| Audience | Emphasis |
|---|---|
| **Equity research** | Valuation multiples, estimates vs actuals, thesis bullets, target price |
| **Investment banking / M&A** | Capitalization, recent transactions, strategic fit, ownership |
| **Corporate development** | Strategic fit, integration considerations, capability gaps |
| **Sales / BD** | Conversation starters, recent news, key relationships |

If audience is unspecified, the skill asks before generating.

## Standard sections (any variant)

1. **Header banner** — Company name + identifiers + key financials in a two-column borderless table (ticker, HQ, founded, employees on left; market cap, EV, stock price, shares outstanding on right). Critical: do NOT stack everything in a single left column — the two-column spread is the visual signal that distinguishes a professional tear sheet.
2. **Company overview** — what they do, business model, segments
3. **Financial summary** — recent quarter and trailing periods, key ratios
4. **Valuation** — multiples vs peers, target price (if applicable)
5. **Audience-specific signature block** — see table above
6. **Footer / disclaimer**

## Style spec (from the `tear-sheet` skill)

- **Colors**: primary navy `#1F3864` (header banner, section headers), accent `#2E75B6`, table fills `#D6E4F0` / `#F2F2F2`, borders `#CCCCCC`
- **Font**: Arial (Calibri at many banks); company name 18pt bold, section headers 11pt bold in primary color, body 9pt
- **Section headers**: 12pt before, 0pt after, bottom border `#CCCCCC` 0.5pt — applied to the heading paragraph itself, not a separate paragraph
- **Bullets**: single `•` character throughout; synthesis bullets get 0.25" hanging indent, informational bullets get standard body indent
- **Tables**: bordered tables are reserved for financial data only; header key-value blocks use unbordered tables

## Data sources

The S&P Global skill pulls live data from **S&P Capital IQ** via the **Kensho LLM-ready API MCP** (`kfinance`). No web fallback — explicit constraint in the skill.

## Related artifacts
- [[strip-profile]] — IB-flavored multi-slide company profile (richer than a single tear sheet)
- [[teaser]] — anonymous one-page sell-side teaser (deliberately omits identity)
- [[pitch-deck]] — full pitch book (tear sheet is often one slide inside)

## See also
- [[plugin-spglobal]] · [[finance]] · [[capital-iq]] · [[kensho]]
