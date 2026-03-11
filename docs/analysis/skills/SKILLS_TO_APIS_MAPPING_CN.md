# Skills → MCP 接口调用映射表

## 📊 完整的接口使用矩阵

本文档显示每个Skill具体会调用哪些MCP接口，以及这些接口的具体参数。

---

## 1️⃣ Initiating Coverage (Equity Research)

### Task 1: Company Research

**主要数据需求**: 公司背景、管理层、竞争分析、行业背景

```
调用流程：

1. Daloopa.get_company_profile(ticker="AAPL")
   ├─ 返回: 公司名称、行业、总部、网站、成立年份
   └─ 用途: "Overview" 部分

2. Daloopa.get_management_team(ticker="AAPL")
   ├─ 返回: CEO、CFO、主要高管、简历
   └─ 用途: "Management & Organization" 部分

3. Daloopa.get_business_segments(ticker="AAPL")
   ├─ 返回: 主要业务线、收入占比、地理分布
   └─ 用途: "Business Model & Segments" 部分

4. Daloopa.get_competitive_analysis(ticker="AAPL")
   ├─ 返回: 竞争对手、市场份额、竞争优势
   └─ 用途: "Competitive Positioning" 部分

5. S&P Global.get_industry_analysis(sector_code="Technology")
   ├─ 返回: 行业增长率、行业利润率、行业吸引力
   └─ 用途: "Industry Outlook" 部分

6. S&P Global.get_industry_trends(sector_code="Technology")
   ├─ 返回: 最新行业趋势、新兴威胁、机遇
   └─ 用途: "Industry Dynamics" 部分

7. MT Newswires.get_company_news(ticker="AAPL", limit=20)
   ├─ 返回: 最近新闻、公告、新闻日期
   └─ 用途: "Recent News & Updates" 部分

8. MT Newswires.get_corporate_actions(ticker="AAPL")
   ├─ 返回: 分拆、并购、股权激励、重组
   └─ 用途: "Corporate Actions" 部分

9. Aiera.get_earnings_call_calendar(ticker="AAPL")
   ├─ 返回: 下一次盈利电话会议时间、地点
   └─ 用途: "Upcoming Events" 部分

10. FactSet.get_analyst_estimates(ticker="AAPL", period="FY1")
    ├─ 返回: EPS、收入、EBITDA 预估
    └─ 用途: 背景上下文

输出: 6,000-8,000 字的研究文档 (Markdown)
```

### Task 2: Financial Modeling

**主要数据需求**: 历史财务、分析师指导、分红政策

```
调用流程：

1. Daloopa.get_historical_financials(ticker="AAPL", period=5)
   ├─ 返回: 过去5年的完整财务报表(收入、EBIT、净利润等)
   └─ 用途: 模型的历史年数据

2. Daloopa.get_guidance_data(ticker="AAPL")
   ├─ 返回: 管理层指导(收入增长预期、利润率预期)
   └─ 用途: 确定增长率假设

3. FactSet.get_analyst_estimates(ticker="AAPL", period=["FY1", "FY2"])
   ├─ 返回: 分析师共识预估
   └─ 用途: 验证增长率合理性

4. FactSet.get_consensus_estimates(ticker="AAPL")
   ├─ 返回: 市场共识(EPS、收入等)
   └─ 用途: 参考市场预期

5. Morningstar.get_dividend_history(ticker="AAPL", years=10)
   ├─ 返回: 历史分红金额、支付比率、增长率
   └─ 用途: 分红模型假设

6. Daloopa.get_capital_structure(ticker="AAPL")
   ├─ 返回: 债务、股权、优先股、稀释效应
   └─ 用途: 资本结构分析

输出: Excel模型(6个标签页: 历史数据、假设、投影、三情景、敏感性、总结)
```

### Task 3: Valuation Analysis

**主要数据需求**: 可比公司倍数、行业基准、Beta

