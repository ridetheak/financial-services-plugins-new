# Skills → MCP Interface Call Mapping Table

## Complete Interface Usage Matrix

This document shows which MCP interfaces each skill specifically calls, and the concrete parameters for those calls.

---

## 1. Initiating Coverage (Equity Research)

### Task 1: Company Research

**Primary data needs**: Company background, management, competitive analysis, industry context

```
Call flow:

1. Daloopa.get_company_profile(ticker="AAPL")
   ├─ Returns: Company name, industry, HQ, website, founding year
   └─ Purpose: "Overview" section

2. Daloopa.get_management_team(ticker="AAPL")
   ├─ Returns: CEO, CFO, key executives, bios
   └─ Purpose: "Management & Organization" section

3. Daloopa.get_business_segments(ticker="AAPL")
   ├─ Returns: Major business lines, revenue mix, geographic distribution
   └─ Purpose: "Business Model & Segments" section

4. Daloopa.get_competitive_analysis(ticker="AAPL")
   ├─ Returns: Competitors, market share, competitive advantages
   └─ Purpose: "Competitive Positioning" section

5. S&P Global.get_industry_analysis(sector_code="Technology")
   ├─ Returns: Industry growth rate, industry margins, sector attractiveness
   └─ Purpose: "Industry Outlook" section

6. S&P Global.get_industry_trends(sector_code="Technology")
   ├─ Returns: Latest industry trends, emerging threats, opportunities
   └─ Purpose: "Industry Dynamics" section

7. MT Newswires.get_company_news(ticker="AAPL", limit=20)
   ├─ Returns: Recent news, announcements, publication dates
   └─ Purpose: "Recent News & Updates" section

8. MT Newswires.get_corporate_actions(ticker="AAPL")
   ├─ Returns: Spin-offs, M&A, equity compensation, restructurings
   └─ Purpose: "Corporate Actions" section

9. Aiera.get_earnings_call_calendar(ticker="AAPL")
   ├─ Returns: Next earnings call date and time
   └─ Purpose: "Upcoming Events" section

10. FactSet.get_analyst_estimates(ticker="AAPL", period="FY1")
    ├─ Returns: EPS, revenue, EBITDA estimates
    └─ Purpose: Background context

Output: 6,000–8,000 word research document (Markdown)
```

### Task 2: Financial Modeling

**Primary data needs**: Historical financials, analyst guidance, dividend policy

```
Call flow:

1. Daloopa.get_historical_financials(ticker="AAPL", period=5)
   ├─ Returns: Full financial statements for the past 5 years (revenue, EBIT, net income, etc.)
   └─ Purpose: Historical-year data for the model

2. Daloopa.get_guidance_data(ticker="AAPL")
   ├─ Returns: Management guidance (revenue growth expectations, margin expectations)
   └─ Purpose: Determines growth rate assumptions

3. FactSet.get_analyst_estimates(ticker="AAPL", period=["FY1", "FY2"])
   ├─ Returns: Analyst consensus estimates
   └─ Purpose: Validates reasonableness of growth rates

4. FactSet.get_consensus_estimates(ticker="AAPL")
   ├─ Returns: Market consensus (EPS, revenue, etc.)
   └─ Purpose: Reference for market expectations

5. Morningstar.get_dividend_history(ticker="AAPL", years=10)
   ├─ Returns: Historical dividend amounts, payout ratios, growth rates
   └─ Purpose: Dividend model assumptions

6. Daloopa.get_capital_structure(ticker="AAPL")
   ├─ Returns: Debt, equity, preferred stock, dilution effects
   └─ Purpose: Capital structure analysis

Output: Excel model (6 tabs: historical data, assumptions, projections, three scenarios, sensitivity, summary)
```

### Task 3: Valuation Analysis

**Primary data needs**: Comparable company multiples, industry benchmarks, beta

```
Call flow:

1. Daloopa.search_peer_companies(ticker="AAPL", criteria={
     "sector": "Technology",
     "market_cap_range": [100B, 1T],
     "business_model": "similar"
   })
   ├─ Returns: 10–15 comparable companies
   └─ Purpose: Selects the comparable company universe

2. Daloopa.get_batch_financials(
     tickers=["MSFT", "GOOGL", "META", ...],
     metrics=["revenue", "ebitda", "net_income", "free_cash_flow"]
   )
   ├─ Returns: Batch financial data
   └─ Purpose: Calculates comparable multiples

3. S&P Global.get_valuation_benchmarks(sector="Technology")
   ├─ Returns: Industry average multiples (P/E, EV/EBITDA, P/B)
   └─ Purpose: Comparison against industry benchmarks

4. FactSet.get_current_prices(tickers=["AAPL", "MSFT", ...])
   ├─ Returns: Current stock price, market cap
   └─ Purpose: Multiples denominator calculation

5. FactSet.get_beta(ticker="AAPL")
   ├─ Returns: Stock beta
   └─ Purpose: Risk premium in WACC calculation

6. FactSet.get_risk_free_rate()
   ├─ Returns: Risk-free rate (typically 10-year Treasury yield)
   └─ Purpose: Risk-free rate in WACC calculation

Output: Valuation analysis document + Excel tabs (comparable analysis, DCF, price target)
```

