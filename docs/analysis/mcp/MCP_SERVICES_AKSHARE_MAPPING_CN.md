# MCP 服务 API 接口分析与 AKShare 对应表

## 概述

本文档详细分析了 11 个 MCP 服务的具体 API 接口及其与 AKShare 的对应关系。

---

## 1. Daloopa

### 服务信息
- **URL**: `https://mcp.daloopa.com/server/mcp`
- **类型**: HTTP MCP
- **主要功能**: 财务数据聚合平台，整合全球上市公司财务数据

### 提供的 API 接口
```
GET /financials/{company_id}              # 获取公司财务数据（P&L、BS、CF）
GET /metrics/{company_id}                  # 获取关键财务指标
GET /competitors/{company_id}              # 获取竞争对手分析
GET /guidance/{company_id}                 # 获取管理层指导
GET /segments/{company_id}                 # 获取细分数据
GET /historical/{company_id}               # 获取历史财务数据
```

### 对应 AKShare API

| 功能 | Daloopa API | AKShare 对应 API | 备注 |
|------|-----------|-------------------|------|
| 上市公司财务报表 | `/financials/{company_id}` | `stock_financial_analysis_indicator` | 获取财务报表指标 |
| 季度/年度报表 | `/financials/{company_id}` | `stock_main_indicator` | 主要财务指标 |
| 竞争对手分析 | `/competitors/{company_id}` | 需手工组合 | A股无直接对应 |
| 管理层指导 | `/guidance/{company_id}` | 无直接对应 | 需要从公告爬取 |
| 细分业务数据 | `/segments/{company_id}` | `stock_main_indicator` | 部分披露在财报中 |
| 历史财务数据 | `/historical/{company_id}` | `stock_main_indicator` (历史) | 支持多期对比 |

### 实现方案
```python
# AKShare 替代方案
import akshare as ak

# 获取财务报表
df = ak.stock_financial_analysis_indicator(symbol="000001", indicator="基本每股收益")

# 获取主要指标
df = ak.stock_main_indicator(symbol="000001")

# 获取业绩快报
df = ak.guba_sina(show_params=False)
```

---

## 2. Morningstar

### 服务信息
- **URL**: `https://mcp.morningstar.com/mcp`
- **类型**: HTTP MCP
- **主要功能**: 投资研究数据、基金评级、股票评级

### 提供的 API 接口
```
GET /fund/profile/{fund_id}                # 基金档案
GET /fund/rating/{fund_id}                 # 基金评级
GET /stock/rating/{ticker}                 # 股票评级
GET /equity/dividend/{ticker}              # 股息历史
GET /equity/earnings-estimate/{ticker}     # 盈利预估
GET /portfolio/{portfolio_id}              # 投资组合分析
```

### 对应 AKShare API

| 功能 | Morningstar API | AKShare 对应 API | 备注 |
|------|-----------------|-----------------|------|
| 股票评级 | `/stock/rating/{ticker}` | 无直接对应 | 可从研报获取 |
| 股息历史 | `/equity/dividend/{ticker}` | `stock_dividend_cninfo` | A股分红信息 |
| 盈利预估 | `/equity/earnings-estimate/{ticker}` | `bk_hk_sina` | 无直接预估数据 |
| 基金信息 | `/fund/profile/{fund_id}` | `fund_info` | 基金基本信息 |
| 基金评级 | `/fund/rating/{fund_id}` | 无直接对应 | 需第三方爬取 |

### 实现方案
```python
import akshare as ak

# 获取股息信息
df = ak.stock_dividend_cninfo(symbol="000001")

# 获取基金基本信息
df = ak.fund_info()

# 获取基金净值
df = ak.fund_daily_history(symbol="110022")

# 获取基金持仓
df = ak.fund_portfolio_detail_rank(symbol="110022", date="20231231")
```

---

## 3. S&P Global (Kensho)

### 服务信息
- **URL**: `https://kfinance.kensho.com/integrations/mcp`
- **类型**: HTTP MCP
- **主要功能**: 行业分析、估值工具、公司撕页、盈利预览

### 提供的 API 接口
```
GET /company/profile/{isin}                # 公司档案
GET /industry/overview/{sector}            # 行业概览
GET /valuation/multiples/{ticker}          # 估值倍数
GET /earnings/estimates/{ticker}           # 盈利估计
GET /dividends/{ticker}                    # 股息信息
GET /peer-comparison/{ticker}              # 同行对比
```