```
调用流程：

1. Daloopa.search_peer_companies(ticker="AAPL", criteria={
     "sector": "Technology",
     "market_cap_range": [100B, 1T],
     "business_model": "similar"
   })
   ├─ 返回: 10-15个可比公司
   └─ 用途: 选择可比公司样本

2. Daloopa.get_batch_financials(
     tickers=["MSFT", "GOOGL", "META", ...],
     metrics=["revenue", "ebitda", "net_income", "free_cash_flow"]
   )
   ├─ 返回: 批量财务数据
   └─ 用途: 计算可比倍数

3. S&P Global.get_valuation_benchmarks(sector="Technology")
   ├─ 返回: 行业平均倍数(P/E, EV/EBITDA, P/B)
   └─ 用途: 与行业基准比较

4. FactSet.get_current_prices(tickers=["AAPL", "MSFT", ...])
   ├─ 返回: 当前股价、市值
   └─ 用途: 计算倍数分母

5. FactSet.get_beta(ticker="AAPL")
   ├─ 返回: 股票Beta值
   └─ 用途: WACC计算中的风险溢价

6. FactSet.get_risk_free_rate()
   ├─ 返回: 无风险利率(通常为10年美债收益率)
   └─ 用途: WACC计算

输出: 估值分析文档 + Excel标签页(可比分析、折扣现金流、价格目标)
```

### Task 4: Chart Generation

**主要数据需求**: 时间序列数据、行业数据、基准数据

```
调用流程：

1. FactSet.get_historical_prices(
     ticker="AAPL",
     start_date="2018-01-01",
     end_date="2024-02-27",
     frequency="daily"
   )
   ├─ 返回: 完整的历史价格序列
   └─ 用途: 图1-3 (股价趋势图)

2. Daloopa.get_historical_financials(ticker="AAPL", period=10)
   ├─ 返回: 过去10年的财务数据
   └─ 用途: 图4-8 (收入、EBITDA、利润率趋势)

3. FactSet.get_analyst_estimates_history(ticker="AAPL")
   ├─ 返回: 历史分析师预估修订
   └─ 用途: 图9 (EPS修订趋势)

4. Daloopa.get_peer_multiples(
     tickers=["AAPL", "MSFT", "GOOGL", ...],
     multiples=["P/E", "EV/EBITDA", "P/B"]
   )
   ├─ 返回: 可比公司倍数
   └─ 用途: 图10-12 (倍数散点图、箱线图)

5. S&P Global.get_sector_performance(sector="Technology", period="5Y")
   ├─ 返回: 行业相对表现
   └─ 用途: 图13 (行业相对收益率)

6. MT Newswires.get_news_volume(ticker="AAPL", months=36)
   ├─ 返回: 月度新闻数量趋势
   └─ 用途: 图14 (新闻热度指数)

输出: 25-35 张PNG/JPG 图表
```

---

## 2️⃣ DCF Model Builder (Financial Analysis)

### Step 1-2: Data Retrieval & Historical Analysis

```
调用流程：

1. Daloopa.get_financials(ticker="AAPL", latest_period="LTM")
   ├─ 参数: ticker, period_type (年度/季度), format
   ├─ 返回: 最近12个月(LTM)的财务报表
   └─ 优先级: ⭐⭐⭐⭐⭐ (最关键)

2. Daloopa.get_historical_financials(ticker="AAPL", years=5)
   ├─ 返回: 过去5年的财务年报
   └─ 用途: 历史增长率、利润率分析

3. FactSet.get_analyst_estimates(
     ticker="AAPL",
     metrics=["EPS", "Revenue", "EBITDA"],
     periods=["FY1", "FY2"]
   )
   ├─ 返回: 市场共识预估(1-2年前瞻)
   └─ 用途: 验证增长假设

4. FactSet.get_guidance_revisions(ticker="AAPL")
   ├─ 返回: 管理层指导历史修订
   └─ 用途: 评估管理层的预测准确性

5. FactSet.get_current_stock_price(ticker="AAPL")
   ├─ 返回: 当前股价
   └─ 用途: DCF校验(当前价格 vs 内在价值)

6. FactSet.get_beta(ticker="AAPL")
   ├─ 返回: 股票Beta(系统风险)
   └─ 用途: WACC中的权益风险溢价

7. FactSet.get_risk_free_rate()
   ├─ 返回: 10年期国债收益率
   └─ 用途: WACC中的无风险利率

8. Morningstar.get_dividend_history(ticker="AAPL")
   ├─ 返回: 历史分红数据
   └─ 用途: 分红政策分析

9. Morningstar.get_share_buyback_history(ticker="AAPL")
   ├─ 返回: 历史回购数据
   └─ 用途: 资本配置政策分析

10. Daloopa.get_capital_expenditure_history(ticker="AAPL", years=5)
    ├─ 返回: 过去5年的资本支出
    └─ 用途: CapEx % of Revenue 假设

输出: 历史指标汇总(收入CAGR、利润率趋势、FCF margin)
```

### Step 3-5: Projections & Valuation

