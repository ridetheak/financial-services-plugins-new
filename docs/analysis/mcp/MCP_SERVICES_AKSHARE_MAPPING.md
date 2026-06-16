# MCP Service API Interface Analysis and AKShare Mapping

## Overview

This document provides a detailed analysis of the specific API interfaces for 11 MCP services and their corresponding AKShare equivalents.

---

## 1. Daloopa

### Service Information
- **URL**: `https://mcp.daloopa.com/server/mcp`
- **Type**: HTTP MCP
- **Primary function**: Financial data aggregation platform integrating financial data for publicly listed companies globally

### API Interfaces Provided
```
GET /financials/{company_id}              # Retrieve company financial data (P&L, BS, CF)
GET /metrics/{company_id}                  # Retrieve key financial metrics
GET /competitors/{company_id}              # Retrieve competitor analysis
GET /guidance/{company_id}                 # Retrieve management guidance
GET /segments/{company_id}                 # Retrieve segment data
GET /historical/{company_id}               # Retrieve historical financial data
```

### Corresponding AKShare APIs

| Function | Daloopa API | AKShare Equivalent | Notes |
|------|-----------|-------------------|------|
| Listed company financial statements | `/financials/{company_id}` | `stock_financial_analysis_indicator` | Financial statement metrics |
| Quarterly/annual reports | `/financials/{company_id}` | `stock_main_indicator` | Key financial indicators |
| Competitor analysis | `/competitors/{company_id}` | Must be assembled manually | No direct equivalent for A-shares |
| Management guidance | `/guidance/{company_id}` | No direct equivalent | Must be scraped from announcements |
| Business segment data | `/segments/{company_id}` | `stock_main_indicator` | Partially disclosed in earnings reports |
| Historical financial data | `/historical/{company_id}` | `stock_main_indicator` (historical) | Supports multi-period comparison |

### Implementation
```python
# AKShare replacement
import akshare as ak

# Get financial statements
df = ak.stock_financial_analysis_indicator(symbol="000001", indicator="Basic EPS")

# Get key indicators
df = ak.stock_main_indicator(symbol="000001")

# Get earnings flash report
df = ak.guba_sina(show_params=False)
```

---

## 2. Morningstar

### Service Information
- **URL**: `https://mcp.morningstar.com/mcp`
- **Type**: HTTP MCP
- **Primary function**: Investment research data, fund ratings, stock ratings

### API Interfaces Provided
```
GET /fund/profile/{fund_id}                # Fund profile
GET /fund/rating/{fund_id}                 # Fund rating
GET /stock/rating/{ticker}                 # Stock rating
GET /equity/dividend/{ticker}              # Dividend history
GET /equity/earnings-estimate/{ticker}     # Earnings estimates
GET /portfolio/{portfolio_id}              # Portfolio analysis
```

### Corresponding AKShare APIs

| Function | Morningstar API | AKShare Equivalent | Notes |
|------|-----------------|-----------------|------|
| Stock ratings | `/stock/rating/{ticker}` | No direct equivalent | Can be obtained from research reports |
| Dividend history | `/equity/dividend/{ticker}` | `stock_dividend_cninfo` | A-share dividend information |
| Earnings estimates | `/equity/earnings-estimate/{ticker}` | `bk_hk_sina` | No direct estimate data |
| Fund information | `/fund/profile/{fund_id}` | `fund_info` | Fund basic information |
| Fund ratings | `/fund/rating/{fund_id}` | No direct equivalent | Must be scraped from third parties |

### Implementation
```python
import akshare as ak

# Get dividend information
df = ak.stock_dividend_cninfo(symbol="000001")

# Get fund basic information
df = ak.fund_info()

# Get fund NAV history
df = ak.fund_daily_history(symbol="110022")

# Get fund holdings
df = ak.fund_portfolio_detail_rank(symbol="110022", date="20231231")
```

---

## 3. S&P Global (Kensho)

### Service Information
- **URL**: `https://kfinance.kensho.com/integrations/mcp`
- **Type**: HTTP MCP
- **Primary function**: Industry analysis, valuation tools, company tear sheets, earnings previews

