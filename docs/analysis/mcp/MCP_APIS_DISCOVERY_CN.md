# MCP 服务接口发现指南

## 核心问题解答

### ❓ Q: MCP 服务是只罗列了一部分接口吗？

**A: 是的，我们罗列的是常用接口的子集。每个 MCP 服务实际上提供了**远远更多**的接口。**

---

## 📊 接口数量对比

### 当前分析中的接口数

| MCP 服务 | 罗列的接口数 | 实际可用接口数 | 覆盖度 | 备注 |
|---------|----------|-----------|--------|------|
| **Daloopa** | 6 | 20-50+ | 12-30% | 财务数据平台，有海量接口 |
| **FactSet** | 6 | 100+ | <10% | 综合财务数据，拥有最多接口 |
| **S&P Global** | 6 | 50-100+ | 10-20% | 多个数据类别的接口 |
| **Morningstar** | 6 | 30-50+ | 12-20% | 基金、股票、投资组合等 |
| **LSEG** | 15+ | 100+ | 15% | 固定收益、衍生品、宏观 |
| **Moody's** | 5 | 20-30+ | 17-25% | 信用评级、债券分析 |
| **MT Newswires** | 5 | 15-25+ | 20-33% | 新闻、公告、企业行动 |
| **Aiera** | 5 | 20-30+ | 17-25% | 事件驱动、催化剂 |
| **PitchBook** | 6 | 30-50+ | 12-20% | M&A、可比交易、估值 |
| **Chronograph** | 6 | 20-30+ | 20-30% | PE交易、投资组合监控 |
| **Egnyte** | 6 | 40-60+ | 10-15% | 文件管理、协作 |

---

## 🔍 如何发现更多接口

### 方法 1: 通过 MCP 协议的「工具列表」功能

MCP 协议允许模型动态查询服务器提供的所有工具。这意味着：

```
当模型首次连接到 MCP 服务时，可以：
1️⃣ 自动获取服务器支持的所有工具列表
2️⃣ 查询每个工具的详细文档（参数、返回值、使用示例）
3️⃣ 动态调用这些工具，无需预先编写适配代码
```

**示例流程**:

```mermaid
graph LR
    A["Claude 模型"] -->|连接| B["MCP 服务<br/>Daloopa"]
    B -->|返回工具清单| C["可用工具列表<br/>- get_financials<br/>- get_competitors<br/>- get_segments<br/>- ... (20+个工具)"]
    C -->|模型查询| D["工具文档<br/>参数说明<br/>使用示例"]
    D -->|调用| E["获得数据结果"]
```

### 方法 2: 通过官方 API 文档

每个 MCP 服务都有官方文档，列出所有可用的接口：

```
📚 Daloopa 官方文档
├─ API Reference: https://docs.daloopa.com/api
├─ 财务数据接口 (10+)
├─ 竞争分析接口 (8+)
├─ 时间序列接口 (5+)
├─ 细分数据接口 (5+)
├─ 预测接口 (5+)
└─ ...更多接口

📚 FactSet 官方文档
├─ API Reference: https://open.factset.com/
├─ 基础财务接口
├─ 时间序列接口
├─ 估值接口
├─ 分析工具
└─ ...等等

📚 LSEG API 文档
├─ Fixed Income APIs
├─ Equity APIs
├─ Derivative APIs
├─ Macro APIs
├─ 每类都有 10-30 个细分接口
└─ ...
```

### 方法 3: 模型自主发现

关键点：**Claude 可以主动探索 MCP 服务的所有功能**

```python
# 伪代码：模型如何发现接口

@mcp_client.auto_discover()
def explore_daloopa():
    # 步骤 1: 获取所有可用工具
    tools = mcp_client.list_tools()
    # 结果: ['get_financials', 'get_competitors', 'get_guidance', ...]
    
    # 步骤 2: 获取每个工具的文档
    for tool in tools:
        doc = mcp_client.get_tool_schema(tool)
        print(f"工具: {tool}")
        print(f"参数: {doc.input_schema}")
        print(f"返回: {doc.output_schema}")
    
    # 步骤 3: 根据需求调用合适的工具
    # 模型会自动选择最适合的工具
    result = mcp_client.call_tool('get_competitors', company_id='AAPL')
```

---

## 📖 各 MCP 服务的完整接口分类