### Task 4: Chart Generation

**Primary data needs**: Time-series data, sector data, benchmark data

```
Call flow:

1. FactSet.get_historical_prices(
     ticker="AAPL",
     start_date="2018-01-01",
     end_date="2024-02-27",
     frequency="daily"
   )
   ├─ Returns: Full historical price series
   └─ Purpose: Charts 1–3 (stock price trend charts)

2. Daloopa.get_historical_financials(ticker="AAPL", period=10)
   ├─ Returns: 10 years of financial data
   └─ Purpose: Charts 4–8 (revenue, EBITDA, margin trends)

3. FactSet.get_analyst_estimates_history(ticker="AAPL")
   ├─ Returns: Historical analyst estimate revisions
   └─ Purpose: Chart 9 (EPS revision trend)

4. Daloopa.get_peer_multiples(
     tickers=["AAPL", "MSFT", "GOOGL", ...],
     multiples=["P/E", "EV/EBITDA", "P/B"]
   )
   ├─ Returns: Comparable company multiples
   └─ Purpose: Charts 10–12 (multiples scatter plots, box plots)

5. S&P Global.get_sector_performance(sector="Technology", period="5Y")
   ├─ Returns: Sector relative performance
   └─ Purpose: Chart 13 (sector relative return)

6. MT Newswires.get_news_volume(ticker="AAPL", months=36)
   ├─ Returns: Monthly news volume trend
   └─ Purpose: Chart 14 (news activity index)

Output: 25–35 PNG/JPG charts
```

---

## 2. DCF Model Builder (Financial Analysis)

### Steps 1–2: Data Retrieval & Historical Analysis

```
Call flow:

1. Daloopa.get_financials(ticker="AAPL", latest_period="LTM")
   ├─ Parameters: ticker, period_type (annual/quarterly), format
   ├─ Returns: Last 12 months (LTM) financial statements
   └─ Priority: ⭐⭐⭐⭐⭐ (most critical)

2. Daloopa.get_historical_financials(ticker="AAPL", years=5)
   ├─ Returns: Annual reports for the past 5 years
   └─ Purpose: Historical growth rate and margin analysis

3. FactSet.get_analyst_estimates(
     ticker="AAPL",
     metrics=["EPS", "Revenue", "EBITDA"],
     periods=["FY1", "FY2"]
   )
   ├─ Returns: Market consensus estimates (1–2 year forward)
   └─ Purpose: Validates growth assumptions

4. FactSet.get_guidance_revisions(ticker="AAPL")
   ├─ Returns: Historical revisions to management guidance
   └─ Purpose: Assesses management forecast accuracy

5. FactSet.get_current_stock_price(ticker="AAPL")
   ├─ Returns: Current stock price
   └─ Purpose: DCF sanity check (current price vs. intrinsic value)

6. FactSet.get_beta(ticker="AAPL")
   ├─ Returns: Stock beta (systematic risk)
   └─ Purpose: Equity risk premium in WACC

7. FactSet.get_risk_free_rate()
   ├─ Returns: 10-year Treasury yield
   └─ Purpose: Risk-free rate in WACC

8. Morningstar.get_dividend_history(ticker="AAPL")
   ├─ Returns: Historical dividend data
   └─ Purpose: Dividend policy analysis

9. Morningstar.get_share_buyback_history(ticker="AAPL")
   ├─ Returns: Historical buyback data
   └─ Purpose: Capital allocation policy analysis

10. Daloopa.get_capital_expenditure_history(ticker="AAPL", years=5)
    ├─ Returns: Capital expenditures for the past 5 years
    └─ Purpose: CapEx % of revenue assumption

Output: Historical metrics summary (revenue CAGR, margin trends, FCF margin)
```

### Steps 3–5: Projections & Valuation

