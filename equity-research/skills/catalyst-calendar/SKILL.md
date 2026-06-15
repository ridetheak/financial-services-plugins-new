# Catalyst Calendar

Description: Build and maintain a catalyst calendar for a covered portfolio — earnings dates, conferences, product launches, regulatory decisions, and macro events. Helps prioritize attention and position ahead of events. Triggers: "catalyst calendar", "upcoming events", "what's coming up", "earnings calendar", "event calendar", or "catalyst tracker".

## Workflow

### Step 1: Define Coverage Universe

- List of companies to track (tickers or names)
- Sector/industry focus
- Include macro events? (Fed meetings, economic data, regulatory deadlines)
- Time horizon (next 2 weeks, 1 month, 1 quarter)

### Step 2: Gather Catalysts

For each company, identify upcoming events:

**Earnings and Financial Events**
- Quarterly earnings dates and timing (before-market / after-market)
- Annual shareholder meetings
- Investor Days / Analyst Days
- Capital Markets Days
- Debt maturities / financing dates

**Corporate Events**
- Product launches or announcements
- FDA approvals / regulatory decisions
- Contract renewals or expirations
- M&A milestones (closing dates, regulatory approvals)
- Management changes
- Insider trading windows (lockup expirations)

**Industry Events**
- Major conferences (dates, which companies are presenting)
- Trade shows
- Regulatory comment periods or rulings
- Industry data releases (monthly sales, traffic, etc.)

**Macro Events**
- Fed meetings (FOMC dates)
- Jobs reports, CPI, GDP releases
- Central bank decisions (ECB, BOJ, etc.)
- Geopolitical events with market impact

### Step 3: Calendar View

| Date | Event | Company / Sector | Type | Impact (High/Med/Low) | Our Positioning | Notes |
|------|-------|-----------------|------|----------------------|----------------|-------|
| | | | Earnings / Corporate / Industry / Macro | | Long / Short / Neutral | |

### Step 4: Weekly Preview

Generate a forward-looking summary each week:

**Key Events This Week:**
1. [Date]: [Company] Q[Quarter] Earnings — consensus est. [$X EPS], our estimate [$X], key focus: [metric]
2. [Date]: [Event] — why it matters for [stock]
3. [Date]: [Macro release] — expectations and our view

**Next Week Preview:**
- Advance notice of important upcoming events

**Positioning Implications:**
- Events that could affect specific positions
- Any pre-positioning recommended
- Risk management ahead of binary events

### Step 5: Output

- Excel workbook with calendar view and sortable columns
- Weekly preview email / note (Markdown)
- Optional: Google Calendar integration

## Important Notes

- Earnings dates shift — confirm with company investor relations and AE composite MCP (openbb) or Yahoo Finance as the date approaches
- Pre-announcement risk: track companies with a history of pre-announcing (positive or negative)
- Conference attendance rosters are valuable — which companies are presenting, and who is notably absent?
- Some catalysts are recurring (monthly industry data) — build a template and auto-populate
- Color-code by impact level: red = high impact, yellow = moderate, green = routine
- Archive past catalysts with actual outcomes — build pattern recognition over time