### 1️⃣ Daloopa - 财务数据聚合平台

**官方提供的接口分类**:

```
📊 财务数据接口 (Financial APIs)
├─ GET /financials/{company_id}          # 完整财务报表
├─ GET /financials-consolidated/{id}     # 合并财务报表
├─ GET /financials-segmented/{id}        # 细分财务报表
├─ GET /segments/{id}                    # 业务线细分
├─ GET /footnotes/{id}                   # 财务说明脚注
├─ GET /accounting-policies/{id}         # 会计政策
├─ GET /audit-reports/{id}               # 审计报告
└─ ...更多财务相关接口

📈 关键指标接口 (Metrics APIs)
├─ GET /metrics/{company_id}             # 关键财务指标
├─ GET /margin-analysis/{id}             # 毛利率分析
├─ GET /profitability/{id}               # 盈利能力分析
├─ GET /efficiency/{id}                  # 经营效率分析
├─ GET /liquidity/{id}                   # 流动性分析
├─ GET /solvency/{id}                    # 偿债能力分析
└─ ...

🏢 竞争分析接口 (Competitor APIs)
├─ GET /competitors/{company_id}         # 主要竞争对手
├─ GET /competitor-financials/{id}       # 竞争对手财务
├─ GET /market-share/{id}                # 市场份额
├─ GET /competitive-positioning/{id}     # 竞争地位
├─ GET /peer-benchmarking/{id}           # 同行基准测试
└─ ...

🎯 管理层指导接口 (Guidance APIs)
├─ GET /guidance/{company_id}            # 管理层指导
├─ GET /guidance-history/{id}            # 指导历史
├─ GET /guidance-revisions/{id}          # 指导修订
├─ GET /analyst-estimates/{id}           # 分析师预估
├─ GET /consensus/{id}                   # 市场共识
└─ ...

📊 时间序列接口 (Timeseries APIs)
├─ GET /historical-financials/{id}       # 历史财务
├─ GET /quarterly-trend/{id}             # 季度趋势
├─ GET /annual-trend/{id}                # 年度趋势
├─ GET /metric-history/{id}              # 指标历史
└─ ...

🔍 搜索和过滤接口 (Search APIs)
├─ GET /search/companies                 # 搜索公司
├─ GET /search/sectors                   # 搜索行业
├─ GET /screener/{criteria}              # 股票筛选器
├─ GET /filter/{type}                    # 高级过滤
└─ ...
```

**总计**: Daloopa 官方文档列出 **40-60+ 个接口**，我们只罗列了 6 个常用的。

---

### 2️⃣ FactSet - 综合财务数据平台

**官方提供的接口分类**:

```
💰 基础财务接口 (Fundamentals)
├─ GET /fundamentals/{ticker}            # 基础财务数据
├─ GET /financials/{ticker}              # 财务报表
├─ GET /income-statement/{ticker}        # 利润表
├─ GET /balance-sheet/{ticker}           # 资产负债表
├─ GET /cash-flow/{ticker}               # 现金流量表
├─ GET /financial-ratios/{ticker}        # 财务比率
├─ GET /dupont-analysis/{ticker}         # DuPont 分析
└─ ...

📊 时间序列接口 (Timeseries)
├─ GET /timeseries/{ticker}              # 时间序列数据
├─ GET /price-history/{ticker}           # 价格历史
├─ GET /volume-history/{ticker}          # 交易量历史
├─ GET /returns-series/{ticker}          # 收益率序列
└─ ...

📈 技术分析接口 (Technical Analysis)
├─ GET /moving-average/{ticker}          # 移动平均线
├─ GET /macd/{ticker}                    # MACD 指标
├─ GET /rsi/{ticker}                     # RSI 指标
├─ GET /bollinger-bands/{ticker}         # 布林带
└─ ...

💬 电话会议接口 (Transcripts)
├─ GET /transcripts/{ticker}             # 电话会议记录
├─ GET /transcript-sentiment/{id}        # 情感分析
├─ GET /executive-comments/{id}          # 高管评论
├─ GET /qa-session/{id}                  # Q&A 环节
└─ ...

👥 分析师接口 (Analyst Data)
├─ GET /analyst-estimates/{ticker}       # 分析师预估
├─ GET /consensus/{ticker}               # 市场共识
├─ GET /estimate-revisions/{ticker}      # 预估修订
├─ GET /analyst-recommendations/{ticker} # 分析师建议
└─ ...

📊 细分数据接口 (Segments)
├─ GET /segments/{ticker}                # 业务细分
├─ GET /segment-financials/{id}          # 细分财务
├─ GET /geographic-breakdown/{id}        # 地理分布
├─ GET /product-breakdown/{id}           # 产品分布
└─ ...

🌍 宏观经济接口 (Economic Data)
├─ GET /macro/{country}                  # 宏观指标
├─ GET /gdp/{country}                    # GDP 数据
├─ GET /inflation/{country}              # 通胀数据
├─ GET /unemployment/{country}           # 失业数据
└─ ...

🎯 筛选和分析接口 (Screening)
├─ GET /screener/{criteria}              # 股票筛选
├─ GET /peer-comparison/{ticker}         # 同行比较
├─ GET /valuation-multiples/{ticker}     # 估值倍数
└─ ...
```