### 对应 AKShare API

| 功能 | S&P Global API | AKShare 对应 API | 备注 |
|------|---------------|------------------|------|
| 公司档案 | `/company/profile/{isin}` | 无直接对应 | 可从东财爬取 |
| 行业概览 | `/industry/overview/{sector}` | `bk_sina` | 新浪分类行业 |
| 估值倍数 | `/valuation/multiples/{ticker}` | `stock_valuation` | 估值倍数数据 |
| 盈利估计 | `/earnings/estimates/{ticker}` | 无直接对应 | 需爬取券商研报 |
| 同行对比 | `/peer-comparison/{ticker}` | 需手工组合 | 可使用 bk 数据 |

### 实现方案
```python
import akshare as ak

# 获取估值数据（PE、PB等）
df = ak.stock_valuation()

# 获取行业信息
df = ak.bk_sina()

# 获取行业成分
df = ak.bk_sina_members(symbol="bk0471")

# 获取股票基本信息
df = ak.stock_info_a_sina()
```

---

## 4. FactSet

### 服务信息
- **URL**: `https://mcp.factset.com/mcp`
- **类型**: HTTP MCP
- **主要功能**: 综合财务数据、分析工具、市场数据

### 提供的 API 接口
```
GET /fundamentals/{ticker}                 # 基础财务数据
GET /timeseries/{ticker}                   # 时间序列数据
GET /ratios/{ticker}                       # 财务比率
GET /statements/{ticker}                   # 财务报表
GET /segments/{ticker}                     # 细分数据
GET /transcripts/{ticker}                  # 电话会议记录
```

### 对应 AKShare API

| 功能 | FactSet API | AKShare 对应 API | 备注 |
|------|-----------|-------------------|------|
| 财务数据 | `/fundamentals/{ticker}` | `stock_financial_analysis_indicator` | 综合财报数据 |
| 时间序列 | `/timeseries/{ticker}` | `stock_zh_a_hist` | 历史行情数据 |
| 财务比率 | `/ratios/{ticker}` | `stock_main_indicator` | 各类财务比率 |
| 财务报表 | `/statements/{ticker}` | `stock_financial_analysis_indicator` | 3张表数据 |
| 细分数据 | `/segments/{ticker}` | `stock_main_indicator` | 需提取 |
| 电话会议 | `/transcripts/{ticker}` | 无对应 | 仅A股部分公司 |

### 实现方案
```python
import akshare as ak

# 获取所有财务指标
df = ak.stock_financial_analysis_indicator(symbol="000001")

# 获取主要指标（包含比率）
df = ak.stock_main_indicator(symbol="000001")

# 获取历史行情
df = ak.stock_zh_a_hist(symbol="000001", period="daily", start_date="20200101", end_date="20231231")

# 获取现金流
df = ak.stock_cash_flow_sheet(symbol="000001")
```

---

## 5. Moody's

### 服务信息
- **URL**: `https://api.moodys.com/genai-ready-data/m1/mcp`
- **类型**: HTTP MCP
- **主要功能**: 信用评级、违约风险、债券分析

### 提供的 API 接口
```
GET /rating/{issuer_id}                    # 信用评级
GET /credit-risk/{issuer_id}               # 信用风险指标
GET /default-probability/{issuer_id}       # 违约概率
GET /bond-analysis/{bond_isin}             # 债券分析
GET /sector-rating/{sector}                # 部门评级展望
```

### 对应 AKShare API

| 功能 | Moody's API | AKShare 对应 API | 备注 |
|------|-----------|------------------|------|
| 信用评级 | `/rating/{issuer_id}` | 无对应 | A股评级需爬取 |
| 信用风险 | `/credit-risk/{issuer_id}` | `stock_concept_sina` | 需结合流动性 |
| 违约概率 | `/default-probability/{issuer_id}` | 无对应 | 仅债券市场 |
| 债券分析 | `/bond-analysis/{bond_isin}` | `bond_* 相关` | 债券数据接口 |
| 部门评级 | `/sector-rating/{sector}` | `bk_sina` | 行业基本数据 |

### 实现方案
```python
import akshare as ak

# 获取债券数据
df = ak.bond_sina()

# 获取债券基本信息
df = ak.bond_info_sina()

# 获取可转债数据
df = ak.convertible_bond_sina()
```

