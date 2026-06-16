# MCP Interface Complete Summary Table - AKShare Replacement Reference

## Overview
This table summarizes the interfaces for all MCP services, including interfaces explicitly listed in documentation and implied interfaces inferred by reverse-engineering the Skills. It can serve as a reference for AKShare replacement planning.

---

## 📊 Complete Interface Summary Table

### 1. Daloopa (Financial Data Aggregation)

| Interface | Parameters | Return Fields | Source | Documented/Inferred | AKShare Equivalent | Use Case | Function | Related Skills | Related Plugin |
|-------|------|--------|------|---------|----------|------|------|----------|--------|
| `get_financials()` | ticker, period, format | Revenue, EBIT, net income, assets, liabilities | Daloopa | Documented | `stock_financial_analysis_indicator()` | Retrieve financial statements | Financial data retrieval | Comps, DCF, Initiating | financial-analysis |
| `get_operating_metrics()` | ticker | Gross margin, EBITDA, profit margin | Daloopa | Documented | `stock_main_indicator()` | Retrieve operating metrics | Metric calculation | Comps | financial-analysis |
| `get_batch_financials()` | tickers[], metrics[], period | Batch financial data | Daloopa | Inferred | `stock_zh_a_hist()` + local aggregation | Batch financial retrieval | Multi-company data retrieval | Comps, DCF, Initiating | financial-analysis |
| `get_historical_financials()` | ticker, years | Financial statements for past N years | Daloopa | Inferred | `stock_financial_analysis_indicator()` (historical data) | Historical financial analysis | Trend analysis | DCF, Comps, Initiating | financial-analysis |
| `get_company_profile()` | ticker | Company name, industry, HQ, website, founding year | Daloopa | Inferred | None (requires scraper) | Company basic information | Company profile | Initiating Coverage | equity-research |
| `get_management_team()` | ticker | CEO, CFO, key executives, bios | Daloopa | Inferred | None (requires scraper) | Management team information | Team analysis | Initiating Coverage | equity-research |
| `get_business_segments()` | ticker | Business lines, revenue mix, geographic breakdown | Daloopa | Inferred | None (requires scraper or filings) | Business segment breakdown | Segment analysis | Initiating Coverage | equity-research |
| `get_competitive_analysis()` | ticker | Competitors, market share, competitive advantages | Daloopa | Inferred | None (requires scraper or external data) | Competitive analysis | Competitive assessment | Initiating Coverage | equity-research |
| `search_peer_companies()` | sector, criteria, size_range | List of comparable companies | Daloopa | Inferred | `bk_sina()` + local search | Competitor search | Sample selection | Comps, Buyer List, Initiating | financial-analysis |
| `get_guidance_data()` | ticker | Management revenue growth expectations, margin expectations | Daloopa | Inferred | None (requires scraper) | Management guidance | Growth assumptions | DCF | financial-analysis |
| `get_capital_structure()` | ticker | Debt, equity, preferred stock, dilution effects | Daloopa | Inferred | `stock_main_indicator()` (partial) | Capital structure | WACC calculation | DCF | financial-analysis |
| `get_peer_multiples()` | tickers[] | P/E, EV/EBITDA, P/B, etc. | Daloopa | Inferred | Local calculation (based on financials + price) | Comparable multiples | Multiples analysis | Comps, DCF | financial-analysis |
| `get_capital_expenditure_history()` | ticker, years | CapEx for past N years | Daloopa | Inferred | `stock_cash_flow_sheet()` | CapEx history | Capital investment analysis | DCF | financial-analysis |
| `get_margin_analysis()` | ticker | Gross margin, operating margin, net margin trend | Daloopa | Inferred | Local calculation | Margin analysis | Efficiency analysis | Comps | financial-analysis |
| `get_efficiency_metrics()` | ticker | ROE, ROIC, asset turnover | Daloopa | Inferred | Local calculation | Efficiency metrics | Efficiency assessment | Comps | financial-analysis |
| `get_dividend_policy()` | ticker | Payout ratio, payment history, growth rate | Daloopa | Inferred | `stock_dividend_cninfo()` | Dividend policy | Cash distribution analysis | DCF | financial-analysis |

---

### 2. FactSet (Comprehensive Financial Data)