```
调用流程：

1. FactSet.get_industry_growth_rates(sector="Technology")
   ├─ 返回: 行业平均增长率
   └─ 用途: 验证投影增长率的合理性

2. S&P Global.get_sector_margin_benchmarks(sector="Technology")
   ├─ 返回: 行业平均利润率
   └─ 用途: 终值年假设的基准

3. FactSet.get_consensus_terminal_growth_rate()
   ├─ 返回: 市场隐含的终值增长率
   └─ 用途: 3-5%区间的选择

输出: 完整Excel模型(财务投影表、敏感性分析表、DCF估值总结)
```

---

## 3️⃣ Comparable Company Analysis (Financial Analysis)

### Core Workflow

```
调用流程：

第一步: 搜索可比公司
1. Daloopa.search_peer_companies(
     ticker="AAPL",
     criteria={
       "sector": "Technology",
       "business_model": "similar",
       "size_range": [50B, 1T]
     }
   )
   ├─ 返回: 竞争对手列表(10-15个公司)
   └─ 用途: 确定样本

第二步: 批量获取财务数据
2. Daloopa.get_batch_financials(
     tickers=["MSFT", "GOOGL", "META", "NVDA", ...],
     metrics=["revenue", "gross_profit", "ebitda", "net_income", "fcf"],
     period="LTM"
   )
   ├─ 返回: 所有公司的财务数据(一次调用)
   └─ 用途: 填充"Operating Metrics"部分

3. FactSet.get_batch_current_prices(tickers=[...])
   ├─ 返回: 当前市价、市值
   └─ 用途: 计算倍数分母

第三步: 获取行业基准
4. S&P Global.get_sector_multiples(sector="Technology")
   ├─ 返回: 行业平均倍数(P/E, EV/EBITDA, P/B等)
   └─ 用途: "Statistical Summary"部分的基准行

5. S&P Global.get_sector_margins(sector="Technology")
   ├─ 返回: 行业平均利润率
   └─ 用途: 毛利率、EBITDA利率基准

第四步: 计算和汇总
6. 本地计算所有倍数
   - P/E = 股价 / EPS
   - EV/EBITDA = (市值 + 债务 - 现金) / EBITDA
   - P/B = 市值 / 账面价值

输出: Excel Comps分析(公司数据表、倍数表、统计汇总)
```

**关键的隐含接口**:
- `get_batch_financials()` - 单次批量获取所有公司数据(而不是逐个调用)
- `search_peer_companies()` - 智能搜索而不是手动输入
- `get_sector_multiples()` - 获取行业基准而不是手工计算

---

## 4️⃣ Fixed Income Portfolio Analysis (LSEG)

### Core Workflow

```
调用流程：

第一步: 债券搜索和定价
1. LSEG.bond_search(
     criteria={
       "issuer_type": "corporate",
       "rating_range": ["AAA", "BB"],
       "maturity_range": [2, 10],
       "currency": "USD"
     }
   )
   ├─ 返回: 满足条件的债券列表
   └─ 用途: 样本筛选(可选，如果用户没有提供现有组合)

2. LSEG.bond_price(
     bond_ids=["US0378331005", "US0846701050", ...],
     pricing_date="2024-02-27"
   )
   ├─ 返回: 清价、脏价、收益率、久期、DV01、OAS
   └─ 用途: "Portfolio Summary"表中的收益率、久期、DV01

第二步: 参考数据和信用分析
3. LSEG.yieldbook_bond_reference(
     bond_ids=["US0378331005", ...]
   )
   ├─ 返回: 发行人、票面利率、到期日、评级、行业、国家
   └─ 用途: "Composition Breakdown"中的行业/评级/期限分布

4. Moody's.get_credit_rating(bond_id="US0378331005")
   ├─ 返回: 当前评级、历史评级、展望
   └─ 用途: 评级分析和展望变化

第三步: 现金流预测
5. LSEG.yieldbook_cashflow(
     bond_ids=["US0378331005", ...],
     projection_years=10
   )
   ├─ 返回: 未来现金流时间表(利息+本金)
   └─ 用途: "Cashflow Waterfall"表

6. 本地聚合 aggregate_cashflows()
   ├─ 将所有债券的现金流汇总为季度/年度
   └─ 用途: 组合级现金流展望

第四步: 情景分析和压力测试
7. LSEG.yieldbook_scenario(
     bond_ids=["US0378331005", ...],
     scenarios={
       "parallel_shift": [-200, -100, -50, 0, 50, 100, 200],  # 基点
       "curve_scenarios": ["bull_steepen", "bear_steepen", ...]
     }
   )
   ├─ 返回: 每个债券在每个情景下的价格变化
   └─ 用途: "Scenario P&L"表

8. LSEG.interest_rate_curve(
     currency="USD",
     curve_date="2024-02-27"
   )
   ├─ 返回: 完整的零息利率曲线
   └─ 用途: 基准收益率曲线参考

第五步: 风险指标
9. LSEG.fixed_income_risk_analytics(
     bond_ids=["US0378331005", ...],
     analytics_type=["effective_duration", "key_rate_duration", "convexity"]
   )
   ├─ 返回: 有效久期、关键利率久期、凸性
   └─ 用途: 风险分解(哪些债券/利率期限贡献最多的风险)

输出: PowerPoint 或 PDF 报告
```