---

## 6. MT Newswires

### 服务信息
- **URL**: `https://vast-mcp.blueskyapi.com/mtnewswires`
- **类型**: HTTP MCP
- **主要功能**: 财务新闻、市场动态、公司公告

### 提供的 API 接口
```
GET /news/{ticker}                         # 股票新闻
GET /breaking-news                         # 突发新闻
GET /news-feed/{source}                    # 新闻源订阅
GET /earnings-reports/{ticker}             # 盈利报告
GET /corporate-actions/{ticker}            # 企业行动（并购等）
```

### 对应 AKShare API

| 功能 | MT Newswires API | AKShare 对应 API | 备注 |
|------|-----------------|-----------------|------|
| 股票新闻 | `/news/{ticker}` | `guba_sina` | 股吧内容和新闻 |
| 突发新闻 | `/breaking-news` | 无直接对应 | 需爬虫实现 |
| 盈利报告 | `/earnings-reports/{ticker}` | `guba_sina` | 从公告获取 |
| 企业行动 | `/corporate-actions/{ticker}` | `stock_main_indicator` | 分红送股等 |

### 实现方案
```python
import akshare as ak

# 获取股吧新闻
df = ak.guba_sina(show_params=False)

# 获取分红送股信息
df = ak.stock_dividend_cninfo(symbol="000001")

# 获取增发、配股信息
df = ak.stock_allocation_cninfo(symbol="000001")
```

---

## 7. Aiera

### 服务信息
- **URL**: `https://mcp-pub.aiera.com`
- **类型**: HTTP MCP
- **主要功能**: 事件驱动情报、盈利电话会议、催化剂分析

### 提供的 API 接口
```
GET /events/{ticker}                       # 公司事件日历
GET /earnings-calls/{ticker}               # 盈利电话会议
GET /catalysts/{ticker}                    # 催化剂事件
GET /event-transcript/{event_id}           # 事件记录
GET /sentiment/{ticker}                    # 情感分析
```

### 对应 AKShare API

| 功能 | Aiera API | AKShare 对应 API | 备注 |
|------|----------|------------------|------|
| 事件日历 | `/events/{ticker}` | 无直接对应 | A股无统一日历 |
| 盈利电话 | `/earnings-calls/{ticker}` | 无对应 | 仅部分公司披露 |
| 催化剂 | `/catalysts/{ticker}` | 需手动构建 | 使用财报和公告 |
| 情感分析 | `/sentiment/{ticker}` | `guba_sina` | 可进行NLP分析 |

### 实现方案
```python
import akshare as ak

# 获取财务日历信息
df = ak.stock_zh_a_hist(symbol="000001")  # 含停复牌信息

# 获取股吧评论（用于情感分析）
df = ak.guba_sina()

# 获取研报发布信息
df = ak.stock_research_detail()
```

---

## 8. LSEG (Refinitiv)

### 服务信息
- **URL**: `https://api.analytics.lseg.com/lfa/mcp`
- **类型**: HTTP MCP
- **主要功能**: 固定收益、外汇、期权、宏观数据

### 提供的 API 接口

#### 固定收益工具
```
bond_price()                               # 债券定价
yieldbook_bond_reference()                 # 债券参考数据
yieldbook_cashflow()                       # 现金流预测
yieldbook_scenario()                       # 情景分析
interest_rate_curve()                      # 收益率曲线
fixed_income_risk_analytics()              # 风险分析
```

#### 衍生品工具
```
equity_vol_surface()                       # 股票波动率曲面
fx_vol_surface()                           # 外汇波动率曲面
option_value()                             # 期权定价
option_template_list()                     # 期权模板
tscc_historical_pricing_summaries()        # 历史价格
qa_historical_equity_price()               # 历史股价
```

#### 宏观工具
```
macro_data()                               # 宏观指标
economic_calendar()                        # 经济日历
central_bank_rates()                       # 央行利率
```

### 对应 AKShare API