| Interface | Parameters | Return Fields | Source | Documented/Inferred | AKShare Equivalent | Use Case | Function | Related Skills | Related Plugin |
|-------|------|--------|------|---------|----------|------|------|----------|--------|
| `get_analyst_estimates()` | ticker, metrics, periods | EPS, Revenue, EBITDA estimates | FactSet | Inferred | `stock_main_indicator()` (EPS-related) | Analyst estimates | Market expectations | DCF, Comps, Equity Research | financial-analysis |
| `get_current_prices()` | tickers[] | Current price, market cap | FactSet | Inferred | `stock_zh_a_hist(period='daily')` (latest quote) | Real-time price | Multiples calculation | DCF, Comps, Portfolio | financial-analysis |
| `get_historical_prices()` | ticker, period, frequency | Daily/weekly/monthly price, volume | FactSet | Inferred | `stock_zh_a_hist()` | Historical price | Trend analysis | DCF, Chart Gen | financial-analysis |
| `get_beta()` | ticker | Beta (systematic risk) | FactSet | Inferred | Requires calculation (based on historical returns) | Beta calculation | Risk premium in WACC | DCF | financial-analysis |
| `qa_ibes_consensus()` | ticker, metrics, periods | Analyst consensus (median, mean, range, dispersion) | FactSet | Documented | `stock_main_indicator()` | IBES consensus | Consensus valuation | Equity Research | partner-lseg |
| `qa_company_fundamentals()` | ticker, periods | Revenue, gross margin, EBIT, ROE, ROIC, etc. | FactSet | Documented | `stock_financial_analysis_indicator()` | Company fundamentals | Financial analysis | Equity Research | partner-lseg |
| `qa_historical_equity_price()` | ticker, period | Daily price, returns, beta, 52-week range | FactSet | Documented | `stock_zh_a_hist()` | Historical price | Price analysis | Equity Research | partner-lseg |
| `tscc_historical_pricing_summaries()` | ticker, frequency, period | Daily/weekly/monthly price summaries | FactSet | Documented | `stock_zh_a_hist()` | Price summaries | Volume trends | Equity Research | partner-lseg |
| `get_consensus_estimates()` | ticker | Market consensus estimates | FactSet | Inferred | `stock_main_indicator()` | Consensus estimates | Market expectations | DCF | financial-analysis |
| `get_estimate_revisions()` | ticker | Estimate revision history | FactSet | Inferred | None (requires scraper) | Estimate revisions | Expectation changes | DCF | financial-analysis |
| `get_industry_growth_rates()` | sector | Industry average growth rate | FactSet | Inferred | `bk_sina()` (sector data) | Industry growth | Growth benchmark | DCF | financial-analysis |
| `qa_macroeconomic()` | indicators[], countries[] | GDP, CPI, unemployment, etc. | FactSet | Documented | `macro_china_gdp()`, `macro_china_cpi()`, `macro_china_ppi()` | Macro indicators | Economic context | Equity Research | partner-lseg |

---

### 3. LSEG (Fixed Income, Derivatives, Macro)

