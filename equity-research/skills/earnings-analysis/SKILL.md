---
name: earnings-analysis
description: Create a professional equity research earnings update report (8-12 pages, 3,000-5,000 words) analyzing quarterly results for a covered company. Fast-turnaround format focused on beat/miss analysis, key metrics, updated estimates, and revised thesis. Includes 1-3 summary tables and 8-12 charts. Use when the user requests an "earnings update", "quarterly update", "earnings analysis", "Q1/Q2/Q3/Q4 results", or post-earnings report.
---

# Equity Research Earnings Update

Create a professional **earnings update report** analyzing quarterly results for a covered company, following institutional standards (JPMorgan, Goldman Sachs, Morgan Stanley format).

**Key Characteristics:**
- **Length**: 8-12 pages
- **Word count**: 3,000-5,000 words
- **Tables**: 1-3 summary tables (not comprehensive)
- **Charts**: 8-12
- **Turnaround time**: 1-2 days (within 24-48 hours of earnings release)
- **Audience**: Clients already familiar with the company
- **Focus**: What's new — beat/miss, updated estimates, thesis impact
- **Font**: Times New Roman throughout (unless user specifies otherwise)

## When to Use

Use when the user requests:
- "Create an earnings update for [Company] Q3 2024"
- "Analyze [Company]'s quarterly results"
- "[Company]'s post-earnings report"
- "[Company]'s Q1/Q2/Q3/Q4 update"

**Do NOT use when:**
- User requests an "initiation report" → use a different skill
- User requests a "quick note" or "quick take" → different format
- Company is not covered → need to initiate coverage first

## Key Requirements

### 1. Speed and Timeliness
- Publish within 24-48 hours of earnings release
- Focus only on new information
- Do not over-rehash company background

### 2. Beat/Miss Analysis
- State upfront whether the company beat or missed
- Quantify the variance (e.g., "revenue beat by $120M or 3%")
- Explain WHY results differed from expectations

### 3. Summary Format
- Keep tables to 1-3 (summary only, not comprehensive)
- No full P&L / cash flow / balance sheet (key metrics only)
- Assume reader has seen the initiation report

### 4. Citations and Source Attribution ⭐⭐⭐ MANDATORY

**Critical**: Properly cite all data with specific sources and clickable hyperlinks.

**Include specific citations and clickable links in every chart and table:**

```
Source: Q3 2024 10-Q, filed November 8, 2024; Company earnings release
       [Hyperlink "10-Q" to: https://www.sec.gov/cgi-bin/viewer?accession=...]
       [Hyperlink "earnings release" to: https://investor.company.com/news/q3-2024]
```

**How hyperlinks appear in Word:**
- Filename shown as blue, underlined, clickable link
- Reader can Ctrl+Click to open source directly
- Not plain text URLs — formatted hyperlinks with display text

**Required source list:**