```
Call flow:

1. FactSet.get_industry_growth_rates(sector="Technology")
   ├─ Returns: Industry average growth rate
   └─ Purpose: Validates reasonableness of projected growth rates

2. S&P Global.get_sector_margin_benchmarks(sector="Technology")
   ├─ Returns: Industry average margins
   └─ Purpose: Benchmark for terminal-year assumptions

3. FactSet.get_consensus_terminal_growth_rate()
   ├─ Returns: Market-implied terminal growth rate
   └─ Purpose: Choosing within the 3–5% range

Output: Complete Excel model (financial projections, sensitivity analysis, DCF valuation summary)
```

---

## 3. Comparable Company Analysis (Financial Analysis)

### Core Workflow

```
Call flow:

Step 1: Search for peer companies
1. Daloopa.search_peer_companies(
     ticker="AAPL",
     criteria={
       "sector": "Technology",
       "business_model": "similar",
       "size_range": [50B, 1T]
     }
   )
   ├─ Returns: Peer company list (10–15 companies)
   └─ Purpose: Defines the universe

Step 2: Batch-retrieve financial data
2. Daloopa.get_batch_financials(
     tickers=["MSFT", "GOOGL", "META", "NVDA", ...],
     metrics=["revenue", "gross_profit", "ebitda", "net_income", "fcf"],
     period="LTM"
   )
   ├─ Returns: Financial data for all companies (single call)
   └─ Purpose: Populates the "Operating Metrics" section

3. FactSet.get_batch_current_prices(tickers=[...])
   ├─ Returns: Current market price, market cap
   └─ Purpose: Calculates multiples denominator

Step 3: Retrieve industry benchmarks
4. S&P Global.get_sector_multiples(sector="Technology")
   ├─ Returns: Industry average multiples (P/E, EV/EBITDA, P/B, etc.)
   └─ Purpose: Benchmark row in the "Statistical Summary" section

5. S&P Global.get_sector_margins(sector="Technology")
   ├─ Returns: Industry average margins
   └─ Purpose: Gross margin and EBITDA margin benchmarks

Step 4: Calculate and summarize
6. Local calculation of all multiples
   - P/E = Stock price / EPS
   - EV/EBITDA = (Market cap + Debt - Cash) / EBITDA
   - P/B = Market cap / Book value

Output: Excel comps analysis (company data table, multiples table, statistical summary)
```

**Key implied interfaces**:
- `get_batch_financials()` — retrieves all company data in a single batch (rather than calling one by one)
- `search_peer_companies()` — intelligent search rather than manual entry
- `get_sector_multiples()` — retrieves industry benchmarks rather than computing them manually

---

## 4. Fixed Income Portfolio Analysis (LSEG)

### Core Workflow

```
Call flow:

Step 1: Bond search and pricing
1. LSEG.bond_search(
     criteria={
       "issuer_type": "corporate",
       "rating_range": ["AAA", "BB"],
       "maturity_range": [2, 10],
       "currency": "USD"
     }
   )
   ├─ Returns: List of bonds meeting the criteria
   └─ Purpose: Universe selection (optional, if the user has not provided an existing portfolio)

2. LSEG.bond_price(
     bond_ids=["US0378331005", "US0846701050", ...],
     pricing_date="2024-02-27"
   )
   ├─ Returns: Clean price, dirty price, yield, duration, DV01, OAS
   └─ Purpose: Yield, duration, and DV01 in the "Portfolio Summary" table

Step 2: Reference data and credit analysis
3. LSEG.yieldbook_bond_reference(
     bond_ids=["US0378331005", ...]
   )
   ├─ Returns: Issuer, coupon, maturity date, rating, sector, country
   └─ Purpose: Sector/rating/maturity breakdown in "Composition Breakdown"

4. Moody's.get_credit_rating(bond_id="US0378331005")
   ├─ Returns: Current rating, historical ratings, outlook
   └─ Purpose: Rating analysis and outlook changes

Step 3: Cash flow forecasting
5. LSEG.yieldbook_cashflow(
     bond_ids=["US0378331005", ...],
     projection_years=10
   )
   ├─ Returns: Future cash flow schedule (interest + principal)
   └─ Purpose: "Cashflow Waterfall" table

6. Local aggregation via aggregate_cashflows()
   ├─ Aggregates all bond cash flows into quarterly/annual totals
   └─ Purpose: Portfolio-level cash flow outlook

Step 4: Scenario analysis and stress testing
7. LSEG.yieldbook_scenario(
     bond_ids=["US0378331005", ...],
     scenarios={
       "parallel_shift": [-200, -100, -50, 0, 50, 100, 200],  # basis points
       "curve_scenarios": ["bull_steepen", "bear_steepen", ...]
     }
   )
   ├─ Returns: Price change for each bond under each scenario
   └─ Purpose: "Scenario P&L" table

8. LSEG.interest_rate_curve(
     currency="USD",
     curve_date="2024-02-27"
   )
   ├─ Returns: Complete zero-coupon rate curve
   └─ Purpose: Reference for the benchmark yield curve

Step 5: Risk metrics
9. LSEG.fixed_income_risk_analytics(
     bond_ids=["US0378331005", ...],
     analytics_type=["effective_duration", "key_rate_duration", "convexity"]
   )
   ├─ Returns: Effective duration, key rate duration, convexity
   └─ Purpose: Risk decomposition (which bonds/rate tenors contribute most risk)

Output: PowerPoint or PDF report
```