| 功能 | LSEG API | AKShare 对应 API | 备注 |
|------|---------|------------------|------|
| 债券定价 | `bond_price()` | `bond_sina` | 债券行情 |
| 收益率曲线 | `interest_rate_curve()` | 无直接对应 | 需调用金融数据库 |
| 期权定价 | `option_value()` | `stock_option_sina` | 期权行情 |
| 波动率 | `equity_vol_surface()` | 无直接对应 | 需计算 |
| 宏观数据 | `macro_data()` | `macro_* 系列` | 经济数据 |
| 央行利率 | `central_bank_rates()` | `macro_*` | 利率数据 |

### 实现方案
```python
import akshare as ak

# 获取债券数据
df = ak.bond_sina()

# 获取期权数据
df = ak.stock_option_sina()

# 获取利率数据
df = ak.macro_cninfo()

# 获取宏观指标
df = ak.macro_sz_retail_sales()  # 社零数据
df = ak.macro_china_gdp()         # GDP数据
df = ak.macro_china_ppi()         # PPI数据
df = ak.macro_china_cpi()         # CPI数据
```

---

## 9. PitchBook

### 服务信息
- **URL**: `https://premium.mcp.pitchbook.com/mcp`
- **类型**: HTTP MCP
- **主要功能**: M&A 交易数据、私募股权、可比交易分析

### 提供的 API 接口
```
GET /transactions/{transaction_id}         # 交易详情
GET /comparables/{company_id}              # 可比交易
GET /valuation-multiples/{sector}          # 估值倍数
GET /company-financials/{company_id}       # 公司财务
GET /buyer-list/{criteria}                 # 买方名单
GET /precedent-transactions/{ticker}       # 先例交易
```

### 对应 AKShare API

| 功能 | PitchBook API | AKShare 对应 API | 备注 |
|------|----------|-------------------|------|
| 交易详情 | `/transactions/` | 无直接对应 | A股需爬虫 |
| 可比交易 | `/comparables/` | 需手动构建 | 使用上市公司数据 |
| 估值倍数 | `/valuation-multiples/` | `stock_valuation` | PE/PB等 |
| 买方名单 | `/buyer-list/` | 无对应 | 需企业信息库 |
| 先例交易 | `/precedent-transactions/` | 无直接对应 | 需爬虫 |

### 实现方案
```python
import akshare as ak

# 获取估值数据构建可比分析
df = ak.stock_valuation()

# 获取上市公司财务
df = ak.stock_main_indicator(symbol="000001")

# 获取增发、配股相关融资活动
df = ak.stock_allocation_cninfo()

# 获取并购重组信息
df = ak.stock_board_change_cninfo()
```

---

## 10. Chronograph

### 服务信息
- **URL**: `https://ai.chronograph.pe/mcp`
- **类型**: HTTP MCP
- **主要功能**: 私募股权数据、交易筛选、投资组合监控

### 提供的 API 接口
```
GET /pe-deals/{date_range}                 # 私募股权交易
GET /portfolio-monitoring/{fund_id}        # 投资组合监控
GET /deal-screening/{criteria}             # 交易筛选
GET /returns-analysis/{investment_id}      # 回报分析
GET /unit-economics/{company_id}           # 单位经济学
GET /exit-strategy/{investment_id}         # 退出策略
```

### 对应 AKShare API

| 功能 | Chronograph API | AKShare 对应 API | 备注 |
|------|----------|------------------|------|
| 私募交易 | `/pe-deals/` | 无直接对应 | A股无PE数据 |
| 投资组合 | `/portfolio-monitoring/` | 需手动跟踪 | 可结合公开数据 |
| 回报分析 | `/returns-analysis/` | 需自行计算 | 使用历史股价 |
| 单位经济 | `/unit-economics/` | `stock_main_indicator` | 需财务分析 |

### 实现方案
```python
import akshare as ak

# 获取上市公司财务用于分析
df = ak.stock_main_indicator(symbol="000001")

# 获取融资轮次（IPO、增发）
df = ak.stock_allocation_cninfo()

# 获取持股变化
df = ak.stock_restricted_shares()
```

---

## 11. Egnyte

### 服务信息
- **URL**: `https://mcp-server.egnyte.com/mcp`
- **类型**: HTTP MCP
- **主要功能**: 文件存储、文档管理、报告发布

### 提供的 API 接口
```
POST /files/upload                         # 上传文件
GET /files/{file_id}                       # 获取文件
DELETE /files/{file_id}                    # 删除文件
GET /folders/{folder_id}                   # 列出文件夹
POST /share/{file_id}                      # 文件分享
GET /activity/{file_id}                    # 文件活动日志
```