### API Interfaces Provided
```
GET /company/profile/{isin}                # Company profile
GET /industry/overview/{sector}            # Industry overview
GET /valuation/multiples/{ticker}          # Valuation multiples
GET /earnings/estimates/{ticker}           # Earnings estimates
GET /dividends/{ticker}                    # Dividend information
GET /peer-comparison/{ticker}              # Peer comparison
```

### Corresponding AKShare APIs

| Function | S&P Global API | AKShare Equivalent | Notes |
|------|---------------|------------------|------|
| Company profile | `/company/profile/{isin}` | No direct equivalent | Can be scraped from Eastmoney |
| Industry overview | `/industry/overview/{sector}` | `bk_sina` | Sina industry classification |
| Valuation multiples | `/valuation/multiples/{ticker}` | `stock_valuation` | Valuation multiples data |
| Earnings estimates | `/earnings/estimates/{ticker}` | No direct equivalent | Must be scraped from broker research |
| Peer comparison | `/peer-comparison/{ticker}` | Must be assembled manually | Can use bk data |

### Implementation
```python
import akshare as ak

# Get valuation data (PE, PB, etc.)
df = ak.stock_valuation()

# Get industry information
df = ak.bk_sina()

# Get industry constituents
df = ak.bk_sina_members(symbol="bk0471")

# Get basic stock information
df = ak.stock_info_a_sina()
```

---

## 4. FactSet

### Service Information
- **URL**: `https://mcp.factset.com/mcp`
- **Type**: HTTP MCP
- **Primary function**: Comprehensive financial data, analytical tools, market data

### API Interfaces Provided
```
GET /fundamentals/{ticker}                 # Fundamental financial data
GET /timeseries/{ticker}                   # Time series data
GET /ratios/{ticker}                       # Financial ratios
GET /statements/{ticker}                   # Financial statements
GET /segments/{ticker}                     # Segment data
GET /transcripts/{ticker}                  # Earnings call transcripts
```

### Corresponding AKShare APIs

| Function | FactSet API | AKShare Equivalent | Notes |
|------|-----------|-------------------|------|
| Financial data | `/fundamentals/{ticker}` | `stock_financial_analysis_indicator` | Comprehensive financial data |
| Time series | `/timeseries/{ticker}` | `stock_zh_a_hist` | Historical price data |
| Financial ratios | `/ratios/{ticker}` | `stock_main_indicator` | Various financial ratios |
| Financial statements | `/statements/{ticker}` | `stock_financial_analysis_indicator` | Three financial statements |
| Segment data | `/segments/{ticker}` | `stock_main_indicator` | Needs extraction |
| Earnings call transcripts | `/transcripts/{ticker}` | No equivalent | Available for only some A-share companies |

### Implementation
```python
import akshare as ak

# Get all financial indicators
df = ak.stock_financial_analysis_indicator(symbol="000001")

# Get key indicators (including ratios)
df = ak.stock_main_indicator(symbol="000001")

# Get historical prices
df = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20200101", end_date="20231231")

# Get cash flow
df = ak.stock_cash_flow_sheet(symbol="000001")
```

---

## 5. Moody's

### Service Information
- **URL**: `https://api.moodys.com/genai-ready-data/m1/mcp`
- **Type**: HTTP MCP
- **Primary function**: Credit ratings, default risk, bond analysis

### API Interfaces Provided
```
GET /rating/{issuer_id}                    # Credit rating
GET /credit-risk/{issuer_id}               # Credit risk metrics
GET /default-probability/{issuer_id}       # Default probability
GET /bond-analysis/{bond_isin}             # Bond analysis
GET /sector-rating/{sector}                # Sector rating outlook
```

### Corresponding AKShare APIs

| Function | Moody's API | AKShare Equivalent | Notes |
|------|-----------|------------------|------|
| Credit rating | `/rating/{issuer_id}` | No equivalent | A-share ratings must be scraped |
| Credit risk | `/credit-risk/{issuer_id}` | `stock_concept_sina` | Needs to be combined with liquidity data |
| Default probability | `/default-probability/{issuer_id}` | No equivalent | Bond market only |
| Bond analysis | `/bond-analysis/{bond_isin}` | `bond_*` related | Bond data interfaces |
| Sector rating | `/sector-rating/{sector}` | `bk_sina` | Basic industry data |