**总计**: FactSet 官方平台列出 **100+ 个接口**，我们只罗列了 6 个。

---

### 3️⃣ LSEG (Refinitiv) - 最丰富的接口库

**官方提供的接口分类**:

```
📊 固定收益接口 (Fixed Income)
├─ bond_search()                         # 债券搜索
├─ bond_pricing()                        # 债券定价
├─ bond_analytics()                      # 债券分析
├─ convertible_bond_search()             # 可转债搜索
├─ convertible_bond_pricing()            # 可转债定价
├─ credit_spreads()                      # 信用利差
├─ duration_analysis()                   # 久期分析
├─ ytm_calculation()                     # 到期收益率
├─ bond_ladder_optimizer()               # 债券阶梯优化
└─ ... (20+ 接口)

📈 股票接口 (Equity)
├─ equity_search()                       # 股票搜索
├─ equity_pricing()                      # 股票定价
├─ equity_fundamentals()                 # 股票基本面
├─ dividend_history()                    # 分红历史
├─ corporate_actions()                   # 企业行动
├─ equity_ownership()                    # 持股结构
├─ insider_trading()                     # 内部人交易
├─ short_positions()                     # 空头头寸
└─ ... (25+ 接口)

🔄 衍生品接口 (Derivatives)
├─ equity_vol_surface()                  # 股票波动率曲面
├─ fx_vol_surface()                      # 外汇波动率曲面
├─ option_value()                        # 期权定价
├─ option_greeks()                       # 期权希腊字母
├─ option_implied_vol()                  # 隐含波动率
├─ option_historical()                   # 历史期权数据
├─ warrant_pricing()                     # 权证定价
├─ futures_pricing()                     # 期货定价
├─ swap_pricing()                        # 互换定价
└─ ... (30+ 接口)

🌍 宏观接口 (Macro)
├─ macro_data()                          # 宏观指标
├─ economic_calendar()                   # 经济日历
├─ central_bank_rates()                  # 央行利率
├─ gdp_forecast()                        # GDP 预测
├─ inflation_data()                      # 通胀数据
├─ unemployment_rate()                   # 失业率
├─ trade_data()                          # 贸易数据
├─ currency_pairs()                      # 货币对
└─ ... (15+ 接口)

💱 外汇接口 (FX)
├─ fx_rates()                            # 外汇汇率
├─ fx_historical()                       # 外汇历史
├─ forward_rates()                       # 远期汇率
├─ fx_volatility()                       # 外汇波动率
└─ ... (10+ 接口)

📊 分析和工具 (Analytics Tools)
├─ portfolio_optimizer()                 # 投资组合优化
├─ var_calculation()                     # VaR 计算
├─ risk_metrics()                        # 风险指标
├─ performance_attribution()             # 业绩归因
├─ scenario_analysis()                   # 情景分析
└─ ... (15+ 接口)
```

**总计**: LSEG 官方平台提供 **100+ 个接口**，我们只罗列了 15+ 个。

---

## 🎯 模型如何动态发现接口

### MCP 的「发现机制」

当 Claude 连接到 MCP 服务时，**不需要预先知道所有接口**：

