---
name: thesis-tracker
description: Maintain and update investment theses for portfolio positions and watchlist names. Track key data points, catalysts, and thesis milestones. Use when updating a thesis with new information, reviewing position rationale, or checking whether a thesis is still intact. Trigger when: "update thesis for [company]", "is my thesis still intact", "thesis check", "add data point to [company]", or "review my position".
---

# Thesis Tracker

Description: Maintain and update investment theses for portfolio positions and watchlist names. Track key data points, catalysts, and thesis milestones. Use when updating a thesis with new information, reviewing position rationale, or checking whether a thesis is still intact. Trigger when: "update thesis for [company]", "is my thesis still intact", "thesis check", "add data point to [company]", or "review my position".

## Workflow

### Step 1: Define or Load Thesis

If creating a new thesis:
- **Company**: Name and ticker
- **Position**: Long or short
- **Thesis statement**: 1-2 sentence core thesis (e.g., "Long ACME — margin expansion from pricing power + operating leverage as mix shifts toward software")
- **Key pillars**: 3-5 supporting arguments
- **Key risks**: 3-5 risks that would invalidate the thesis
- **Catalysts**: Upcoming events that could prove/disprove the thesis (earnings, product launches, regulatory decisions)
- **Price target / valuation**: What is it worth if the thesis plays out
- **Stop-loss triggers**: What would make you exit

If updating an existing thesis, ask the user for the new data points or developments.

### Step 2: Update Log

For each new data point or development:

- **Date**: When it occurred
- **Data point**: What changed (earnings beat, management departure, competitor move, etc.)
- **Thesis impact**: Does this strengthen, weaken, or leave neutral a specific pillar?
- **Action**: No change / add to position / reduce / exit
- **Updated conviction**: High / Medium / Low

### Step 3: Thesis Scorecard

Maintain a running scorecard:

| Pillar | Original Expectation | Current Status | Trend |
|--------|---------------------|---------------|-------|
| Revenue growth >20% | On track | Q3 was 22% | Stable |
| Margin expansion | Lagging | Margins flat YoY | Concerning |
| New product launch | Pending | Delayed to Q2 | Watch |

### Step 4: Catalyst Calendar

Track upcoming catalysts:

| Date | Event | Expected Impact | Notes |
|------|-------|----------------|-------|
| | | | |

### Step 5: Output

Thesis summary suitable for:
- Morning meeting discussion
- Portfolio review
- Risk committee presentation

Format: concise Markdown or Word document with scorecard, recent updates, and current conviction level.

## Important Notes

- A thesis should be falsifiable — if nothing could disprove it, it is not a thesis
- Track disconfirming evidence as rigorously as confirming evidence
- Review theses at least quarterly, even if nothing dramatic has happened
- If the user manages multiple positions, offer to run a full portfolio thesis review
- Store thesis data in structured format so it can be referenced across sessions
