# Catalyst Calendar

description: Build and maintain a catalyst calendar for the coverage portfolio — earnings dates, conferences, product launches, regulatory decisions, and macro events. Helps prioritize attention and position around events. Triggers on "catalyst calendar", "upcoming events", "what's coming up", "earnings calendar", "event calendar", or "catalyst tracking".

## Workflow

### Step 1: Define Coverage Scope

- List of companies to track (tickers or names)
- Sector / industry focus
- Include macro events? (FOMC meetings, economic data, regulatory deadlines)
- Time horizon (next 2 weeks, 1 month, 1 quarter)

### Step 2: Collect Catalysts

For each company, identify upcoming events:

**Earnings and financial events**
- Quarterly earnings dates and timing (pre-market / after-hours)
- Annual shareholder meetings
- Investor day / analyst day
- Capital markets day
- Debt maturity / refinancing dates

**Corporate events**
- Product launches or announcements
- FDA approvals / regulatory decisions
- Contract renewals or expirations
- M&A milestones (closing dates, regulatory approvals)
- Management changes
- Insider trading windows (lockup expirations)

**Industry events**
- Major conferences (dates, which companies participate)
- Trade shows
- Regulatory comment periods or rulings
- Industry data releases (monthly sales, traffic, etc.)

**Macro events**
- FOMC meetings (Fed dates)
- Jobs report, CPI, GDP releases
- Central bank decisions (ECB, BoJ, etc.)
- Geopolitical events affecting markets

### Step 3: Calendar View

| Date | Event | Company / Sector | Type | Impact (H/M/L) | Our Position | Notes |
|------|-------|------------------|------|---------------|--------------|-------|
| | | | Earnings/Corporate/Industry/Macro | | Long/Short/Neutral | |

### Step 4: Weekly Preview

Generate a forward-looking weekly summary:

**Key events this week:**
1. [Date]: [Company] Q[X] earnings — consensus [$X EPS], our estimate [$X], key focus: [metric]
2. [Date]: [Event] — why it matters for [stock]
3. [Date]: [Macro release] — expectations and our view

**Next week preview:**
- Advance notice of upcoming important events

**Positioning implications:**
- Events that may affect specific positions
- Any suggested pre-positioning
- Risk management ahead of binary events

### Step 5: Output

- Excel workbook with calendar view and sortable columns
- Weekly preview email/note (Markdown)
- Optional: integration with Google Calendar

## Important Notes

- Earnings dates shift — verify with company IR and Bloomberg/FactSet as the date approaches
- Pre-announcement risk: track companies with a pre-announcement history (positive or negative)
- Conference attendance lists are valuable — which companies participate, which are conspicuously absent?
- Some catalysts are recurring (monthly industry data) — build templates and auto-populate
- Color-code by impact level: red = high, yellow = medium, green = routine
- Archive past catalysts and actual outcomes — build pattern recognition over time