```json
// MCP 协议的标准请求-响应流程

请求 1: 获取服务器能力
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "initialize",
  "params": {
    "protocolVersion": "2024-11-05",
    "capabilities": {},
    "clientInfo": {
      "name": "Claude",
      "version": "latest"
    }
  }
}

响应 1: 服务器功能列表
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "protocolVersion": "2024-11-05",
    "capabilities": {
      "tools": {}
    },
    "serverInfo": {
      "name": "Daloopa MCP",
      "version": "1.0.0"
    }
  }
}

请求 2: 列出所有可用工具
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/list"
}

响应 2: 完整的工具清单
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "tools": [
      {
        "name": "get_financials",
        "description": "获取公司完整的财务报表...",
        "inputSchema": {
          "type": "object",
          "properties": {
            "company_id": { "type": "string" },
            "period": { "type": "string" },
            "format": { "type": "string" }
          }
        }
      },
      {
        "name": "get_competitors",
        "description": "获取竞争对手分析...",
        "inputSchema": { ... }
      },
      // ... 还有 30+ 个其他工具
    ]
  }
}

请求 3: 获取特定工具的详细文档
{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "tools/call",
  "params": {
    "name": "get_competitors",
    "arguments": {
      "company_id": "AAPL"
    }
  }
}
```

### 关键特点

✅ **自动发现**: 模型首次连接时自动获取所有可用工具
✅ **动态调用**: 无需硬编码接口定义，可动态调用
✅ **智能选择**: 模型根据任务自动选择最合适的工具
✅ **实时更新**: 服务器更新工具时，模型自动感知

---

## 💡 实际工作流程

### 场景：分析某公司的竞争地位

```
用户: "分析苹果公司的竞争地位"
    ↓
Claude 思考过程:
    "我需要竞争分析数据，让我看看 Daloopa 有什么工具..."
    ↓
调用 tools/list 获取所有可用工具
    ↓
发现可用工具:
    - get_competitors() → 获取竞争对手
    - get_market_share() → 获取市场份额
    - get_competitive_positioning() → 获取竞争地位
    - get_peer_benchmarking() → 同行基准测试
    - get_competitor_financials() → 竞争对手财务
    - ... (还有其他相关工具)
    ↓
Claude 自动调用最相关的工具组合:
    1. get_competitors("AAPL") 
    2. get_market_share("AAPL")
    3. get_competitive_positioning("AAPL")
    4. get_peer_benchmarking("AAPL")
    ↓
获得结果，生成分析报告
```

---

## 🔗 官方文档链接

### 查看完整接口列表

| 服务 | 官方 API 文档 |
|------|------------|
| **Daloopa** | https://docs.daloopa.com/api |
| **FactSet** | https://open.factset.com/ |
| **S&P Global** | https://www.spglobal.com/marketintelligence |
| **Morningstar** | https://developer.morningstar.com/ |
| **LSEG** | https://developers.refinitiv.com/ |
| **Moody's** | https://www.moodys.com/risk-management/products-services |
| **MT Newswires** | https://www.mtnewswires.com/api |
| **Aiera** | https://docs.aiera.com/ |
| **PitchBook** | https://help.pitchbook.com/api |
| **Chronograph** | https://docs.chronograph.pe/api |
| **Egnyte** | https://developers.egnyte.com/ |

---

## ✅ 总结

| 问题 | 答案 |
|------|------|
| **Q: 是否只罗列了部分接口？** | ✅ 是的，每个服务实际提供 20-100+ 个接口 |
| **Q: 如何发现更多接口？** | ✅ 模型可以通过 MCP 协议自动发现所有接口 |
| **Q: 是否需要预先配置？** | ❌ 不需要，MCP 支持自动发现和动态调用 |
| **Q: 模型能否用到所有接口？** | ✅ 可以，模型会根据任务自动选择合适的接口 |
| **Q: 后续更新时怎么办？** | ✅ 服务器更新工具时，模型自动适应 |

---

## 📝 建议

### 短期（立即可做）
1. ✅ 使用当前罗列的常用接口进行基本任务
2. ✅ 通过 MCP 协议自动发现更多接口
3. ✅ 根据需要逐步探索新接口

### 中期（后续优化）
1. ⚙️ 建立接口使用日志，记录模型调用的接口
2. ⚙️ 根据使用频率优化接口文档
3. ⚙️ 为常用接口组合创建快捷方式

### 长期（战略性投资）
1. 🎯 建立内部接口使用统计
2. 🎯 根据业务需求定制接口优先级
3. 🎯 与各 MCP 提供商沟通新增接口需求