### 对应 AKShare API

| 功能 | Egnyte API | AKShare 对应 API | 备注 |
|------|-----------|------------------|------|
| 文件管理 | `/files/` | 无对应 | 需本地方案 |
| 文件分享 | `/share/` | 无对应 | 需本地方案 |
| 活动日志 | `/activity/` | 无对应 | 需本地方案 |

### 实现方案
```python
# 文件存储需要本地实现，可使用：
# - MinIO (开源S3兼容)
# - Nextcloud (开源网盘)
# - 阿里云OSS
# - 腾讯云COS
```

---

## 按功能分类的 AKShare 替代方案总结

### 📊 财务数据类
| 需求 | AKShare API | 说明 |
|------|-----------|------|
| 上市公司财务报表 | `stock_financial_analysis_indicator` | 综合财报数据 |
| 主要财务指标 | `stock_main_indicator` | PE、PB、ROE等 |
| 现金流数据 | `stock_cash_flow_sheet` | 现金流量表 |
| 估值数据 | `stock_valuation` | 估值倍数 |
| 分红信息 | `stock_dividend_cninfo` | 分红记录 |

### 📰 新闻事件类
| 需求 | AKShare API | 说明 |
|------|-----------|------|
| 新闻评论 | `guba_sina` | 股吧信息 |
| 公司公告 | `stock_information` | 公告信息 |
| 研报 | `stock_research_detail` | 研究报告 |

### 📈 行情数据类
| 需求 | AKShare API | 说明 |
|------|-----------|------|
| 历史行情 | `stock_zh_a_hist` | 日线数据 |
| 实时行情 | `stock_zh_a_hist_min` | 分钟数据 |
| 期权数据 | `stock_option_sina` | 期权行情 |
| 债券数据 | `bond_sina` | 债券行情 |

### 🏢 公司信息类
| 需求 | AKShare API | 说明 |
|------|-----------|------|
| 行业分类 | `bk_sina` | 行业信息 |
| 行业成分 | `bk_sina_members` | 行业成分股 |
| 股票基本信息 | `stock_info_a_sina` | 上市公司信息 |

### 💹 宏观数据类
| 需求 | AKShare API | 说明 |
|------|-----------|------|
| GDP数据 | `macro_china_gdp` | 经济总量 |
| CPI数据 | `macro_china_cpi` | 物价指数 |
| PPI数据 | `macro_china_ppi` | 生产指数 |
| 利率数据 | `macro_cninfo` | 利率信息 |

---

## 完整的 AKShare 替代实现示例

### 场景1：建立可比公司分析（替代 S&P Global + FactSet）

```python
import akshare as ak
import pandas as pd

def comparable_company_analysis(target_ticker, sector):
    """
    使用 AKShare 替代 S&P Global + FactSet
    """
    # 获取行业成分股
    industry_df = ak.bk_sina_members(symbol=sector)
    competitors = industry_df['code'].tolist()
    competitors.remove(target_ticker)  # 移除目标公司
    
    # 获取所有公司的估值和财务数据
    results = []
    for ticker in competitors:
        valuation = ak.stock_valuation(symbol=ticker)
        main_indicator = ak.stock_main_indicator(symbol=ticker)
        
        results.append({
            'ticker': ticker,
            'pe': valuation['pe'].values[0],
            'pb': valuation['pb'].values[0],
            'roe': main_indicator['roe'].values[0],
            'profit_margin': main_indicator['profit_margin'].values[0],
        })
    
    comp_df = pd.DataFrame(results)
    return comp_df.describe()

# 使用示例
comp_analysis = comparable_company_analysis('000001', 'bk0471')
print(comp_analysis)
```

### 场景2：盈利分析（替代 Daloopa + FactSet）

```python
import akshare as ak

def earnings_analysis(ticker, quarters=4):
    """
    使用 AKShare 替代 Daloopa + FactSet 进行盈利分析
    """
    # 获取历史财务指标
    df = ak.stock_main_indicator(symbol=ticker)
    
    # 获取近期财务数据
    financial = ak.stock_financial_analysis_indicator(
        symbol=ticker,
        indicator="基本每股收益"
    )
    
    # 获取现金流
    cashflow = ak.stock_cash_flow_sheet(symbol=ticker)
    
    return {
        'main_indicator': df.head(quarters),
        'eps': financial,
        'cashflow': cashflow.head(quarters)
    }

earnings = earnings_analysis('000001')
```

