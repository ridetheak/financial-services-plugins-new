# Thesis Tracker

description: Maintain and update investment theses for portfolio positions and the watchlist. Track key data points, catalysts, and thesis milestones. Use when updating a thesis with new information, reviewing position rationale, or checking whether a thesis is still intact. Triggers on "update [Company]'s thesis", "is my thesis still intact", "thesis check", "add data point to [Company]", or "review my position".

## Workflow

### Step 1: Define or Load Thesis

If creating a new thesis:
- **Company**: name and ticker
- **Position**: long or short
- **Thesis statement**: 1-2 sentence core thesis (e.g., "Long ACME — pricing power-driven margin expansion + operating leverage as mix shifts to software")
- **Key pillars**: 3-5 supporting arguments
- **Key risks**: 3-5 risks that would invalidate the thesis
- **Catalysts**: upcoming events that could prove / disprove the thesis (earnings, product launches, regulatory decisions)
- **Price target / valuation**: what the thesis is worth if it plays out
- **Stop-loss trigger**: what would make you exit

If updating an existing thesis, ask the user for new data points or developments.

### Step 2: Update Log

For each new data point or development:

- **Date**: when it happened
- **Data point**: what changed (earnings beat, management departure, competitor move, etc.)
- **Thesis impact**: does it strengthen, weaken, or stay neutral on a specific pillar?
- **Action**: no change / add to position / trim / exit
- **Updated conviction**: high / medium / low

### Step 3: Thesis Scorecard

Maintain a running scorecard:

| Pillar | Original expectation | Current status | Trend |
|--------|---------------------|----------------|-------|
| Revenue growth >20% | On track | 22% in Q3 | Steady |
| Margin expansion | Behind | Margins flat YoY | Concerning |
| New product launch | Pending | Delayed to Q2 | Watch |

### Step 4: Catalyst Calendar

Track upcoming catalysts:

| Date | Event | Expected impact | Notes |
|------|-------|-----------------|-------|
| | | | |

### Step 5: Output

Thesis summary suitable for:
- Morning meeting discussion
- Portfolio review
- Risk committee presentation

Format: concise Markdown or Word document containing scorecard, recent updates, and current conviction level.

## Important Notes

- A thesis should be falsifiable — if nothing could disprove it, it isn't a thesis
- Track disconfirming evidence as rigorously as confirming evidence
- Review theses at least quarterly even if nothing dramatic happened
- If the user manages multiple positions, offer to run a full portfolio thesis review
- Store thesis data in a structured format so it can be referenced in-session