**关键的隐含接口**:
- `bond_price(batch)` - 批量定价(而不是逐个)
- `aggregate_cashflows()` - 聚合功能
- `yieldbook_scenario()` - 标准情景库

---

## 5️⃣ Buyer List (Investment Banking)

### Core Workflow

```
调用流程：

第一步: 理解目标公司
(用户提供: 公司描述、规模、行业、地理位置)

第二步: 搜索战略买家
1. Daloopa.search_peer_companies(
     industry=user_industry,
     criteria={
       "market_position": "large",
       "geographic_presence": "global or regional",
       "business_type": ["direct_competitor", "adjacent_player", "vertical_integrator"]
     }
   )
   ├─ 返回: 潜在战略买家列表(30-50个)
   └─ 用途: 战略买家样本

2. S&P Global.get_strategic_buyer_database(
     sector=user_sector,
     criteria={"m_a_activity": "active"}
   )
   ├─ 返回: 最近12个月有并购活动的买家
   └─ 用途: 交叉验证，识别活跃买家

3. PitchBook.strategic_buyer_search(
     target_profile={
       "revenue_range": [X, Y],
       "growth_profile": user_target_growth,
       "synergy_potential": "high"
     }
   )
   ├─ 返回: PitchBook识别的战略买家
   └─ 用途: 第三方验证

4. Daloopa.get_batch_financials(
     tickers=[所有潜在买家],
     metrics=["revenue", "ebitda", "fcf", "net_debt"]
   )
   ├─ 返回: 财务能力评估数据
   └─ 用途: 判断"Financial Capacity"

第三步: 搜索PE买家
5. PitchBook.financial_sponsor_search(
     criteria={
       "fund_size": [100M, 5B],
       "sector_focus": [相关行业],
       "deal_size_range": [target_revenue_range],
       "investment_stage": "late stage / mature"
     }
   )
   ├─ 返回: 符合条件的PE基金列表(20-40个)
   └─ 用途: 财务买家样本

6. Chronograph.get_portfolio_companies(
     sector=user_sector
   )
   ├─ 返回: PE基金的投资组合公司
   └─ 用途: 识别"add-on"收购潜力

第四步: M&A历史和最近活动
7. MT Newswires.get_m_a_activity(
     buyer_tickers=[所有潜在买家],
     period="12M",
     status="completed"
   )
   ├─ 返回: 最近12个月的并购交易
   └─ 用途: "M&A Track Record"列

8. PitchBook.get_comparable_transactions(
     target_profile=user_target,
     period="3Y"
   )
   ├─ 返回: 相似交易的可比数据
   └─ 用途: 估值范围、交易结构参考

第五步: 联系人映射
(本地CRM搜索 + 手工研究)

输出: Excel 买家清单(战略买家表、PE买家表、Tier分类、联系人映射)
```

**关键的隐含接口**:
- `search_peer_companies()` - 智能搜索
- `search_financial_sponsors()` - PE基金搜索
- `get_m_a_activity()` - 交易历史
- `get_comparable_transactions()` - 可比交易

---

## 6️⃣ Equity Research Snapshot (LSEG)

### Core Workflow