| Interface | Parameters | Return Fields | Source | Documented/Inferred | AKShare Equivalent | Use Case | Function | Related Skills | Related Plugin |
|-------|------|--------|------|---------|----------|------|------|----------|--------|
| `bond_price()` | bond_ids[], pricing_date | Clean price, dirty price, yield, duration, DV01, OAS | LSEG | Documented | `bond_sina()`, `convertible_bond_sina()` | Bond pricing | Bond valuation | Fixed Income Portfolio | partner-lseg |
| `yieldbook_bond_reference()` | bond_ids[] | Issuer, coupon, maturity, rating, sector | LSEG | Documented | None (requires scraper or external data) | Bond reference data | Bond information | Fixed Income Portfolio | partner-lseg |
| `yieldbook_cashflow()` | bond_ids[], projection_years | Future cash flow schedule (interest + principal) | LSEG | Documented | None (requires calculation) | Cash flow projection | Cash flow analysis | Fixed Income Portfolio | partner-lseg |
| `yieldbook_scenario()` | bond_ids[], scenarios | Price changes under each scenario | LSEG | Documented | None (requires calculation) | Scenario analysis | Stress testing | Fixed Income Portfolio | partner-lseg |
| `interest_rate_curve()` | currency, curve_date | Complete zero-coupon rate curve | LSEG | Documented | None (can use treasury yields) | Rate curve | Reference curve | Fixed Income Portfolio | partner-lseg |
| `fixed_income_risk_analytics()` | bond_ids[], analytics_type | Effective duration, key rate duration, convexity | LSEG | Documented | None (requires calculation) | Risk metrics | Risk decomposition | Fixed Income Portfolio | partner-lseg |
| `bond_search()` | criteria{} | List of bonds matching criteria | LSEG | Inferred | `bond_sina()` (filtered) | Bond search | Sample selection | Fixed Income Portfolio | partner-lseg |
| `portfolio_duration_calculation()` | bond_ids[], weights[] | Portfolio duration | LSEG | Inferred | Local calculation | Duration calculation | Portfolio analysis | Fixed Income Portfolio | partner-lseg |
| `stress_test_parallel_shock()` | bond_ids[], shock_amounts[] | P&L under parallel shift | LSEG | Inferred | Local calculation | Parallel shock | Stress testing | Fixed Income Portfolio | partner-lseg |
| `curve_scenario_analysis()` | bond_ids[], scenarios[] | P&L under curve scenarios | LSEG | Inferred | Local calculation | Curve scenarios | Scenario analysis | Fixed Income Portfolio | partner-lseg |
| `option_pricing()` | option_params{} | Option price, Greeks | LSEG | Inferred | `stock_option_sina()` (option quotes) | Option pricing | Derivatives valuation | Derivatives-related Skills | partner-lseg |
| `volatility_surface()` | underlying, currency | Volatility surface | LSEG | Inferred | None (requires calculation) | Volatility surface | Pricing parameters | Derivatives Skills | partner-lseg |
| `option_greeks()` | option_id | Delta, Gamma, Vega, Theta, Rho | LSEG | Inferred | None (requires calculation) | Option Greeks | Risk management | Derivatives Skills | partner-lseg |
| `swap_pricing()` | swap_params{} | Swap price, spread | LSEG | Inferred | None (requires calculation or external data) | Swap pricing | Derivatives valuation | Derivatives Skills | partner-lseg |
| `macro_gdp()` | country, period | GDP data, growth rate | LSEG | Inferred | `macro_china_gdp()` | GDP data | Macro analysis | Equity Research, DCF | partner-lseg |
| `macro_inflation()` | country, indicator_type | Inflation data | LSEG | Inferred | `macro_china_cpi()`, `macro_china_ppi()` | Inflation indicators | Macro analysis | Equity Research | partner-lseg |
| `macro_rates_data()` | country | Central bank rates, monetary policy | LSEG | Inferred | None (can use treasury yields) | Interest rate data | Macro context | Portfolio Rebalance | partner-lseg |

---

### 4. S&P Global (Valuation, Sectors)

| Interface | Parameters | Return Fields | Source | Documented/Inferred | AKShare Equivalent | Use Case | Function | Related Skills | Related Plugin |
|-------|------|--------|------|---------|----------|------|------|----------|--------|
| `get_sector_multiples()` | sector | Sector average multiples (P/E, EV/EBITDA, P/B) | S&P Global | Inferred | Local calculation (based on sector companies) | Sector multiples | Multiples benchmark | Comps, DCF | financial-analysis |
| `get_valuation_benchmarks()` | sector, metrics[] | Valuation benchmarks | S&P Global | Inferred | Local calculation | Valuation benchmarks | Multiples reference | Comps, DCF | financial-analysis |
| `get_industry_analysis()` | sector_code | Industry growth rate, margins, attractiveness | S&P Global | Inferred | `bk_sina()`, `bk_sina_members()` | Industry analysis | Industry understanding | Initiating Coverage | equity-research |
| `get_industry_trends()` | sector_code | Industry trends, threats, opportunities | S&P Global | Inferred | None (requires scraper or reports) | Industry trends | Trend identification | Initiating Coverage | equity-research |
| `get_industry_classification()` | ticker, classification_type | Industry classification codes | S&P Global | Inferred | `bk_sina()` | Industry classification | Classification coding | Comps, Buyer List | financial-analysis |
| `get_strategic_buyer_database()` | sector, criteria | Strategic buyer list | S&P Global | Inferred | None (requires scraper or PitchBook) | Buyer database | Buyer search | Buyer List | investment-banking |
| `get_sector_performance()` | sector, period | Sector relative performance, returns | S&P Global | Inferred | Local calculation (based on sector companies) | Sector performance | Relative returns | Initiating Coverage | equity-research |
| `get_sector_margins()` | sector | Sector average margins | S&P Global | Inferred | Local calculation | Sector margins | Margin benchmark | Comps | financial-analysis |
| `sector_overview()` | sector_code | Sector overview data | S&P Global | Inferred | `bk_sina()` | Sector overview | Basic information | Sector Overview Skill | partner-spglobal |

---

