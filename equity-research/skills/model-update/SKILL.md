# Model Update

description: Update financial models with new data — quarterly earnings, management guidance, macro changes, or revised assumptions. Adjust estimates, recompute valuation, flag material changes. Use post-earnings, after guidance updates, or when assumptions need refreshing. Triggers on "update model", "plug in earnings", "refresh estimates", "[Company]'s updated numbers", "new guidance", or "revised estimates".

## Workflow

### Step 1: Identify What Changed

Determine the update trigger:
- **Earnings release**: new quarterly actuals to plug in
- **Guidance change**: company updated forward outlook
- **Estimate revision**: analyst is changing assumptions based on new data
- **Macro update**: rates, FX, commodity price changes
- **Event-driven**: M&A, restructuring, new product, management change

### Step 2: Plug in New Data

#### Post-Earnings
Update the model with reported actuals:

| Line item | Prior estimate | Actual | Variance | Notes |
|-----------|---------------|--------|----------|-------|
| Revenue | | | | |
| Gross margin | | | | |
| Operating expenses | | | | |
| EBITDA | | | | |
| EPS | | | | |
| [Key metric 1] | | | | |
| [Key metric 2] | | | | |

**Segment detail** (where applicable):
- Update revenue and margins for each segment
- Note any segment mix shifts

**Balance sheet / cash flow updates:**
- Cash and debt balances
- Share count (buybacks, dilution)
- Capex actuals vs estimate
- Working capital changes

### Step 3: Revise Forward Estimates

Adjust forward estimates based on the new data:

| | Old FY est | New FY est | Change | Old NFY | New NFY | Change |
|---|-----------|-----------|--------|---------|---------|--------|
| Revenue | | | | | | |
| EBITDA | | | | | | |
| EPS | | | | | | |

**Key assumption changes:**
- Which assumptions did you change and why?
- Revenue growth rate: old → new (reason)
- Margin assumption: old → new (reason)
- Any new items (restructuring charges, one-time gains, etc.)

### Step 4: Valuation Impact

Recompute valuation with updated estimates:

| Valuation method | Prior | Updated | Change |
|------------------|-------|---------|--------|
| DCF fair value | | | |
| P/E (NTM EPS × target multiple) | | | |
| EV/EBITDA (NTM EBITDA × target multiple) | | | |
| **Price target** | | | |

### Step 5: Summary and Action

**Summary of estimate changes:**
- One paragraph: what changed, why, and what it means for the stock
- Is this a thesis-changing event or noise?

**Rating / price target:**
- Maintain or change rating?
- New price target (if changed) and methodology
- Upside / downside vs current price

### Step 6: Output

- Updated Excel model (if the user provides an existing model)
- Summary of estimate changes (Markdown or Word)
- Updated price target derivation

## Important Notes

- Always reconcile estimates with the company's reported numbers before projecting forward
- Note whether your estimates are GAAP or adjusted, and any non-recurring items
- Track estimate revision history — it shows the evolution of your analysis
- If the quarter is noisy, separate signal from noise in the estimate changes
- Check consensus after updating — how do your revised estimates compare to the Street?
- Share count matters — dilution from stock comp, conversions, or buybacks can materially affect EPS