Cite in every earnings update:
- ✅ Earnings release (include date and URL)
- ✅ 10-Q filing (include filing date and EDGAR link via `edgar_full_text_search` or direct EDGAR URL)
- ✅ Earnings call transcript (include date; retrieve via `equity_fundamental_transcript` from AE composite MCP, or from company IR site)
- ✅ Investor presentation / supplemental materials (if available on company IR site)
- ✅ Consensus estimates source (AE composite MCP / openbb preferred — use `equity_estimates_consensus`, `equity_estimates_forward_eps`, `equity_estimates_forward_sales`, or `earnings_review`; fall back to SEC EDGAR filings; do NOT use Bloomberg/FactSet — unavailable; include "as of" date)
- ✅ Prior guidance (from prior quarter's materials)

**Sources section with clickable hyperlinks at end of report:**

```
Sources and References

Earnings Materials (Q3 2024):
• Earnings Release (November 7, 2024)
  [Hyperlink entire line to: https://investor.company.com/news/q3-2024-earnings]

• Form 10-Q (filed November 8, 2024)
  [Hyperlink to: https://www.sec.gov/cgi-bin/viewer?accession=...]

• Earnings Call Transcript (November 7, 2024)
  [Retrieved via equity_fundamental_transcript (AE composite MCP);
   Hyperlink to company IR site or SEC filing if available]

• Investor Presentation (November 7, 2024)
  [Hyperlink to: https://investor.company.com/presentations/q3-2024.pdf]
```

**Verification Checklist:**
- [ ] Every chart has source with specific document and date
- [ ] Every table has source and document reference
- [ ] Beat/miss analysis cites consensus source and date
- [ ] Guidance changes cite current and prior guidance sources
- [ ] Key statistics have footnotes
- [ ] Sources section lists all materials with URLs
- [ ] All URLs are clickable hyperlinks (not plain text)
- [ ] All SEC filings hyperlinked to EDGAR viewer

### 5. Updated Estimates
- Update forward estimates based on results
- Clearly show old vs. new estimates
- Explain what changed and why

## Detailed Workflow

The earnings update process follows 5 phases:

### Phase 1: Data Collection (30-60 minutes)

**🚨🚨🚨 CRITICAL: Training data is stale 🚨🚨🚨**

**Before starting — complete these 4 steps in order:**
1. **Check today's date** — write down the current date
2. **Pull latest data** — use AE composite MCP (`earnings_review`, `equity_calendar_earnings`, `company_briefing`) as the first stop; supplement with `equity_fundamental_transcript` for the call transcript and `edgar_full_text_search` for filings
3. **Verify the date** — confirm the earnings release is within the past 3 months
4. **Check transcript date** — verify transcript date matches release date

**Common mistake**: Using stale earnings calls from training data instead of pulling live data via AE composite MCP tools.

**Data sources — use in priority order:**
1. **AE composite MCP (openbb)** — `earnings_review` for beat/miss summary; `equity_estimates_consensus`, `equity_estimates_forward_eps`, `equity_estimates_forward_ebitda`, `equity_estimates_forward_sales` for pre-earnings consensus; `equity_fundamental_income`, `equity_fundamental_metrics`, `equity_fundamental_ratios` for reported financials; `equity_fundamental_revenue_per_segment`, `equity_fundamental_revenue_per_geography` for segment/geo breakdown; `equity_fundamental_transcript` for the call transcript; `equity_price_quote`, `equity_price_historical`, `equity_price_performance` for price data; `company_briefing` for narrative context
2. **SEC EDGAR filings** — 10-Q / 10-K / 8-K for authoritative reported results; use `edgar_full_text_search` or direct EDGAR links
3. **Company investor relations site** — earnings press release, supplemental data, presentation slides (accessed via web search or direct URL)

**Requirements:**
- ✅ Pull latest earnings via AE composite MCP first — do not rely on training data
- ✅ Write down today's date and the release date found
- ✅ Verify release date is within 3 months of today
- ✅ Verify transcript date matches release date
- ✅ If dates do not match or are too old (>3 months), search again

**See [references/workflow.md](references/workflow.md)** for detailed search procedures and verification steps.

### Phase 2: Analysis (2-3 hours)
- Beat/miss analysis for each key metric (use `earnings_review` and `equity_estimates_consensus`)
- Segment / geographic / product breakdown (use `equity_fundamental_revenue_per_segment`, `equity_fundamental_revenue_per_geography`)
- Margin and guidance analysis (use `equity_fundamental_metrics`, `equity_fundamental_ratios`)
- Update financial model and estimates (use `equity_estimates_forward_eps`, `equity_estimates_forward_ebitda`, `equity_estimates_forward_sales`)

**See [references/workflow.md](references/workflow.md)** for detailed analysis framework.

### Phase 3: Chart Generation (1-2 hours)
Create 8-12 charts focused on quarterly trends and what's new:
- Quarterly revenue progression
- Quarterly EPS progression
- Quarterly margin trends
- Revenue by segment / geography
- Key operating metrics
- Beat/miss summary
- Estimate revisions
- Valuation charts

**See [references/workflow.md](references/workflow.md)** for chart specifications.

### Phase 4: Report Creation (2-3 hours)
Create 8-12 page DOCX report with specific structure.

**See [references/report-structure.md](references/report-structure.md)** for complete page-by-page template and formatting requirements.

**High-level structure:**
- Page 1: Earnings summary with rating and price target
- Pages 2-3: Detailed results analysis
- Pages 4-5: Key metrics and guidance
- Pages 6-7: Updated investment thesis
- Pages 8-10: Valuation and estimates
- Pages 11-12: Appendix (optional)

### Phase 5: Quality Check and Delivery (30 minutes)
Verify content, format, accuracy, and timeliness before delivery.

**See [references/best-practices.md](references/best-practices.md)** for quality checklist and common errors to avoid.

## Output Specifications

**Primary deliverable**: DOCX report (8-12 pages)
**File name**: `[Company]_Q[Quarter]_[Year]_Earnings_Update.docx`
**Example**: `Nike_Q2_FY24_Earnings_Update.docx`

**Contents:**
- Page 1: Summary with rating, price target, key takeaways
- Pages 2-3: Detailed results analysis
- Pages 4-5: Key metrics and guidance
- Pages 6-7: Updated thesis assessment
- Pages 8-10: Valuation and estimates
- Pages 11-12: Appendix (optional)
- 8-12 embedded charts
- 1-3 summary tables
- Complete sources section with clickable hyperlinks

**Optional deliverable**: XLS model update (optional for earnings updates)

## Key Differences vs. Initiation Report

| Aspect | Earnings Update | Initiation Report |
|--------|----------------|------------------|
| **Length** | 8-12 pages | 30-50 pages |
| **Word count** | 3,000-5,000 | 10,000-15,000 |
| **Tables** | 1-3 summary | 12-20 comprehensive |
| **Charts** | 8-12 | 25-35 |
| **Turnaround** | 1-2 days | 3-6 weeks |
| **Scope** | Quarterly results | Full company |
| **Focus** | What's new | Everything |
| **Company background** | Brief mention | 6-10 pages |
| **XLS model** | Optional | Required |

## Resources

### references/workflow.md
Detailed Phase 1-5 instructions with step-by-step procedures for data collection, analysis, chart generation, and report creation.

### references/report-structure.md
Complete page-by-page template, table formats, and formatting requirements for the DOCX report.

### references/best-practices.md
Examples of good vs. bad headlines, tips for success, common errors to avoid, and a comprehensive quality checklist.

## Dependencies

**Required:**
- AE composite MCP (openbb) — primary data source for consensus estimates, reported financials, earnings review, and call transcripts
- Python (matplotlib, pandas, seaborn) for chart generation
- DOCX skill for report creation

**Optional:**
- XLS skill for model updates (not required for earnings updates)