### 5. Morningstar (Investment Data)

| Interface | Parameters | Return Fields | Source | Documented/Inferred | AKShare Equivalent | Use Case | Function | Related Skills | Related Plugin |
|-------|------|--------|------|---------|----------|------|------|----------|--------|
| `get_dividend_history()` | ticker, years | Dividend amount, payment date, payout ratio | Morningstar | Inferred | `stock_dividend_cninfo()` | Dividend history | Dividend analysis | DCF, Comps | financial-analysis |
| `get_dividend_policy()` | ticker | Payout ratio, policy, growth rate | Morningstar | Inferred | None (requires calculation) | Dividend policy | Dividend forecasting | DCF | financial-analysis |
| `get_fund_ratings()` | fund_id | Fund rating, risk level | Morningstar | Inferred | None (requires scraper) | Fund rating | Fund assessment | Portfolio Rebalance | wealth-management |
| `get_fund_holdings()` | fund_id | Fund holdings list | Morningstar | Inferred | None (requires scraper) | Fund holdings | Holdings analysis | Portfolio Rebalance | wealth-management |
| `get_fundamental_analysis()` | ticker | Fundamental data | Morningstar | Inferred | `stock_financial_analysis_indicator()` | Fundamental analysis | Financial analysis | Equity Research | partner-lseg |
| `get_valuation_snapshot()` | ticker | Valuation snapshot data | Morningstar | Inferred | `stock_valuation()` | Valuation snapshot | Valuation reference | Equity Research | partner-lseg |

---

### 6. MT Newswires (News)

| Interface | Parameters | Return Fields | Source | Documented/Inferred | AKShare Equivalent | Use Case | Function | Related Skills | Related Plugin |
|-------|------|--------|------|---------|----------|------|------|----------|--------|
| `get_company_news()` | ticker, limit, date_range | News headlines, timestamps, summaries | MT Newswires | Inferred | `guba_sina()` | Company news | News aggregation | Initiating Coverage | equity-research |
| `get_earnings_announcements()` | ticker | Earnings announcements, dates, highlights | MT Newswires | Inferred | None (requires scraper) | Earnings announcements | Announcement retrieval | Initiating Coverage | equity-research |
| `get_corporate_actions()` | ticker | Spinoffs, M&A, equity incentives, restructurings | MT Newswires | Inferred | None (requires scraper) | Corporate actions | Material events | Initiating Coverage | equity-research |
| `get_news_sentiment()` | ticker, timeframe | News sentiment score | MT Newswires | Inferred | None (requires NLP) | News sentiment | Sentiment analysis | Equity Research | partner-lseg |
| `get_m_a_activity()` | buyer_tickers[], period, status | M&A transaction list | MT Newswires | Inferred | None (requires scraper or database) | M&A activity | Transaction history | Buyer List | investment-banking |
| `get_company_mentions()` | search_terms | Company mention data | MT Newswires | Inferred | None (requires scraper) | Company mentions | Search results | Deal Sourcing | private-equity |

---

### 7. Aiera (Event-Driven)

| Interface | Parameters | Return Fields | Source | Documented/Inferred | AKShare Equivalent | Use Case | Function | Related Skills | Related Plugin |
|-------|------|--------|------|---------|----------|------|------|----------|--------|
| `get_earnings_call_schedule()` | ticker | Call date, time, registration link | Aiera | Inferred | None (requires scraper) | Earnings calls | Event calendar | Initiating Coverage | equity-research |
| `get_conference_attendance()` | ticker | List of attended conferences | Aiera | Inferred | None (requires scraper) | Conference attendance | Attendance information | Initiating Coverage | equity-research |
| `get_earnings_call_calendar()` | sector, date_range | Earnings call calendar | Aiera | Inferred | None (requires scraper) | Call calendar | Event calendar | Equity Research | partner-lseg |
| `get_event_catalysts()` | ticker | Event catalyst list | Aiera | Inferred | None (requires scraper or analysis) | Event catalysts | Catalyst identification | Equity Research | partner-lseg |

---

### 8. PitchBook (M&A/PE Data)