### Implementation
```python
import akshare as ak

# Get bond data
df = ak.bond_sina()

# Get bond basic information
df = ak.bond_info_sina()

# Get convertible bond data
df = ak.convertible_bond_sina()
```

---

## 6. MT Newswires

### Service Information
- **URL**: `https://vast-mcp.blueskyapi.com/mtnewswires`
- **Type**: HTTP MCP
- **Primary function**: Financial news, market developments, company announcements

### API Interfaces Provided
```
GET /news/{ticker}                         # Stock news
GET /breaking-news                         # Breaking news
GET /news-feed/{source}                    # News feed subscription
GET /earnings-reports/{ticker}             # Earnings reports
GET /corporate-actions/{ticker}            # Corporate actions (M&A, etc.)
```

### Corresponding AKShare APIs

| Function | MT Newswires API | AKShare Equivalent | Notes |
|------|-----------------|-----------------|------|
| Stock news | `/news/{ticker}` | `guba_sina` | Stock forum content and news |
| Breaking news | `/breaking-news` | No direct equivalent | Must be implemented with a scraper |
| Earnings reports | `/earnings-reports/{ticker}` | `guba_sina` | Obtained from announcements |
| Corporate actions | `/corporate-actions/{ticker}` | `stock_main_indicator` | Dividends, stock splits, etc. |

### Implementation
```python
import akshare as ak

# Get stock forum news
df = ak.guba_sina(show_params=False)

# Get dividend and stock split information
df = ak.stock_dividend_cninfo(symbol="000001")

# Get rights issue and additional offering information
df = ak.stock_allocation_cninfo(symbol="000001")
```

---

## 7. Aiera

### Service Information
- **URL**: `https://mcp-pub.aiera.com`
- **Type**: HTTP MCP
- **Primary function**: Event-driven intelligence, earnings calls, catalyst analysis

### API Interfaces Provided
```
GET /events/{ticker}                       # Company event calendar
GET /earnings-calls/{ticker}               # Earnings calls
GET /catalysts/{ticker}                    # Catalyst events
GET /event-transcript/{event_id}           # Event transcripts
GET /sentiment/{ticker}                    # Sentiment analysis
```

### Corresponding AKShare APIs

| Function | Aiera API | AKShare Equivalent | Notes |
|------|----------|------------------|------|
| Event calendar | `/events/{ticker}` | No direct equivalent | No unified calendar for A-shares |
| Earnings calls | `/earnings-calls/{ticker}` | No equivalent | Available for only some companies |
| Catalysts | `/catalysts/{ticker}` | Must be built manually | Use earnings reports and announcements |
| Sentiment analysis | `/sentiment/{ticker}` | `guba_sina` | Can be used for NLP analysis |

### Implementation
```python
import akshare as ak

# Get financial calendar information
df = ak.stock_zh_a_hist(symbol="000001")  # Includes suspension/resumption info

# Get stock forum comments (for sentiment analysis)
df = ak.guba_sina()

# Get research report releases
df = ak.stock_research_detail()
```

---

## 8. LSEG (Refinitiv)

### Service Information
- **URL**: `https://api.analytics.lseg.com/lfa/mcp`
- **Type**: HTTP MCP
- **Primary function**: Fixed income, FX, options, macro data

### API Interfaces Provided

#### Fixed Income Tools
```
bond_price()                               # Bond pricing
yieldbook_bond_reference()                 # Bond reference data
yieldbook_cashflow()                       # Cash flow projection
yieldbook_scenario()                       # Scenario analysis
interest_rate_curve()                      # Yield curve
fixed_income_risk_analytics()              # Risk analytics
```

#### Derivatives Tools
```
equity_vol_surface()                       # Equity volatility surface
fx_vol_surface()                           # FX volatility surface
option_value()                             # Option pricing
option_template_list()                     # Option templates
tscc_historical_pricing_summaries()        # Historical pricing
qa_historical_equity_price()               # Historical equity prices
```

#### Macro Tools
```
macro_data()                               # Macro indicators
economic_calendar()                        # Economic calendar
central_bank_rates()                       # Central bank rates
```

### Corresponding AKShare APIs

