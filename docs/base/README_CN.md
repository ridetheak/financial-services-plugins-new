# Claude for Financial Services 插件

将Claude变成金融服务专家的插件集——投资银行、股票研究、私募股权和财富管理。为[Claude Cowork](https://claude.com/product/cowork)设计，也兼容[Claude Code](https://claude.com/product/claude-code)。

## 为什么选择插件

Cowork让你设定目标，Claude负责交付成果。插件让你走得更远：告诉Claude你的公司如何进行分析、使用哪些数据源、如何处理关键工作流，以及公开哪些斜杠命令——这样你的团队就能获得更优质、更一致的成果。

每个插件都为特定的金融服务工作流整合了技能、连接器、斜杠命令和子代理。开箱即用，它们为Claude提供了一个强大的起点，帮助该角色的任何人工作。真正的威力来自于为你的公司定制——你的模型、你的模板、你的流程——让Claude工作得像是为你的团队量身定制的。

## 什么是Claude for Financial Services?

Claude for Financial Services是建立在Claude Enterprise之上的综合解决方案，具有金融分析的专业能力。它将Claude连接到金融专业人士日常使用的数据源和工具——无需在多个浏览器标签页之间切换，并改进源验证以降低手动数据收集错误的风险。

## 端到端工作流

这些插件不仅仅是一些点工具的集合——它们能够实现跨越研究、分析、建模和输出生成的完整工作流：

- **研究到报告**：从MCP提供商拉取实时数据，分析财务报告结果，生成可发布的股票研究报告——一切都在一个会话中完成
- **电子表格分析**：构建可比公司分析、DCF模型和LBO模型，生成功能完整的Excel工作簿，具有实时公式、敏感性分析和行业标准格式
- **财务建模**：从SEC申报表填充3表模型，根据同行数据交叉验证假设，压力测试场景——内置蓝/黑/绿色编码惯例
- **交易文件**：起草CIM、预告和流程信函，然后使用你公司的品牌PowerPoint模板生成演示稿幻灯片和概览
- **投资组合到演示文稿**：筛选机会、运行尽职调查清单、构建IC备忘录、跟踪投资组合关键指标——无缝地从数据转移到可交付成果

每个工作流都连接上游数据源（通过MCP）和下游输出（Excel、PowerPoint、Word），因此你可以从问题转移到完成的工作产品，而无需改变上下文。

## 插件市场

从**财务分析**开始——核心插件，提供共享建模工具和所有MCP数据连接器。然后添加任何特定函数的插件来增强Claude对你的工作流的能力。

| 插件 | 类型 | 功能 | 连接器 |
|------|------|------|--------|
| **[财务分析 (financial analysis)](./financial-analysis)** | 核心（必须首先安装） | 构建可比分析、DCF模型、LBO模型和3表财务报表。质量检查演示文稿并创建可重用的PPT模板。提供共享基础和所有数据连接器。 | Daloopa、Morningstar、S&P Global、FactSet、Moody's、MT Newswires、Aiera、LSEG、PitchBook、Chronograph、Egnyte |
| **[投资银行 (investment banking)](./investment-banking)** | 附加组件 | 起草CIM、预告和流程信函。构建买家名单、运行并购模型、创建概览、跟踪交易里程碑。 | — |
| **[股票研究 (equity research)](./equity-research)** | 附加组件 | 撰写财报更新和新研究报告。维护投资论点、跟踪催化剂、起草晨报、筛选新想法。 | — |
| **[私募股权 (private equity)](./private-equity)** | 附加组件 | 交易采购和筛选、运行尽职调查清单、分析单位经济学和回报、起草IC备忘录、监控投资组合公司关键指标。 | — |
| **[财富管理 (wealth management)](./wealth-management)** | 附加组件 | 客户会议准备、构建财务规划、投资组合再平衡、生成客户报告、识别税损收割机会。 | — |

**41个技能、38个命令、11个MCP集成**

直接从Cowork安装这些插件，浏览GitHub上的完整集合，或构建自己的插件。

### 合作伙伴构建的插件

这些插件由我们的数据合作伙伴构建和维护，将他们的金融数据和分析直接带入Claude工作流。

| 插件 | 合作伙伴 | 功能 |
|------|---------|------|
| **[LSEG](./partner-built/lseg)** | [LSEG](https://www.lseg.com/) | 使用LSEG金融数据和分析进行债券定价、收益率曲线分析、评估外汇套利交易、期权估值和建立宏观仪表板。包含8个命令，覆盖固定收益、外汇、股票和宏观。 |
| **[S&P Global](./partner-built/spglobal)** | [S&P Global](https://www.spglobal.com/) | 使用S&P Capital IQ数据生成公司概览、财报预览和融资摘要。支持多种观众类型（股票研究、IB/M&A、企业发展、销售）。 |

## 快速开始

### Cowork

从[claude.com/plugins](https://claude.com/plugins/)安装插件。

### Claude Code

```bash
# 添加市场
claude plugin marketplace add anthropics/financial-services-plugins

# 首先安装核心插件（必需）
claude plugin install financial-analysis@financial-services-plugins

# 然后根据需要添加特定函数的插件
claude plugin install investment-banking@financial-services-plugins
claude plugin install equity-research@financial-services-plugins
claude plugin install private-equity@financial-services-plugins
claude plugin install wealth-management@financial-services-plugins
```

安装后，插件会自动激活。技能在相关时触发，斜杠命令在你的会话中可用：

```bash
/comps [公司]                    # 可比公司分析
/dcf [公司]                      # DCF估值模型
/earnings [公司] [季度]          # 财报后更新报告
/one-pager [公司]                # 单页公司概览
/ic-memo [项目名称]              # 投资委员会备忘录
/source [条件]                   # 交易采购
/client-review [客户]            # 客户会议准备
```

## 插件如何工作

每个插件遵循相同的结构：

```
plugin-name/
├── .claude-plugin/plugin.json   # 清单
├── .mcp.json                    # 工具连接
├── commands/                    # 你明确调用的斜杠命令
└── skills/                      # Claude自动使用的领域知识
```

- **技能**编码了Claude需要提供专业质量金融工作的领域专业知识、最佳实践和分步工作流。Claude在相关时自动使用它们。
- **命令**是你触发的明确操作（例如`/comps`、`/earnings`、`/ic-memo`）。
- **连接器**通过[MCP服务器](https://modelcontextprotocol.io/)将Claude连接到你的工作流依赖的外部数据源——金融数据终端、研究平台、文档管理等。

每个组件都是基于文件的——markdown和JSON，无代码、无基础设施、无构建步骤。

## MCP集成

所有连接器都集中在**财务分析**核心插件中，并在所有附加插件中共享。

| 提供商 | URL |
|--------|-----|
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

> MCP访问可能需要来自相应提供商的订阅或API密钥。

## 让它们属于你

这些插件是起点。当你为公司实际的工作方式定制它们时，它们会变得更加有用：

- **交换连接器** — 编辑`.mcp.json`以指向你的特定数据提供商和内部工具。
- **添加公司背景** — 将你的术语、交易流程和格式标准放入技能文件，让Claude理解你的世界。
- **使用你的模板** — 使用`/ppt-template`教Claude你公司的品牌PowerPoint布局，这样每份演示文稿都符合你的风格指南。
- **调整工作流** — 修改技能说明以匹配你的团队实际进行分析的方式，而不是教科书所说的方式。
- **构建新插件** — 遵循上述结构为我们尚未涵盖的工作流创建插件。

随着你的团队构建和共享插件，Claude成为了跨职能专家。你定义的背景被融入到每个相关的交互中，因此领导者可以花更少的时间强制执行流程，花更多的时间改进流程。

## 贡献

插件只是markdown文件。Fork仓库、进行更改并提交PR。对于新技能或插件，请包括：

- 一个`SKILL.md`，带有清晰的触发条件和工作流步骤
- 如果用户可调用，在`commands/`中有相应的命令
- 如果添加新功能，更新的插件清单

## 许可证

[Apache License 2.0](./LICENSE)

## 免责声明

这些插件协助金融工作流，但不提供财务或投资建议。始终与合格的金融专业人士核实结论。在依赖AI生成的分析进行财务或投资决策之前，应由金融专业人士审查。
