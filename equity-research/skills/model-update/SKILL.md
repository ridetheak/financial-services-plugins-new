---
name: model-update
description: Update a financial model with new data — quarterly earnings, management guidance, macro changes, or revised assumptions. Adjust estimates, recalculate valuation, and flag material changes. Use after earnings, after a guidance update, or when assumptions need refreshing. Trigger when: "update model", "plug in earnings", "refresh estimates", "updated numbers for [company]", "new guidance", or "revised estimates".
---

# Model Update

Description: Update a financial model with new data — quarterly earnings, management guidance, macro changes, or revised assumptions. Adjust estimates, recalculate valuation, and flag material changes. Use after earnings, after a guidance update, or when assumptions need refreshing. Trigger when: "update model", "plug in earnings", "refresh estimates", "updated numbers for [company]", "new guidance", or "revised estimates".

## Workflow

### Step 1: Identify What Changed

Determine the update trigger:
- **Earnings release**: New quarterly actuals to plug in
- **Guidance change**: Company updated its forward outlook
- **Estimate revision**: Analyst changing assumptions based on new data
- **Macro update**: Interest rate, FX, commodity price changes
- **Event-driven**: M&A, restructuring, new product, management change

### Step 2: Insert New Data

#### Post-Earnings
Update model with reported actuals. Pull financials using:
- `mcp__claude_ai_OpenBB__equity_fundamental_income` — income statement actuals (revenue, gross margin, operating expenses, EBITDA, EPS)
- `mcp__claude_ai_OpenBB__equity_fundamental_balance` — balance sheet (cash, debt, share count)
- `mcp__claude_ai_OpenBB__equity_fundamental_cash` — cash flow statement (CapEx, free cash flow, working capital)
- `mcp__claude_ai_OpenBB__fd_get_income_statement` / `mcp__claude_ai_OpenBB__fd_get_balance_sheet` / `mcp__claude_ai_OpenBB__fd_get_cash_flow_statement` — alternative via financialdatasets MCP
- Fall back to SEC EDGAR 10-Q/10-K filed text for line-item verification

| Line Item | Prior Estimate | Actual | Variance | Notes |
|-----------|---------------|--------|----------|-------|
| Revenue | | | | |
| Gross margin | | | | |
| Operating expenses | | | | |
| EBITDA | | | | |
| EPS | | | | |
| [Key Metric 1] | | | | |
| [Key Metric 2] | | | | |

**Segment Detail** (if applicable):
- Use `mcp__claude_ai_OpenBB__fd_get_segmented_financials` for segment revenue and margin breakdown
- Note any segment mix changes

**Balance Sheet / Cash Flow Update**:
- Cash and debt balances
- Share count (buybacks, dilution)
- CapEx actuals vs. estimate
- Working capital changes

### Step 3: Revise Forward Estimates

Adjust forward estimates based on new data. Compare to Street consensus using:
- `mcp__claude_ai_OpenBB__equity_estimates_consensus` — consensus revenue, EPS, EBITDA
- `mcp__claude_ai_OpenBB__equity_estimates_forward_eps` — forward EPS estimates by period
- `mcp__claude_ai_OpenBB__equity_estimates_forward_ebitda` — forward EBITDA estimates
- `mcp__claude_ai_OpenBB__equity_estimates_forward_sales` — forward revenue estimates

| | Old FY Estimate | New FY Estimate | Change | Old Next FY | New Next FY | Change |
|---|----------------|----------------|--------|-------------|-------------|--------|
| Revenue | | | | | | |
| EBITDA | | | | | | |
| EPS | | | | | | |

**Key Assumption Changes:**
- Which assumptions changed and why?
- Revenue growth rate: old → new (reason)
- Margin assumptions: old → new (reason)
- Any new line items (restructuring charges, one-time gains, etc.)

### Step 4: Valuation Impact

Recalculate valuation with updated estimates. Pull current multiples and metrics using:
- `mcp__claude_ai_OpenBB__equity_fundamental_metrics` — key valuation metrics (EV/EBITDA, P/E, EV/Sales, FCF yield)
- `mcp__claude_ai_OpenBB__fmp_key_metrics_ttm` — trailing twelve-month key metrics
- `mcp__claude_ai_OpenBB__equity_fundamental_ratios` — profitability and valuation ratios
- `mcp__claude_ai_OpenBB__fmp_enterprise_values` — enterprise value history

| Valuation Method | Prior | Updated | Change |
|-----------------|-------|---------|--------|
| DCF fair value | | | |
| P/E (NTM EPS × target multiple) | | | |
| EV/EBITDA (NTM EBITDA × target multiple) | | | |
| **Price Target** | | | |

### Step 5: Summary and Action

**Estimate Change Summary:**
- One paragraph: what changed, why, and what it means for the stock
- Is this a thesis-changing event or noise?

**Rating / Price Target:**
- Maintain or change rating?
- New price target (if changed) and methodology
- Upside/downside relative to current price (pull live quote via `mcp__claude_ai_OpenBB__equity_price_quote`)

### Step 6: Output

- Updated Excel model (if user provides existing model)
- Estimate change summary (Markdown or Word)
- Updated price target derivation

## Important Notes

- Always reconcile estimates to company-reported numbers before projecting forward; primary source is SEC EDGAR 10-Q/10-K, verified via OpenBB tools
- Note whether your estimates are GAAP or adjusted, and any non-recurring items
- Track estimate revision history — this shows how your analysis has evolved
- If the quarter was noisy, separate signal from noise in the estimate change
- After updating, compare revised estimates to consensus via `mcp__claude_ai_OpenBB__equity_estimates_consensus` — how do your revisions compare to the Street?
- Share count matters — dilution from stock compensation, conversions, or buybacks can materially affect EPS; verify via `mcp__claude_ai_OpenBB__equity_ownership_share_statistics`