| Function | LSEG API | AKShare Equivalent | Notes |
|------|---------|------------------|------|
| Bond pricing | `bond_price()` | `bond_sina` | Bond market data |
| Yield curve | `interest_rate_curve()` | No direct equivalent | Requires financial database call |
| Option pricing | `option_value()` | `stock_option_sina` | Options market data |
| Volatility | `equity_vol_surface()` | No direct equivalent | Must be calculated |
| Macro data | `macro_data()` | `macro_*` series | Economic data |
| Central bank rates | `central_bank_rates()` | `macro_*` | Interest rate data |

### Implementation
```python
import akshare as ak

# Get bond data
df = ak.bond_sina()

# Get options data
df = ak.stock_option_sina()

# Get interest rate data
df = ak.macro_cninfo()

# Get macro indicators
df = ak.macro_sz_retail_sales()  # Retail sales data
df = ak.macro_china_gdp()         # GDP data
df = ak.macro_china_ppi()         # PPI data
df = ak.macro_china_cpi()         # CPI data
```

---

## 9. PitchBook

### Service Information
- **URL**: `https://premium.mcp.pitchbook.com/mcp`
- **Type**: HTTP MCP
- **Primary function**: M&A deal data, private equity, comparable transaction analysis

### API Interfaces Provided
```
GET /transactions/{transaction_id}         # Transaction details
GET /comparables/{company_id}              # Comparable transactions
GET /valuation-multiples/{sector}          # Valuation multiples
GET /company-financials/{company_id}       # Company financials
GET /buyer-list/{criteria}                 # Buyer list
GET /precedent-transactions/{ticker}       # Precedent transactions
```

### Corresponding AKShare APIs

| Function | PitchBook API | AKShare Equivalent | Notes |
|------|----------|-------------------|------|
| Transaction details | `/transactions/` | No direct equivalent | Requires scraper for A-shares |
| Comparable transactions | `/comparables/` | Must be built manually | Use listed company data |
| Valuation multiples | `/valuation-multiples/` | `stock_valuation` | PE/PB, etc. |
| Buyer list | `/buyer-list/` | No equivalent | Requires corporate information database |
| Precedent transactions | `/precedent-transactions/` | No direct equivalent | Requires scraper |

### Implementation
```python
import akshare as ak

# Get valuation data for comparable analysis
df = ak.stock_valuation()

# Get listed company financials
df = ak.stock_main_indicator(symbol="000001")

# Get additional offering and rights issue financing activities
df = ak.stock_allocation_cninfo()

# Get M&A and restructuring information
df = ak.stock_board_change_cninfo()
```

---

## 10. Chronograph

### Service Information
- **URL**: `https://ai.chronograph.pe/mcp`
- **Type**: HTTP MCP
- **Primary function**: Private equity data, deal screening, portfolio monitoring

### API Interfaces Provided
```
GET /pe-deals/{date_range}                 # Private equity deals
GET /portfolio-monitoring/{fund_id}        # Portfolio monitoring
GET /deal-screening/{criteria}             # Deal screening
GET /returns-analysis/{investment_id}      # Returns analysis
GET /unit-economics/{company_id}           # Unit economics
GET /exit-strategy/{investment_id}         # Exit strategy
```

### Corresponding AKShare APIs

| Function | Chronograph API | AKShare Equivalent | Notes |
|------|----------|------------------|------|
| Private equity deals | `/pe-deals/` | No direct equivalent | No PE data for A-shares |
| Portfolio monitoring | `/portfolio-monitoring/` | Must be tracked manually | Can combine with public data |
| Returns analysis | `/returns-analysis/` | Must be calculated manually | Use historical prices |
| Unit economics | `/unit-economics/` | `stock_main_indicator` | Requires financial analysis |

### Implementation
```python
import akshare as ak

# Get listed company financials for analysis
df = ak.stock_main_indicator(symbol="000001")

# Get financing rounds (IPO, additional offerings)
df = ak.stock_allocation_cninfo()

# Get changes in shareholding
df = ak.stock_restricted_shares()
```

---

## 11. Egnyte

### Service Information
- **URL**: `https://mcp-server.egnyte.com/mcp`
- **Type**: HTTP MCP
- **Primary function**: File storage, document management, report publishing

