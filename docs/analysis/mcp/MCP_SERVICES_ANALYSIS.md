# MCP Service Analysis

## Overview

This project uses **11 MCP (Model Context Protocol) services** distributed across different plugins. All services are of HTTP type.

---

## Complete MCP Service List

### 1. **Daloopa**
- **URL**: `https://mcp.daloopa.com/server/mcp`
- **Type**: HTTP
- **Plugin**: financial-analysis (core plugin)
- **Function**: Financial data and market data aggregation platform
- **Use cases**: Pulling company financial data, competitor analysis, market trends

### 2. **Morningstar**
- **URL**: `https://mcp.morningstar.com/mcp`
- **Type**: HTTP
- **Plugin**: financial-analysis (core plugin)
- **Function**: Investment research and fund data platform
- **Use cases**: Fund analysis, stock ratings, performance benchmarking

### 3. **S&P Global (Kensho)**
- **URL**: `https://kfinance.kensho.com/integrations/mcp`
- **Type**: HTTP
- **Plugin**:
  - financial-analysis (core plugin)
  - partner-built/spglobal (S&P Global dedicated plugin)
- **Function**: Financial data, industry analysis, valuation tools
- **Use cases**: Company tear sheets, earnings previews, financing summaries

### 4. **FactSet**
- **URL**: `https://mcp.factset.com/mcp`
- **Type**: HTTP
- **Plugin**: financial-analysis (core plugin)
- **Function**: Comprehensive financial data and analytics platform
- **Use cases**: Financial modeling, valuation, market data

### 5. **Moody's**
- **URL**: `https://api.moodys.com/genai-ready-data/m1/mcp`
- **Type**: HTTP
- **Plugin**: financial-analysis (core plugin)
- **Function**: Credit ratings and risk analysis
- **Use cases**: Credit quality assessment, bond analysis

### 6. **MT Newswires**
- **URL**: `https://vast-mcp.blueskyapi.com/mtnewswires`
- **Type**: HTTP
- **Plugin**: financial-analysis (core plugin)
- **Function**: Financial news and market intelligence
- **Use cases**: Market news, company announcements, economic news

### 7. **Aiera**
- **URL**: `https://mcp-pub.aiera.com`
- **Type**: HTTP
- **Plugin**: financial-analysis (core plugin)
- **Function**: Event-driven market intelligence
- **Use cases**: Earnings calls, company events, market insights

### 8. **LSEG (London Stock Exchange Group)**
- **URL**: `https://api.analytics.lseg.com/lfa/mcp`
- **Type**: HTTP
- **Plugin**:
  - financial-analysis (core plugin)
  - partner-built/lseg (LSEG dedicated plugin)
- **Function**: Fixed income, FX, options, macro data
- **Use cases**: Bond pricing, yield curve analysis, options valuation, macro dashboards

### 9. **PitchBook**
- **URL**: `https://premium.mcp.pitchbook.com/mcp`
- **Type**: HTTP
- **Plugin**: financial-analysis (core plugin)
- **Function**: M&A and private equity data
- **Use cases**: Deal tracking, comparable transaction analysis, buyer lists

### 10. **Chronograph**
- **URL**: `https://ai.chronograph.pe/mcp`
- **Type**: HTTP
- **Plugin**: financial-analysis (core plugin)
- **Function**: Private equity and venture capital data
- **Use cases**: Deal screening, portfolio monitoring, returns analysis

### 11. **Egnyte**
- **URL**: `https://mcp-server.egnyte.com/mcp`
- **Type**: HTTP
- **Plugin**: financial-analysis (core plugin)
- **Function**: File management and file sharing
- **Use cases**: File storage, document management, report publishing

---

## MCP Service Distribution by Plugin

### Core Plugin: financial-analysis
Contains all 11 MCP services:
- ✅ Daloopa
- ✅ Morningstar
- ✅ S&P Global
- ✅ FactSet
- ✅ Moody's
- ✅ MT Newswires
- ✅ Aiera
- ✅ LSEG
- ✅ PitchBook
- ✅ Chronograph
- ✅ Egnyte

### Add-on Plugins

| Plugin | MCP Services |
|------|---------|
| **equity-research** | No independent MCP (inherits from financial-analysis) |
| **investment-banking** | No independent MCP (inherits from financial-analysis) |
| **private-equity** | No independent MCP (inherits from financial-analysis) |
| **wealth-management** | No independent MCP (inherits from financial-analysis) |

