---
name: sector-overview
description: Create a comprehensive industry and sector landscape report covering market dynamics, competitive positioning, key players, and thematic trends. Use for client requests, sector initiations, thematic research, or internal knowledge building. Trigger when: "sector overview", "industry report", "market landscape", "sector analysis", "industry deep dive", or "thematic research".
---

# Sector Overview

Description: Create a comprehensive industry and sector landscape report covering market dynamics, competitive positioning, key players, and thematic trends. Use for client requests, sector initiations, thematic research, or internal knowledge building. Trigger when: "sector overview", "industry report", "market landscape", "sector analysis", "industry deep dive", or "thematic research".

## Workflow

### Step 1: Define Scope

- **Sector/sub-sector**: What industry and how is it precisely defined?
- **Purpose**: Client report, internal research, pitch materials, idea generation
- **Depth**: High-level overview (5-10 pages) or deep dive (20-30 pages)
- **Angle**: Neutral landscape vs. thematic thesis (e.g., "AI infrastructure buildout")
- **Universe**: Public companies only or include private companies?

### Step 2: Market Overview

**Market Size and Growth**
- Total addressable market (TAM) and source — use `mcp__claude_ai_OpenBB__economy_fred_series` or `mcp__claude_ai_OpenBB__economy_gdp_nominal` for macro context; cite specific industry research firms for sector-specific TAM estimates
- Historical growth rate (5-year CAGR) — pull via `mcp__claude_ai_OpenBB__fmp_historical_sector_performance`
- Projected growth rate and key assumptions
- Market segmentation (by product, geography, end market, customer type)

**Industry Structure**
- Fragmented vs. consolidated — top 5 market share; use `mcp__claude_ai_OpenBB__index_constituents` or `mcp__claude_ai_OpenBB__equity_compare_peers` to identify the key players
- Value chain map — where does value accrue?
- Business model types (subscription, transaction, license, services)
- Barriers to entry (capital, regulatory, technology, network effects)

**Key Trends and Drivers**
- Long-term secular growth trends (3-5 major trends)
- Headwinds and risks
- Technology disruption vectors
- Regulatory developments — check `mcp__claude_ai_OpenBB__news_world` and `mcp__claude_ai_OpenBB__news_company` for recent regulatory filings or announcements
- M&A activity and consolidation trends — `mcp__claude_ai_OpenBB__equity_calendar_earnings` and company news feeds

### Step 3: Competitive Landscape

**Company Profiles** (top 5-10 players). Pull financial data using:
- `mcp__claude_ai_OpenBB__equity_profile` — business description, sector, market cap, CEO
- `mcp__claude_ai_OpenBB__equity_fundamental_metrics` — revenue, margins, EV/EBITDA, P/E, EV/Sales
- `mcp__claude_ai_OpenBB__equity_fundamental_ratios` — profitability and leverage ratios
- `mcp__claude_ai_OpenBB__equity_compare_peers` — side-by-side peer comparison
- `mcp__claude_ai_OpenBB__equity_price_performance` — relative price performance vs. peers
- Fall back to SEC EDGAR 10-K filings for segment detail and qualitative business description

| Company | Revenue | Growth | EBITDA Margin | Market Share | Key Differentiator |
|---------|---------|--------|---------------|-------------|-------------------|
| | | | | | |

For each company, brief profile:
- Business description (2-3 sentences) — from `mcp__claude_ai_OpenBB__equity_profile`
- Strategic positioning and moat
- Recent developments (earnings, M&A, product launches) — from `mcp__claude_ai_OpenBB__news_company`
- Valuation snapshot (P/E, EV/EBITDA, EV/Revenue) — from `mcp__claude_ai_OpenBB__equity_fundamental_metrics`

**Competitive Dynamics**
- How do companies compete? (price, product, service, distribution)
- Who is gaining/losing market share and why?
- Disruption risk from new entrants or adjacent players

### Step 4: Valuation Context

- Sector trading multiples (current and historical range) — use `mcp__claude_ai_OpenBB__fmp_historical_sector_pe` for historical sector P/E; `mcp__claude_ai_OpenBB__equity_fundamental_metrics` for current multiples
- Premium/discount drivers (growth, margins, market position)
- Recent M&A transaction multiples — search `mcp__claude_ai_OpenBB__news_company` for deal announcements; check `mcp__claude_ai_OpenBB__fmp_enterprise_values` for EV context
- How does the sector compare to the broader market? — `mcp__claude_ai_OpenBB__index_sectors` for sector vs. index performance

### Step 5: Investment Implications

- Where is the best risk/reward opportunity? — run `mcp__claude_ai_OpenBB__equity_screener` or `mcp__claude_ai_Interactive_MCP__valuation-context` to surface undervalued names
- What thematic bets can be expressed through this sector?
- Key debates within the sector (bull vs. bear arguments)
- Catalysts that could change the sector narrative

### Step 6: Output

- Word document or PowerPoint containing:
  - Market overview and sizing
  - Competitive landscape map
  - Company comparison table
  - Valuation summary
  - Key charts: market growth, share trends, valuation history
- Excel appendix with detailed company data — source from `mcp__claude_ai_OpenBB__equity_fundamental_metrics` and `mcp__claude_ai_OpenBB__equity_compare_peers`

## Important Notes

- Source all market size data — cite research firms or methodology; use `mcp__claude_ai_OpenBB__economy_fred_series` for macro series, OpenBB tools for company financials
- Distinguish TAM hype from realistic addressable market
- Sector overviews age quickly — date the document and flag data that may be stale
- Charts are essential — market size waterfall, competitive positioning matrix, valuation scatter plot
- If for a client, tailor the "so what" to their specific situation (M&A target identification, competitive positioning, market entry)
