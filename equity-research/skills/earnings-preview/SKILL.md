---
name: earnings-preview
description: Pre-earnings analysis using an estimate model, scenario framework, and key metrics. Use before a company reports quarterly earnings to prepare a positioning note, build bull/bear scenarios, and identify what will move the stock. Trigger when: "earnings preview", "what to watch for [company] earnings", "pre-earnings", "earnings setup", or "[company] Q[X] preview".
---

# Earnings Preview

Description: Pre-earnings analysis using an estimate model, scenario framework, and key metrics. Use before a company reports quarterly earnings to prepare a positioning note, build bull/bear scenarios, and identify what will move the stock. Trigger when: "earnings preview", "what to watch for [company] earnings", "pre-earnings", "earnings setup", or "[company] Q[X] preview".

## Workflow

### Step 1: Gather Context

- Identify the company and reporting quarter
- Pull consensus estimates (revenue, EPS, key segment metrics) via AE composite MCP (openbb); fall back to SEC EDGAR filings or Yahoo Finance
- Find earnings date and time (pre-market vs. after-market)
- Review the company's prior-quarter earnings call for any guidance or commentary

### Step 2: Key Metrics Framework

Build a company-specific "what to watch" framework:

**Financial Metrics:**
- Revenue vs. consensus (total and by segment)
- EPS vs. consensus
- Margins (gross, operating, net) — expanding or contracting?
- Free cash flow
- Forward guidance vs. consensus

**Operating Metrics** (industry-specific):
- Tech/SaaS: ARR, net retention, RPO, customer count
- Retail: same-store sales, traffic, basket size
- Industrials: backlog, book-to-bill, price vs. volume
- Financials: NIM, credit quality, loan growth, fee income
- Healthcare: prescriptions, patient volumes, pipeline updates

### Step 3: Scenario Analysis

Build 3 scenarios with stock price impact:

| Scenario | Revenue | EPS | Key Driver | Stock Reaction |
|----------|---------|-----|------------|---------------|
| Bull | | | | |
| Base | | | | |
| Bear | | | | |

For each scenario:
- What needs to happen operationally
- What management commentary would signal this
- Historical context — how has the stock traded on similar reports?

### Step 4: Catalyst Checklist

Identify 3-5 things that will determine the stock's reaction:

1. [Metric] vs. [consensus/buyside expectations] — why it matters
2. [Guidance item] — what the buyside expects to hear
3. [Narrative shift] — any strategic changes, M&A, restructuring

### Step 5: Output

Single-page earnings preview containing:
- Company, quarter, earnings date
- Consensus estimates table (sourced from AE composite MCP / openbb or Yahoo Finance)
- Key metrics to watch (ranked by importance)
- Bull/base/bear scenario table
- Catalyst checklist
- Trade setup: recent stock performance, options implied volatility

## Important Notes

- Consensus estimates change — always note the source and date of estimates; use AE composite MCP (openbb) as primary; fall back to Yahoo Finance
- "Buyside expectations" from survey data are often more relevant than published consensus
- Historical earnings reactions help calibrate expectations (search "[company] earnings reaction history")
- Options implied volatility tells you what the market expects — compare to your scenarios