### Partner-Built Plugins

| Plugin | MCP Services | Notes |
|------|---------|------|
| **partner-built/lseg** | LSEG | Dedicated LSEG data integration |
| **partner-built/spglobal** | S&P Global | Dedicated S&P data integration |

---

## MCP Services by Function

### Financial Data and Modeling
- **Daloopa** - Financial data aggregation
- **FactSet** - Comprehensive financial data
- **Morningstar** - Investment data

### Company and Valuation Analysis
- **S&P Global** - Industry analysis, valuation
- **Moody's** - Credit analysis

### News and Events
- **MT Newswires** - Financial news
- **Aiera** - Earnings calls, market events

### M&A and Private Equity
- **PitchBook** - M&A and PE deal data
- **Chronograph** - Private equity and venture capital

### Fixed Income and Derivatives
- **LSEG** - Bonds, FX, options, macro

### Document Management
- **Egnyte** - File storage and management

---

## Key Characteristics

### Centralized Architecture
- All MCP services are declared in the **financial-analysis (core plugin)**
- Add-on plugins and partner-built plugins **inherit** the core plugin's MCP services
- Avoids duplicate configuration and version conflicts

### Service Sharing Mechanism
```
financial-analysis (core)
    ↓ provides all MCP services
├── equity-research
├── investment-banking
├── private-equity
└── wealth-management

partner-built/lseg (LSEG dedicated)
    ↓ additional LSEG customization

partner-built/spglobal (S&P Global dedicated)
    ↓ additional S&P Global customization
```

### Authentication and Authorization Requirements
Per README.md:
> MCP access may require a subscription or API key from the corresponding provider.

Credentials that need to be configured:
- Daloopa API Key
- Morningstar API Key
- S&P Global / Kensho API Key
- FactSet API Key
- Moody's API Key
- MT Newswires API Key
- Aiera API Key
- LSEG API Key / OAuth
- PitchBook API Key
- Chronograph API Key
- Egnyte API Key

---

## MCP Use Cases in Workflows

### Research-to-Report Workflow
1. Pull financial data using **Daloopa/FactSet**
2. Retrieve news and events using **MT Newswires/Aiera**
3. Get industry analysis using **S&P Global**
4. Obtain credit analysis using **Moody's**
5. Generate publication-ready equity research reports

### Comparable Company Analysis (Comps)
1. Get financial metrics using **FactSet/Daloopa**
2. Get transaction multiples using **PitchBook**
3. Get industry benchmarks using **S&P Global**

### M&A Workflow
1. Identify buyer lists using **PitchBook**
2. Get target company financials using **FactSet/Daloopa**
3. Assess credit risk using **Moody's**

### Fixed Income Analysis (LSEG plugin)
1. Bond pricing using **LSEG**
2. Yield curve analysis
3. FX carry trade evaluation
4. Options valuation
5. Build macro dashboards

### Private Equity Workflow
1. Deal screening using **Chronograph**
2. Unit economics analysis using **FactSet**
3. Comparable transaction analysis using **PitchBook**

---

## Architecture Benefits

| Benefit | Description |
|------|------|
| **Configure once, use everywhere** | Configure once in financial-analysis; all plugins can use it |
| **Version consistency** | No risk of different plugins using different versions |
| **Easy to maintain** | Updating or replacing an MCP only requires changing one place |
| **Flexible extension** | Partners can add their own dedicated MCP services |
| **Reduced complexity** | Add-on plugins can focus on business logic, not data connections |

---

## Customization Recommendations

To tailor this architecture for a specific company, you can:

1. **Replace data sources**
   - Edit `financial-analysis/.mcp.json`
   - Point to your company's internal data APIs
   - Keep the interfaces the same

2. **Add internal tools**
   - Add MCP services for internal financial systems
   - Add MCP services for internal document management systems
   - Add MCP services for internal trading platforms

3. **Configure specific services**
   - Some companies may only need specific data providers
   - MCP services can be selectively enabled or disabled

---

## Summary

✅ **11 MCP services**
✅ **Centralized in the financial-analysis core plugin**
✅ **Spanning financial research, M&A, private equity, fixed income, and more**
✅ **Supports end-to-end workflows from data collection to report generation**
✅ **Easy to customize and extend**