### API Interfaces Provided
```
POST /files/upload                         # Upload file
GET /files/{file_id}                       # Get file
DELETE /files/{file_id}                    # Delete file
GET /folders/{folder_id}                   # List folder
POST /share/{file_id}                      # Share file
GET /activity/{file_id}                    # File activity log
```

### Corresponding AKShare APIs

| Function | Egnyte API | AKShare Equivalent | Notes |
|------|-----------|------------------|------|
| File management | `/files/` | No equivalent | Requires a local solution |
| File sharing | `/share/` | No equivalent | Requires a local solution |
| Activity log | `/activity/` | No equivalent | Requires a local solution |

### Implementation
```python
# File storage requires a local implementation. Options include:
# - MinIO (open-source S3-compatible)
# - Nextcloud (open-source cloud storage)
# - Alibaba Cloud OSS
# - Tencent Cloud COS
```

---

## AKShare Replacement Summary by Function Category

### Financial Data
| Need | AKShare API | Description |
|------|-----------|------|
| Listed company financial statements | `stock_financial_analysis_indicator` | Comprehensive financial data |
| Key financial indicators | `stock_main_indicator` | PE, PB, ROE, etc. |
| Cash flow data | `stock_cash_flow_sheet` | Cash flow statement |
| Valuation data | `stock_valuation` | Valuation multiples |
| Dividend information | `stock_dividend_cninfo` | Dividend history |

### News and Events
| Need | AKShare API | Description |
|------|-----------|------|
| News commentary | `guba_sina` | Stock forum information |
| Company announcements | `stock_information` | Announcement information |
| Research reports | `stock_research_detail` | Research reports |

### Market Data
| Need | AKShare API | Description |
|------|-----------|------|
| Historical prices | `stock_zh_a_hist` | Daily data |
| Real-time prices | `stock_zh_a_hist_min` | Minute data |
| Options data | `stock_option_sina` | Options market data |
| Bond data | `bond_sina` | Bond market data |

### Company Information
| Need | AKShare API | Description |
|------|-----------|------|
| Industry classification | `bk_sina` | Industry information |
| Industry constituents | `bk_sina_members` | Industry constituent stocks |
| Basic stock information | `stock_info_a_sina` | Listed company information |

### Macro Data
| Need | AKShare API | Description |
|------|-----------|------|
| GDP data | `macro_china_gdp` | Economic output |
| CPI data | `macro_china_cpi` | Consumer price index |
| PPI data | `macro_china_ppi` | Producer price index |
| Interest rate data | `macro_cninfo` | Interest rate information |

---

## Complete AKShare Replacement Implementation Examples

### Scenario 1: Build a Comparable Company Analysis (Replaces S&P Global + FactSet)

```python
import akshare as ak
import pandas as pd

def comparable_company_analysis(target_ticker, sector):
    """
    Use AKShare to replace S&P Global + FactSet
    """
    # Get industry constituent stocks
    industry_df = ak.bk_sina_members(symbol=sector)
    competitors = industry_df['code'].tolist()
    competitors.remove(target_ticker)  # Remove target company
    
    # Get valuation and financial data for all companies
    results = []
    for ticker in competitors:
        valuation = ak.stock_valuation(symbol=ticker)
        main_indicator = ak.stock_main_indicator(symbol=ticker)
        
        results.append({
            'ticker': ticker,
            'pe': valuation['pe'].values[0],
            'pb': valuation['pb'].values[0],
            'roe': main_indicator['roe'].values[0],
            'profit_margin': main_indicator['profit_margin'].values[0],
        })
    
    comp_df = pd.DataFrame(results)
    return comp_df.describe()

# Usage example
comp_analysis = comparable_company_analysis('000001', 'bk0471')
print(comp_analysis)
```

### Scenario 2: Earnings Analysis (Replaces Daloopa + FactSet)

```python
import akshare as ak

def earnings_analysis(ticker, quarters=4):
    """
    Use AKShare to replace Daloopa + FactSet for earnings analysis
    """
    # Get historical financial indicators
    df = ak.stock_main_indicator(symbol=ticker)
    
    # Get recent financial data
    financial = ak.stock_financial_analysis_indicator(
        symbol=ticker,
        indicator="Basic EPS"
    )
    
    # Get cash flow
    cashflow = ak.stock_cash_flow_sheet(symbol=ticker)
    
    return {
        'main_indicator': df.head(quarters),
        'eps': financial,
        'cashflow': cashflow.head(quarters)
    }

earnings = earnings_analysis('000001')
```