**Key implied interfaces**:
- `bond_price(batch)` — batch pricing (rather than one at a time)
- `aggregate_cashflows()` — aggregation feature
- `yieldbook_scenario()` — standard scenario library

---

## 5. Buyer List (Investment Banking)

### Core Workflow

```
Call flow:

Step 1: Understand the target company
(User provides: company description, size, sector, geography)

Step 2: Search for strategic buyers
1. Daloopa.search_peer_companies(
     industry=user_industry,
     criteria={
       "market_position": "large",
       "geographic_presence": "global or regional",
       "business_type": ["direct_competitor", "adjacent_player", "vertical_integrator"]
     }
   )
   ├─ Returns: List of potential strategic buyers (30–50 companies)
   └─ Purpose: Strategic buyer universe

2. S&P Global.get_strategic_buyer_database(
     sector=user_sector,
     criteria={"m_a_activity": "active"}
   )
   ├─ Returns: Buyers with M&A activity in the past 12 months
   └─ Purpose: Cross-validation, identifying active buyers

3. PitchBook.strategic_buyer_search(
     target_profile={
       "revenue_range": [X, Y],
       "growth_profile": user_target_growth,
       "synergy_potential": "high"
     }
   )
   ├─ Returns: Strategic buyers identified by PitchBook
   └─ Purpose: Third-party validation

4. Daloopa.get_batch_financials(
     tickers=[all potential buyers],
     metrics=["revenue", "ebitda", "fcf", "net_debt"]
   )
   ├─ Returns: Financial capacity assessment data
   └─ Purpose: Evaluates "Financial Capacity"

Step 3: Search for PE buyers
5. PitchBook.financial_sponsor_search(
     criteria={
       "fund_size": [100M, 5B],
       "sector_focus": [relevant sectors],
       "deal_size_range": [target_revenue_range],
       "investment_stage": "late stage / mature"
     }
   )
   ├─ Returns: List of qualifying PE funds (20–40)
   └─ Purpose: Financial buyer universe

6. Chronograph.get_portfolio_companies(
     sector=user_sector
   )
   ├─ Returns: PE funds' portfolio companies
   └─ Purpose: Identifies add-on acquisition potential

Step 4: M&A history and recent activity
7. MT Newswires.get_m_a_activity(
     buyer_tickers=[all potential buyers],
     period="12M",
     status="completed"
   )
   ├─ Returns: M&A transactions in the past 12 months
   └─ Purpose: "M&A Track Record" column

8. PitchBook.get_comparable_transactions(
     target_profile=user_target,
     period="3Y"
   )
   ├─ Returns: Comparable data for similar transactions
   └─ Purpose: Valuation range and deal structure reference

Step 5: Contact mapping
(Local CRM search + manual research)

Output: Excel buyer list (strategic buyers table, PE buyers table, tier classification, contact mapping)
```

**Key implied interfaces**:
- `search_peer_companies()` — intelligent search
- `search_financial_sponsors()` — PE fund search
- `get_m_a_activity()` — transaction history
- `get_comparable_transactions()` — comparable transactions

---

## 6. Equity Research Snapshot (LSEG)

### Core Workflow

