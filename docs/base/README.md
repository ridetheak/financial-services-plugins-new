# Claude for Financial Services Plugins

A collection of plugins that turn Claude into a financial services expert — investment banking, equity research, private equity, and wealth management. Designed for [Claude Cowork](https://claude.com/product/cowork) and also compatible with [Claude Code](https://claude.com/product/claude-code).

## Why Plugins

Cowork lets you set objectives and Claude delivers results. Plugins take you further: tell Claude how your firm conducts analysis, which data sources you use, how to handle critical workflows, and which slash commands to expose — so your team gets higher-quality, more consistent output.

Each plugin integrates skills, connectors, slash commands, and sub-agents for a specific financial services workflow. Out of the box, they give Claude a powerful starting point for anyone working in that role. The real power comes from customizing them for your firm — your models, your templates, your processes — so Claude works as if it were built specifically for your team.

## What Is Claude for Financial Services?

Claude for Financial Services is a comprehensive solution built on Claude Enterprise, with specialized capabilities for financial analysis. It connects Claude to the data sources and tools that financial professionals use every day — eliminating the need to switch between multiple browser tabs — and improves source verification to reduce the risk of errors from manual data collection.

## End-to-End Workflows

These plugins are more than a collection of point tools — they enable complete workflows spanning research, analysis, modeling, and output generation:

- **Research to Report**: Pull live data from MCP providers, analyze earnings results, generate publishable equity research reports — all within a single session
- **Spreadsheet Analysis**: Build comparable company analyses, DCF models, and LBO models; generate fully functional Excel workbooks with live formulas, sensitivity analyses, and industry-standard formatting
- **Financial Modeling**: Populate three-statement models from SEC filings, cross-validate assumptions against peer data, stress-test scenarios — with blue/black/green coding conventions built in
- **Deal Documents**: Draft CIMs, teasers, and process letters, then generate presentation slides and overviews using your firm's branded PowerPoint templates
- **Portfolio to Presentation**: Screen opportunities, run due diligence checklists, build IC memos, track portfolio company key metrics — seamlessly moving from data to deliverables

Every workflow connects upstream data sources (via MCP) and downstream outputs (Excel, PowerPoint, Word), so you can move from question to finished work product without changing context.

## Plugin Marketplace

Start with **Financial Analysis** — the core plugin that provides shared modeling tools and all MCP data connectors. Then add any function-specific plugins to enhance Claude's understanding of your workflow.

| Plugin | Type | Capabilities | Connectors |
|--------|------|--------------|------------|
| **[Financial Analysis (financial analysis)](./financial-analysis)** | Core (must be installed first) | Build comparable analyses, DCF models, LBO models, and three-statement financials. Quality-check presentations and create reusable PPT templates. Provides the shared foundation and all data connectors. | Daloopa, Morningstar, S&P Global, FactSet, Moody's, MT Newswires, Aiera, LSEG, PitchBook, Chronograph, Egnyte |
| **[Investment Banking (investment banking)](./investment-banking)** | Add-on | Draft CIMs, teasers, and process letters. Build buyer lists, run M&A models, create overviews, track deal milestones. | — |
| **[Equity Research (equity research)](./equity-research)** | Add-on | Write earnings updates and initiation reports. Maintain investment theses, track catalysts, draft morning notes, screen for new ideas. | — |
| **[Private Equity (private equity)](./private-equity)** | Add-on | Deal sourcing and screening, due diligence checklists, unit economics and returns analysis, IC memo drafting, portfolio company KPI monitoring. | — |
| **[Wealth Management (wealth management)](./wealth-management)** | Add-on | Client meeting preparation, financial plan construction, portfolio rebalancing, client report generation, tax-loss harvesting identification. | — |

**41 skills, 38 commands, 11 MCP integrations**

Install these plugins directly from Cowork, browse the full collection on GitHub, or build your own.

### Partner-Built Plugins

These plugins are built and maintained by our data partners, bringing their financial data and analytics directly into Claude workflows.

| Plugin | Partner | Capabilities |
|--------|---------|--------------|
| **[LSEG](./partner-built/lseg)** | [LSEG](https://www.lseg.com/) | Bond pricing, yield curve analysis, FX carry trade evaluation, options valuation, and macro dashboard construction using LSEG financial data and analytics. Includes 8 commands covering fixed income, FX, equities, and macro. |
| **[S&P Global](./partner-built/spglobal)** | [S&P Global](https://www.spglobal.com/) | Generate company overviews, earnings previews, and financing summaries using S&P Capital IQ data. Supports multiple audience types (equity research, IB/M&A, corporate development, sales). |

## Quick Start

### Cowork

Install plugins from [claude.com/plugins](https://claude.com/plugins/).

### Claude Code

```bash
# Add the marketplace
claude plugin marketplace add anthropics/financial-services-plugins

# Install the core plugin first (required)
claude plugin install financial-analysis@financial-services-plugins

# Then add function-specific plugins as needed
claude plugin install investment-banking@financial-services-plugins
claude plugin install equity-research@financial-services-plugins
claude plugin install private-equity@financial-services-plugins
claude plugin install wealth-management@financial-services-plugins
```

After installation, plugins activate automatically. Skills trigger when relevant; slash commands are available in your session:

```bash
/comps [company]                 # Comparable company analysis
/dcf [company]                   # DCF valuation model
/earnings [company] [quarter]    # Post-earnings update report
/one-pager [company]             # Single-page company overview
/ic-memo [project name]          # Investment committee memo
/source [criteria]               # Deal sourcing
/client-review [client]          # Client meeting preparation
```

## How Plugins Work

Every plugin follows the same structure:

```
plugin-name/
├── .claude-plugin/plugin.json   # Manifest
├── .mcp.json                    # Tool connections
├── commands/                    # Slash commands you invoke explicitly
└── skills/                      # Domain knowledge Claude uses automatically
```

- **Skills** encode the domain expertise, best practices, and step-by-step workflows Claude needs to produce professional-quality financial work. Claude uses them automatically when relevant.
- **Commands** are explicit actions you trigger (e.g., `/comps`, `/earnings`, `/ic-memo`).
- **Connectors** connect Claude to the external data sources your workflows depend on — financial data terminals, research platforms, document management systems, and more — via [MCP servers](https://modelcontextprotocol.io/).

Every component is file-based — Markdown and JSON, no code, no infrastructure, no build steps.

## MCP Integrations

All connectors are centralized in the **Financial Analysis** core plugin and shared across all add-on plugins.

| Provider | URL |
|----------|-----|
| [Daloopa](https://www.daloopa.com/) | `https://mcp.daloopa.com/server/mcp` |
| [Morningstar](https://www.morningstar.com/) | `https://mcp.morningstar.com/mcp` |
| [S&P Global](https://www.spglobal.com/) | `https://kfinance.kensho.com/integrations/mcp` |
| [FactSet](https://www.factset.com/) | `https://mcp.factset.com/mcp` |
| [Moody's](https://www.moodys.com/) | `https://api.moodys.com/genai-ready-data/m1/mcp` |
| [MT Newswires](https://www.mtnewswires.com/) | `https://vast-mcp.blueskyapi.com/mtnewswires` |
| [Aiera](https://www.aiera.com/) | `https://mcp-pub.aiera.com` |
| [LSEG](https://www.lseg.com/) | `https://api.analytics.lseg.com/lfa/mcp` |
| [PitchBook](https://pitchbook.com/) | `https://premium.mcp.pitchbook.com/mcp` |
| [Chronograph](https://www.chronograph.pe/) | `https://ai.chronograph.pe/mcp` |
| [Egnyte](https://www.egnyte.com/) | `https://mcp-server.egnyte.com/mcp` |

> MCP access may require a subscription or API key from the respective provider.

## Make Them Your Own

These plugins are a starting point. They become far more useful when customized to match how your firm actually works:

- **Swap connectors** — Edit `.mcp.json` to point to your specific data providers and internal tools.
- **Add firm context** — Put your terminology, deal processes, and formatting standards into skill files so Claude understands your world.
- **Use your templates** — Use `/ppt-template` to teach Claude your firm's branded PowerPoint layout so every presentation conforms to your style guide.
- **Adjust workflows** — Modify skill instructions to match how your team actually conducts analysis, not how the textbook says to do it.
- **Build new plugins** — Follow the structure above to create plugins for workflows we haven't covered yet.

As your team builds and shares plugins, Claude becomes a cross-functional expert. The context you define is woven into every relevant interaction, so leaders can spend less time enforcing process and more time improving it.

## Contributing

Plugins are just Markdown files. Fork the repository, make changes, and submit a PR. For new skills or plugins, include:

- A `SKILL.md` with clear trigger conditions and workflow steps
- A corresponding command in `commands/` if user-invocable
- An updated plugin manifest if adding new capabilities

## License

[Apache License 2.0](./LICENSE)

## Disclaimer

These plugins assist with financial workflows but do not provide financial or investment advice. Always verify conclusions with qualified financial professionals. AI-generated analysis should be reviewed by a financial professional before being relied upon for financial or investment decisions.
