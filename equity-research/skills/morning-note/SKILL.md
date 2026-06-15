---
name: morning-note
description: Draft concise morning meeting notes summarizing overnight developments, trade ideas, and key events for covered stocks. Designed for a 7am morning meeting format — tight, opinionated, actionable. Trigger when: "morning note", "morning meeting", "what happened overnight", "trade ideas", "morning call prep", or "daily note".
---

# Morning Note

Description: Draft concise morning meeting notes summarizing overnight developments, trade ideas, and key events for covered stocks. Designed for a 7am morning meeting format — tight, opinionated, actionable. Trigger when: "morning note", "morning meeting", "what happened overnight", "trade ideas", "morning call prep", or "daily note".

## Workflow

### Step 1: Overnight Developments

Scan for relevant events across the coverage universe using these OpenBB MCP tools:

**Earnings and Guidance**
- `mcp__claude_ai_OpenBB__equity_calendar_earnings` — check which covered companies report overnight or pre-market
- `mcp__claude_ai_OpenBB__equity_estimates_consensus` — pull consensus vs. actuals for any overnight reporters
- `mcp__claude_ai_OpenBB__earnings_review` — structured earnings review with beat/miss analysis
- Earnings surprises (revenue, EPS, key metrics beat or miss)
- Guidance changes (raised, lowered, maintained)

**News and Events**
- `mcp__claude_ai_OpenBB__news_company` — company-specific news for each covered name
- `mcp__claude_ai_OpenBB__news_world` — broad market and macro news overnight
- M&A announcements or rumors
- Management changes
- Product launches or regulatory decisions
- Competitor analyst upgrades/downgrades
- Macro data or policy changes affecting the sector

**Market Context**
- `mcp__claude_ai_OpenBB__equity_price_quote` — pre-market quotes for covered names
- `mcp__claude_ai_OpenBB__equity_market_snapshots` — broad market pre-market snapshot
- `mcp__claude_ai_OpenBB__index_snapshots` — index-level overnight and pre-market moves
- `mcp__claude_ai_OpenBB__etf_discovery_active` — sector ETF movers
- `mcp__claude_ai_OpenBB__economy_calendar` — key economic data releases scheduled for the day
- `mcp__claude_ai_Interactive_MCP__glance` — quick one-screen summary for any covered ticker

### Step 2: Morning Note Format

Keep it tight — a morning note should be readable in 2 minutes:

---

**[Date] Morning Note — [Analyst Name]**
**[Sector Coverage]**

**Top Idea: [Headline — the one thing a portfolio manager needs to hear]**
- 2-3 sentences on the key development and why it matters
- Stock impact: price target, rating reiterated/changed

**Overnight / Pre-Market Developments**
- [Company A]: Single-line summary of earnings/news + our view
- [Company B]: Single-line summary + our view
- [Sector/Macro]: Relevant sector-wide developments

**Key Events Today**
- [Time]: [Company] earnings call
- [Time]: Economic data release (expected vs. our view)
- [Time]: Conference or investor day

**Trade Ideas** (if any)
- [Long/Short] [Company]: 1-2 sentence thesis + catalyst
- Risk: what would make this idea wrong

---

### Step 3: Earnings Quick Comment

If a covered company reports, provide a quick reaction. Pull data via:
- `mcp__claude_ai_OpenBB__equity_fundamental_income` — reported income statement actuals
- `mcp__claude_ai_OpenBB__equity_estimates_consensus` — consensus vs. actual comparison
- `mcp__claude_ai_OpenBB__earnings_review` — structured beat/miss analysis

| Metric | Consensus | Actual | Beat/Miss |
|--------|-----------|--------|-----------|
| Revenue | | | |
| EPS | | | |
| [Key Metric] | | | |
| Guidance | | | |

**Our View**: 2-3 sentences — is this good or bad for the stock? Does it change our thesis?

**Action**: Maintain/upgrade/downgrade rating? Adjust price target?

### Step 4: Output

- Markdown text for email/Slack distribution
- Word document if formal distribution is needed
- Keep to 1 page — portfolio managers and traders will not read more

## Important Notes

- Have a view — a morning note that just summarizes news without a perspective is useless
- Lead with the most important thing — don't bury the headline
- "No news" is a valid morning note — say "no material news overnight, maintaining positioning"
- Distinguish actionable events (earnings, M&A) from noise (minor analyst notes, non-events)
- Timestamp your comments — if writing at 6am, note that pre-market may change by open
- If you were wrong, acknowledge it in the next morning note — credibility matters more than being right every time