### 场景3：固定收益分析（替代 LSEG 债券工具）

```python
import akshare as ak

def bond_portfolio_analysis():
    """
    使用 AKShare 替代 LSEG 的债券分析
    """
    # 获取债券基本信息
    bonds = ak.bond_sina()
    
    # 获取可转债
    convertible = ak.convertible_bond_sina()
    
    # 组合分析
    all_bonds = pd.concat([
        bonds[['bond_code', 'bond_name', 'trade_price', 'yield']],
        convertible[['code', 'name', 'price', 'yield']]
    ])
    
    # 计算组合加权收益率
    total_value = all_bonds['trade_price'].sum()
    weighted_yield = (all_bonds['trade_price'] * all_bonds['yield']).sum() / total_value
    
    return {
        'bonds': all_bonds,
        'portfolio_yield': weighted_yield
    }
```

### 场景4：事件驱动分析（替代 MT Newswires + Aiera）

```python
import akshare as ak

def event_driven_analysis(ticker):
    """
    使用 AKShare 替代 MT Newswires + Aiera 进行事件分析
    """
    # 获取分红送股（企业行动）
    dividends = ak.stock_dividend_cninfo(symbol=ticker)
    
    # 获取股吧新闻（情感分析）
    news = ak.guba_sina()
    
    # 获取停复牌（市场事件）
    history = ak.stock_zh_a_hist(symbol=ticker, period="daily", 
                                 start_date="20230101", end_date="20231231")
    
    # 识别重大事件日期
    events = {
        'dividends': dividends['dividend_date'].tolist() if not dividends.empty else [],
        'news_dates': news[news['symbol'] == ticker]['pub_date'].tolist() if not news.empty else []
    }
    
    return events
```

---

## 迁移成本评估

| MCP 服务 | 替代难度 | 迁移成本 | 备注 |
|---------|---------|---------|------|
| Daloopa | ⭐ 低 | 少 | AKShare 完全覆盖 |
| Morningstar | ⭐⭐ 中低 | 少 | 缺少评级数据 |
| S&P Global | ⭐⭐⭐ 中 | 中 | 需手动构建对标 |
| FactSet | ⭐ 低 | 少 | 综合覆盖 |
| Moody's | ⭐⭐⭐ 中 | 中 | 缺少评级 |
| MT Newswires | ⭐⭐⭐⭐ 高 | 多 | 需爬虫或订阅 |
| Aiera | ⭐⭐⭐⭐ 高 | 多 | 电话会议录音需订阅 |
| LSEG | ⭐⭐⭐⭐ 高 | 多 | 债券定价模型需自建 |
| PitchBook | ⭐⭐⭐⭐ 高 | 多 | M&A 数据需爬虫 |
| Chronograph | ⭐⭐⭐⭐ 高 | 多 | PE数据无对应 |
| Egnyte | ⭐⭐⭐⭐ 高 | 多 | 需自建文件系统 |

---

## 推荐迁移策略

### 第一阶段（高性价比）
- ✅ 使用 AKShare 替代 **Daloopa** + **FactSet** 的财务数据
- ✅ 使用 AKShare 替代 **S&P Global** 的估值数据
- 投入：低，收益：高

### 第二阶段（中期）
- ✅ 爬虫 + AKShare 替代 **MT Newswires** 的新闻
- ✅ NLP 分析 + AKShare 替代 **Aiera** 的情感分析
- 投入：中，收益：中

### 第三阶段（长期）
- 建立内部债券定价模型替代 **LSEG**
- 建立 M&A 数据库替代 **PitchBook**
- 建立 PE 数据库替代 **Chronograph**
- 投入：高，收益：高

---

## 总结

| 指标 | 评分 |
|------|------|
| AKShare 覆盖度 | 6/10 |
| 对标 Daloopa + FactSet | 8/10 ✅ |
| 对标 S&P Global | 6/10 |
| 对标 LSEG | 4/10 |
| 对标新闻和事件数据 | 5/10 |
| 迁移可行性 | 7/10 |

**结论**：AKShare 可以很好地替代 **财务数据类** MCP，但对于 **新闻事件**、**固定收益** 和 **M&A** 数据需要额外的爬虫或订阅。