```
Call flow:

1. FactSet.qa_ibes_consensus(
     ticker="AAPL",
     metrics=["EPS", "Revenue", "EBITDA", "DPS"],
     periods=["FY1", "FY2"]
   )
   ├─ Returns: Analyst consensus (median, mean, range, dispersion)
   └─ Purpose: "Consensus Estimates" table

2. FactSet.qa_company_fundamentals(
     ticker="AAPL",
     periods=5  # past 5 fiscal years
   )
   ├─ Returns: Revenue, gross margin, EBIT, ROE, ROIC, etc.
   └─ Purpose: "Financials Summary" table

3. FactSet.qa_historical_equity_price(
     ticker="AAPL",
     period="1Y"
   )
   ├─ Returns: Daily prices, returns, beta, 52-week range
   └─ Purpose: "Price Performance" calculation

4. FactSet.tscc_historical_pricing_summaries(
     ticker="AAPL",
     frequency="daily",
     period="3M"
   )
   ├─ Returns: 3-month daily price summary
   └─ Purpose: Recent volume and momentum analysis

5. LSEG.qa_macroeconomic(
     indicators=["GDP", "CPI", "unemployment"],
     countries=["US", "China"]
   )
   ├─ Returns: Macroeconomic indicators
   └─ Purpose: "Macro Backdrop" section

Output: Research snapshot document
```

---

## Interface Usage Frequency Ranking

Based on skills analysis, the following interfaces are used most frequently:

### Top 20 Most Used Interfaces

| Rank | Interface | Service | No. of Skills Using | Frequency |
|------|-----------|---------|---------------------|-----------|
| 1 | `get_batch_financials()` | Daloopa | 4 | ⭐⭐⭐⭐⭐ |
| 2 | `get_historical_financials()` | Daloopa | 3 | ⭐⭐⭐⭐⭐ |
| 3 | `get_analyst_estimates()` | FactSet | 3 | ⭐⭐⭐⭐⭐ |
| 4 | `search_peer_companies()` | Daloopa | 3 | ⭐⭐⭐⭐⭐ |
| 5 | `get_current_prices()` | FactSet | 3 | ⭐⭐⭐⭐ |
| 6 | `bond_price()` | LSEG | 1 | ⭐⭐⭐⭐⭐ |
| 7 | `get_dividend_history()` | Morningstar | 2 | ⭐⭐⭐⭐ |
| 8 | `get_company_profile()` | Daloopa | 2 | ⭐⭐⭐⭐ |
| 9 | `qa_ibes_consensus()` | FactSet | 2 | ⭐⭐⭐⭐ |
| 10 | `get_business_segments()` | Daloopa | 1 | ⭐⭐⭐ |
| 11 | `yieldbook_scenario()` | LSEG | 1 | ⭐⭐⭐⭐ |
| 12 | `search_financial_sponsors()` | PitchBook | 1 | ⭐⭐⭐ |
| 13 | `get_m_a_activity()` | MT Newswires | 2 | ⭐⭐⭐ |
| 14 | `fixed_income_risk_analytics()` | LSEG | 1 | ⭐⭐⭐ |
| 15 | `get_sector_multiples()` | S&P Global | 2 | ⭐⭐⭐ |
| 16 | `get_beta()` | FactSet | 1 | ⭐⭐⭐ |
| 17 | `yieldbook_bond_reference()` | LSEG | 1 | ⭐⭐⭐ |
| 18 | `get_comparable_transactions()` | PitchBook | 1 | ⭐⭐⭐ |
| 19 | `get_news()` | MT Newswires | 1 | ⭐⭐ |
| 20 | `qa_macroeconomic()` | LSEG | 1 | ⭐⭐⭐ |

**Optimization recommendations**:
- The Top 5 interfaces should have their response time and caching strategy optimized
- Batch interfaces (`get_batch_*`) are used more frequently than single-record interfaces
- These 20 interfaces cover the core functionality of all skills

---

## Interface Dependencies

### Data Flow Diagram

```
User input (Ticker/parameters)
    ↓
[Search] search_peer_companies()
    ↓
[Batch retrieval] get_batch_financials()
    ↓
[Real-time data] get_current_prices()
    ↓
[Reference data] get_sector_multiples(), yieldbook_bond_reference()
    ↓
[Historical data] get_historical_financials(), qa_historical_equity_price()
    ↓
[Calculation interfaces]
├─ Multiples calculation (local)
├─ Statistical summary (local)
├─ Scenario analysis (yieldbook_scenario)
└─ Stress testing (fixed_income_risk_analytics)
    ↓
[Output] Excel / Markdown / PowerPoint
```

---

## Conclusion

**Why this mapping table matters**:

1. **Completeness** — Shows how 99 inferred interfaces are used in actual skills
2. **Priority** — Clearly marks which interfaces are most frequently used
3. **Dependencies** — Understand how interfaces combine with one another
4. **Validation** — Inferences can be verified against actual MCP logs

**Next steps**:
- Validate these inferences by enabling MCP logging
- Compare actual calls against inferred calls
- Optimize response time and caching for high-frequency interfaces