| Interface | Parameters | Return Fields | Source | Documented/Inferred | AKShare Equivalent | Use Case | Function | Related Skills | Related Plugin |
|-------|------|--------|------|---------|----------|------|------|----------|--------|
| `search_strategic_buyers()` | target_profile | Strategic buyer list | PitchBook | Inferred | None (requires scraper) | Buyer search | Strategic buyer identification | Buyer List | investment-banking |
| `search_financial_sponsors()` | criteria{} | PE fund list | PitchBook | Inferred | None (requires scraper or database) | PE search | Financial sponsor identification | Buyer List | investment-banking |
| `get_m_a_transaction_history()` | buyer_tickers[], period | M&A transaction history | PitchBook | Inferred | None (requires scraper) | Transaction history | Buyer activity record | Buyer List | investment-banking |
| `get_comparable_transactions()` | target_profile, period | Comparable transaction data | PitchBook | Inferred | None (requires scraper or database) | Comparable transactions | Transaction multiples reference | Buyer List, Deal Sourcing | investment-banking |
| `search_target_companies()` | criteria{} | Target company list | PitchBook | Inferred | None (requires scraper) | Target search | Potential target identification | Deal Sourcing | private-equity |
| `get_buyer_activity()` | buyer_id, period | Buyer activity analysis | PitchBook | Inferred | None (requires scraper) | Buyer activity | Buyer analysis | Buyer List | investment-banking |
| `get_pe_transaction_database()` | filters{} | PE transaction database | PitchBook | Inferred | None (requires scraper or database) | PE transaction database | PE transaction reference | PE IC Memo | private-equity |
| `get_deal_multiples()` | sector, deal_type | Deal multiples | PitchBook | Inferred | Local calculation | Deal multiples | Multiples benchmark | PE Deal Screening | private-equity |

---

### 9. Chronograph (PE Data)

| Interface | Parameters | Return Fields | Source | Documented/Inferred | AKShare Equivalent | Use Case | Function | Related Skills | Related Plugin |
|-------|------|--------|------|---------|----------|------|------|----------|--------|
| `get_portfolio_company_metrics()` | portfolio_id | Portfolio company metrics | Chronograph | Inferred | None (requires external data) | Portfolio metrics | Portfolio monitoring | PE Portfolio Monitoring | private-equity |
| `get_fund_performance()` | fund_id | Fund performance data | Chronograph | Inferred | None (requires scraper) | Fund performance | Performance tracking | PE Returns Analysis | private-equity |
| `get_investment_returns()` | investment_id | Investment return data | Chronograph | Inferred | None (requires calculation) | Investment returns | Returns analysis | PE Returns Analysis | private-equity |
| `get_portfolio_tracking()` | portfolio_id | Portfolio tracking | Chronograph | Inferred | None (requires external system) | Portfolio tracking | Ongoing monitoring | PE Value Creation Plan | private-equity |

---

### 10. Moody's (Credit Ratings)

| Interface | Parameters | Return Fields | Source | Documented/Inferred | AKShare Equivalent | Use Case | Function | Related Skills | Related Plugin |
|-------|------|--------|------|---------|----------|------|------|----------|--------|
| `get_credit_rating()` | bond_id/issuer | Credit rating, rating date | Moody's | Inferred | None (requires scraper) | Credit rating | Credit analysis | Fixed Income Portfolio | partner-lseg |
| `get_rating_history()` | issuer | Rating change history | Moody's | Inferred | None (requires scraper) | Rating history | Rating trend | Fixed Income Portfolio | partner-lseg |
| `get_outlook_change()` | issuer | Rating outlook changes | Moody's | Inferred | None (requires scraper) | Rating outlook | Outlook monitoring | Fixed Income Portfolio | partner-lseg |

---

### 11. Egnyte (File Management)

| Interface | Parameters | Return Fields | Source | Documented/Inferred | AKShare Equivalent | Use Case | Function | Related Skills | Related Plugin |
|-------|------|--------|------|---------|----------|------|------|----------|--------|
| `save_file()` | filepath, content, format | File save result | Egnyte | Inferred | None (local storage) | File save | Output saving | All Skills | All plugins |
| `upload_document()` | document, folder | Upload result | Egnyte | Inferred | None (local storage) | Document upload | File management | All Skills | All plugins |
| `create_folder()` | folder_path | Folder creation result | Egnyte | Inferred | None (local storage) | Folder creation | Directory management | All Skills | All plugins |
| `list_files()` | folder_path | File list | Egnyte | Inferred | None (local storage) | File list | Browse management | All Skills | All plugins |
| `share_document()` | file_id, users[] | Sharing result | Egnyte | Inferred | None (local storage) | Document sharing | Permission management | All Skills | All plugins |

---

## 📈 Summary Statistics

### By Source