### Scenario 3: Fixed Income Analysis (Replaces LSEG Bond Tools)

```python
import akshare as ak

def bond_portfolio_analysis():
    """
    Use AKShare to replace LSEG bond analysis
    """
    # Get bond basic information
    bonds = ak.bond_sina()
    
    # Get convertible bonds
    convertible = ak.convertible_bond_sina()
    
    # Portfolio analysis
    all_bonds = pd.concat([
        bonds[['bond_code', 'bond_name', 'trade_price', 'yield']],
        convertible[['code', 'name', 'price', 'yield']]
    ])
    
    # Calculate portfolio weighted yield
    total_value = all_bonds['trade_price'].sum()
    weighted_yield = (all_bonds['trade_price'] * all_bonds['yield']).sum() / total_value
    
    return {
        'bonds': all_bonds,
        'portfolio_yield': weighted_yield
    }
```

### Scenario 4: Event-Driven Analysis (Replaces MT Newswires + Aiera)

```python
import akshare as ak

def event_driven_analysis(ticker):
    """
    Use AKShare to replace MT Newswires + Aiera for event analysis
    """
    # Get dividends and stock splits (corporate actions)
    dividends = ak.stock_dividend_cninfo(symbol=ticker)
    
    # Get stock forum news (for sentiment analysis)
    news = ak.guba_sina()
    
    # Get suspension/resumption data (market events)
    history = ak.stock_zh_a_hist(symbol=ticker, period="daily", 
                                 start_date="20230101", end_date="20231231")
    
    # Identify significant event dates
    events = {
        'dividends': dividends['dividend_date'].tolist() if not dividends.empty else [],
        'news_dates': news[news['symbol'] == ticker]['pub_date'].tolist() if not news.empty else []
    }
    
    return events
```

---

## Migration Cost Assessment

| MCP Service | Replacement Difficulty | Migration Cost | Notes |
|---------|---------|---------|------|
| Daloopa | ⭐ Low | Low | AKShare covers fully |
| Morningstar | ⭐⭐ Low-medium | Low | Missing ratings data |
| S&P Global | ⭐⭐⭐ Medium | Medium | Benchmarks must be built manually |
| FactSet | ⭐ Low | Low | Comprehensive coverage |
| Moody's | ⭐⭐⭐ Medium | Medium | Missing ratings |
| MT Newswires | ⭐⭐⭐⭐ High | High | Requires scraper or subscription |
| Aiera | ⭐⭐⭐⭐ High | High | Earnings call audio requires subscription |
| LSEG | ⭐⭐⭐⭐ High | High | Bond pricing model must be built |
| PitchBook | ⭐⭐⭐⭐ High | High | M&A data requires scraper |
| Chronograph | ⭐⭐⭐⭐ High | High | No equivalent for PE data |
| Egnyte | ⭐⭐⭐⭐ High | High | Requires custom file system |

---

## Recommended Migration Strategy

### Phase 1 (High ROI)
- ✅ Use AKShare to replace **Daloopa** + **FactSet** financial data
- ✅ Use AKShare to replace **S&P Global** valuation data
- Effort: Low, Benefit: High

### Phase 2 (Medium-term)
- ✅ Web scraping + AKShare to replace **MT Newswires** news
- ✅ NLP analysis + AKShare to replace **Aiera** sentiment analysis
- Effort: Medium, Benefit: Medium

### Phase 3 (Long-term)
- Build an internal bond pricing model to replace **LSEG**
- Build an M&A database to replace **PitchBook**
- Build a PE database to replace **Chronograph**
- Effort: High, Benefit: High

---

## Summary

| Metric | Score |
|------|------|
| AKShare overall coverage | 6/10 |
| vs. Daloopa + FactSet | 8/10 ✅ |
| vs. S&P Global | 6/10 |
| vs. LSEG | 4/10 |
| vs. news and event data | 5/10 |
| Migration feasibility | 7/10 |

**Conclusion**: AKShare can effectively replace **financial data** MCP services, but for **news and events**, **fixed income**, and **M&A** data, additional scraping infrastructure or subscriptions will be required.
