---
name: idea-generation
description: Systematic stock screening and investment idea sourcing. Combines quantitative screening, thematic research, and pattern recognition to surface new long and short ideas. Use when looking for new ideas, running screens, or doing thematic scans. Trigger when: "idea generation", "stock screen", "find ideas", "what looks interesting", "screen", "new ideas", or "give me recommendations".
---

# Idea Generation

Description: Systematic stock screening and investment idea sourcing. Combines quantitative screening, thematic research, and pattern recognition to surface new long and short ideas. Use when looking for new ideas, running screens, or doing thematic scans. Trigger when: "idea generation", "stock screen", "find ideas", "what looks interesting", "screen", "new ideas", or "give me recommendations".

## Workflow

### Step 1: Define Search Criteria

Ask the user for parameters:
- **Direction**: Long ideas, short ideas, or both
- **Market cap**: Large-cap, mid-cap, small-cap, micro-cap
- **Sector**: Specific sector or cross-sector
- **Style**: Value, growth, quality, special situations, event-driven
- **Geography**: US, international, global
- **Theme**: Any specific thematic angle (AI, reshoring, aging demographics, etc.)

### Step 2: Quantitative Screening

Run screens based on style. Use AE composite MCP (openbb) as primary data source for screening metrics; fall back to SEC EDGAR filings or Yahoo Finance:

**Value Screen**
- P/E below sector median
- EV/EBITDA below historical average
- Free cash flow yield >5%
- Price/book below 1.5x
- Insider buying in past 90 days
- Dividend yield above market average

**Growth Screen**
- Revenue YoY growth >15%
- EPS YoY growth >20%
- Revenue acceleration (growth rate increasing)
- Expanding margins
- High ROIC (>15%)
- Strong net retention (SaaS >110%)

**Quality Screen**
- Consistent revenue growth (5+ years)
- Stable or expanding margins
- ROE >15%
- Low debt/equity ratio
- High free cash flow conversion
- Insider ownership >5%

**Short Screen**
- Declining revenue or growth deceleration
- Margin compression
- Rising receivables/inventory relative to sales
- Insider selling
- Valuation premium vs. peers without justification
- High short interest but deteriorating fundamentals
- Accounting red flags (auditor change, restatements)

**Special Situations Screen**
- Recent IPO/SPAC with lockup expiration approaching
- Spinoffs in past 12 months
- Companies emerging from restructuring
- Activist shareholder involvement
- Management changes at underperforming companies

### Step 3: Thematic Scan

For thematic ideas, research the theme and identify beneficiaries:

1. Define the thesis (e.g., "AI infrastructure spending acceleration through 2026 and beyond")
2. Map the value chain — who benefits directly, who indirectly?
3. Identify pure plays vs. diversified exposures
4. Assess which names are already "priced in" vs. underpriced
5. Look for second-order beneficiaries the market has not yet connected to the theme

### Step 4: Idea Presentation

For each idea passing screening, show:

**[Company Name] — [Long/Short] — [One-sentence thesis]**

| Metric | Value | vs. Peers |
|--------|-------|-----------|
| Market cap | | |
| EV/EBITDA (NTM) | | |
| P/E (NTM) | | |
| Revenue growth | | |
| EBITDA margin | | |
| FCF yield | | |

**Thesis (3-5 bullet points):**
- Why it is mispriced
- What the market is missing
- Catalysts to realize value

**Key Risks:**
- What would make this idea wrong

**Suggested Next Steps:**
- Build a full model? Deep-dive diligence? Expert call?

### Step 5: Output

- Short list of 5-10 ideas with a one-page summary each
- Documented screening criteria and methodology
- Comparison table across all ideas
- Priority list: which ideas to research first

## Important Notes

- Screens produce candidates, not conclusions — every screen output requires fundamental work
- The best ideas often come from intersections (e.g., quality company appearing at value price due to a short-term headwind)
- Avoid crowded trades — check ownership data, short interest, and how many analysts cover the name
- Contrarian ideas require higher conviction — timing is harder and the risk is asymmetric
- Track idea success rate over time — which screens and approaches generate the best ideas?
- Short ideas require higher conviction — timing is harder and the risk is asymmetric