| Source | Documented | Inferred from Skills | Total |
|------|---------|----------|------|
| **Daloopa** | 2 | 14 | 16 |
| **FactSet** | 4 | 8 | 12 |
| **LSEG** | 6 | 12 | 18 |
| **S&P Global** | 0 | 9 | 9 |
| **Morningstar** | 0 | 6 | 6 |
| **MT Newswires** | 0 | 6 | 6 |
| **Aiera** | 0 | 4 | 4 |
| **PitchBook** | 0 | 8 | 8 |
| **Chronograph** | 0 | 4 | 4 |
| **Moody's** | 0 | 3 | 3 |
| **Egnyte** | 0 | 5 | 5 |
| **Total** | **12** | **79** | **91** |

### By AKShare Replacement Status

| Replacement Status | Interface Count | Share | AKShare Interfaces |
|---------|-------|------|-----------|
| **Full replacement** | 18 | 20% | stock_financial_analysis_indicator, stock_zh_a_hist, stock_dividend_cninfo, etc. |
| **Partial replacement (local calculation required)** | 25 | 27% | Local calculations based on AKShare data |
| **Partial replacement (scraper required)** | 32 | 35% | News, announcements, management information, etc. |
| **No replacement available** | 16 | 18% | M&A data, PE data, detailed bond information, etc. |

---

## 🎯 Statistics by Skill

| Skill | Interface Count | Primary MCP Services |
|------|-------|-----------|
| **Initiating Coverage** | 18 | Daloopa, FactSet, S&P Global, MT News, Aiera |
| **DCF Model Builder** | 15 | FactSet, Daloopa, Morningstar |
| **Comps Analysis** | 12 | Daloopa, FactSet, S&P Global |
| **Fixed Income Portfolio** | 11 | LSEG, Moody's |
| **Buyer List** | 10 | Daloopa, PitchBook, MT News, S&P Global |
| **Equity Research (LSEG)** | 9 | FactSet, LSEG |
| **Portfolio Rebalance** | 8 | FactSet, Morningstar |
| **Deal Sourcing** | 7 | Daloopa, MT News, PitchBook |
| **PE/Portfolio related** | 8 | PitchBook, Chronograph |

---

## 💡 AKShare Replacement Priority

### First Priority (Full Replacement — Act Now)

```
✅ get_batch_financials()        → ak.stock_financial_analysis_indicator()
✅ get_historical_financials()  → ak.stock_financial_analysis_indicator()
✅ get_dividend_history()        → ak.stock_dividend_cninfo()
✅ bond_price()                  → ak.bond_sina()
✅ get_current_prices()          → ak.stock_zh_a_hist()
✅ get_sector_multiples()        → local calculation (based on bk_sina)
```

### Second Priority (Partial Replacement — Supplement Required)

```
⚠️ get_analyst_estimates()       → ak.stock_main_indicator() (supplement other valuations)
⚠️ qa_ibes_consensus()           → ak.stock_main_indicator()
⚠️ search_peer_companies()       → ak.bk_sina() (requires local search engine)
⚠️ yieldbook_cashflow()          → local calculation
⚠️ get_beta()                    → local calculation (based on historical returns)
```

### Third Priority (Requires Scraper or External Data)

```
❌ get_company_news()            → requires scraper guba_sina() or other news source
❌ get_corporate_actions()       → requires scraper or Xueqiu API
❌ get_management_team()         → requires scraper or external data
❌ get_m_a_activity()            → requires professional M&A database
❌ get_earnings_call_schedule()  → requires scraper
```

---

## 🔗 Related Analysis Documents

- **ACTUAL_INTERFACES_INFERRED_CN.md** - Detailed interface inference analysis
- **SKILLS_TO_APIS_MAPPING_CN.md** - Skills to API call flow mapping
- **SKILLS_INFERENCE_QUICK_GUIDE.md** - Quick reference and usage guide
- **MCP_SERVICES_AKSHARE_MAPPING_CN.md** - AKShare mapping details

---

## 📝 Usage Notes

1. **Fully replaceable interfaces** - Can be directly replaced with AKShare; no additional processing required
2. **Partially replaceable interfaces** - Require local calculation or data aggregation on top of AKShare
3. **Interfaces requiring scrapers** - Require building a scraper system or calling other free APIs
4. **Irreplaceable interfaces** - Retain original MCP service or find paid alternatives

---

**Last updated**: February 27, 2026
**Total interfaces**: 91
**AKShare direct replacement**: 18 (20%)
**AKShare indirect replacement**: 25 (27%)
**Interfaces requiring supplementation**: 48 (53%)