```
调用流程：

1. FactSet.qa_ibes_consensus(
     ticker="AAPL",
     metrics=["EPS", "Revenue", "EBITDA", "DPS"],
     periods=["FY1", "FY2"]
   )
   ├─ 返回: 分析师共识(中位数、平均值、范围、分散度)
   └─ 用途: "Consensus Estimates"表

2. FactSet.qa_company_fundamentals(
     ticker="AAPL",
     periods=5  # 过去5个财政年度
   )
   ├─ 返回: 收入、毛利率、EBIT、ROE、ROIC等
   └─ 用途: "Financials Summary"表

3. FactSet.qa_historical_equity_price(
     ticker="AAPL",
     period="1Y"
   )
   ├─ 返回: 日线价格、收益率、Beta、52周范围
   └─ 用途: "Price Performance"计算

4. FactSet.tscc_historical_pricing_summaries(
     ticker="AAPL",
     frequency="daily",
     period="3M"
   )
   ├─ 返回: 3个月日线价格汇总
   └─ 用途: 近期成交量和动量分析

5. LSEG.qa_macroeconomic(
     indicators=["GDP", "CPI", "unemployment"],
     countries=["US", "China"]
   )
   ├─ 返回: 宏观经济指标
   └─ 用途: "Macro Backdrop"部分

输出: 研究快照文档
```

---

## 📋 接口使用频率排行榜

基于Skills分析，以下接口被使用最频繁：

### Top 20 Most Used Interfaces

| 排名 | 接口 | 服务 | 使用Skill数 | 使用频率 |
|-----|------|------|----------|---------|
| 1 | `get_batch_financials()` | Daloopa | 4 | ⭐⭐⭐⭐⭐ |
| 2 | `get_historical_financials()` | Daloopa | 3 | ⭐⭐⭐⭐⭐ |
| 3 | `get_analyst_estimates()` | FactSet | 3 | ⭐⭐⭐⭐⭐ |
| 4 | `search_peer_companies()` | Daloopa | 3 | ⭐⭐⭐⭐⭐ |
| 5 | `get_current_prices()` | FactSet | 3 | ⭐⭐⭐⭐ |
| 6 | `bond_price()` | LSEG | 1 | ⭐⭐⭐⭐⭐ |
| 7 | `get_dividend_history()` | Morningstar | 2 | ⭐⭐⭐⭐ |
| 8 | `get_company_profile()` | Daloopa | 2 | ⭐⭐⭐⭐ |
| 9 | `qa_ibes_consensus()` | FactSet | 2 | ⭐⭐⭐⭐ |
| 10 | `get_business_segments()` | Daloopa | 1 | ⭐⭐⭐ |
| 11 | `yieldbook_scenario()` | LSEG | 1 | ⭐⭐⭐⭐ |
| 12 | `search_financial_sponsors()` | PitchBook | 1 | ⭐⭐⭐ |
| 13 | `get_m_a_activity()` | MT Newswires | 2 | ⭐⭐⭐ |
| 14 | `fixed_income_risk_analytics()` | LSEG | 1 | ⭐⭐⭐ |
| 15 | `get_sector_multiples()` | S&P Global | 2 | ⭐⭐⭐ |
| 16 | `get_beta()` | FactSet | 1 | ⭐⭐⭐ |
| 17 | `yieldbook_bond_reference()` | LSEG | 1 | ⭐⭐⭐ |
| 18 | `get_comparable_transactions()` | PitchBook | 1 | ⭐⭐⭐ |
| 19 | `get_news()` | MT Newswires | 1 | ⭐⭐ |
| 20 | `qa_macroeconomic()` | LSEG | 1 | ⭐⭐⭐ |

**优化建议**:
- Top 5接口应该优化响应时间和缓存策略
- 批量接口(`get_batch_*`)比单笔接口使用更频繁
- 这20个接口覆盖了所有Skills的核心功能

---

## 🔄 接口依赖关系

### 数据流向图

```
用户输入 (Ticker/参数)
    ↓
[搜索接口] search_peer_companies()
    ↓
[批量获取] get_batch_financials()
    ↓
[实时数据] get_current_prices()
    ↓
[参考数据] get_sector_multiples(), yieldbook_bond_reference()
    ↓
[历史数据] get_historical_financials(), qa_historical_equity_price()
    ↓
[计算接口] 
├─ 倍数计算 (本地)
├─ 统计汇总 (本地)
├─ 情景分析 (yieldbook_scenario)
└─ 压力测试 (fixed_income_risk_analytics)
    ↓
[输出] Excel/Markdown/PowerPoint
```

---

## ✅ 结论

**为什么这个映射表重要**:

1. **完整性** - 展示了99个推断接口如何在实际Skills中被使用
2. **优先级** - 清楚地标示了哪些接口最常用
3. **依赖关系** - 理解接口之间的组合方式
4. **验证** - 可根据实际MCP日志验证推断的准确性

**下一步**:
- 通过启用MCP日志记录来验证这些推断
- 对比实际调用与推断调用
- 优化高频接口的响应时间和缓存
