# MCP 服务分析

## 概述

此项目共使用 **11 个 MCP（Model Context Protocol）服务**，分布在不同的插件中。所有服务都是 HTTP 类型。

---

## MCP 服务完整列表

### 1. **Daloopa**
- **URL**: `https://mcp.daloopa.com/server/mcp`
- **类型**: HTTP
- **所在插件**: financial-analysis（核心插件）
- **功能**: 财务数据和市场数据聚合平台
- **用途**: 拉取公司财务数据、竞争对手分析、市场趋势

### 2. **Morningstar**
- **URL**: `https://mcp.morningstar.com/mcp`
- **类型**: HTTP
- **所在插件**: financial-analysis（核心插件）
- **功能**: 投资研究和基金数据平台
- **用途**: 基金分析、股票评级、性能基准

### 3. **S&P Global（Kensho）**
- **URL**: `https://kfinance.kensho.com/integrations/mcp`
- **类型**: HTTP
- **所在插件**: 
  - financial-analysis（核心插件）
  - partner-built/spglobal（S&P Global 专属插件）
- **功能**: 金融数据、行业分析、估值工具
- **用途**: 公司撕页、盈利预览、融资摘要

### 4. **FactSet**
- **URL**: `https://mcp.factset.com/mcp`
- **类型**: HTTP
- **所在插件**: financial-analysis（核心插件）
- **功能**: 综合财务数据和分析平台
- **用途**: 财务建模、估值、市场数据

### 5. **Moody's**
- **URL**: `https://api.moodys.com/genai-ready-data/m1/mcp`
- **类型**: HTTP
- **所在插件**: financial-analysis（核心插件）
- **功能**: 信用评级和风险分析
- **用途**: 信用质量评估、债券分析

### 6. **MT Newswires**
- **URL**: `https://vast-mcp.blueskyapi.com/mtnewswires`
- **类型**: HTTP
- **所在插件**: financial-analysis（核心插件）
- **功能**: 金融新闻和市场情报
- **用途**: 市场新闻、公司公告、经济新闻

### 7. **Aiera**
- **URL**: `https://mcp-pub.aiera.com`
- **类型**: HTTP
- **所在插件**: financial-analysis（核心插件）
- **功能**: 事件驱动的市场情报
- **用途**: 盈利电话会议、公司事件、市场洞察

### 8. **LSEG（伦敦交易所集团）**
- **URL**: `https://api.analytics.lseg.com/lfa/mcp`
- **类型**: HTTP
- **所在插件**: 
  - financial-analysis（核心插件）
  - partner-built/lseg（LSEG 专属插件）
- **功能**: 固定收益、外汇、期权、宏观数据
- **用途**: 债券定价、收益曲线分析、期权估值、宏观仪表板

### 9. **PitchBook**
- **URL**: `https://premium.mcp.pitchbook.com/mcp`
- **类型**: HTTP
- **所在插件**: financial-analysis（核心插件）
- **功能**: M&A 和私募股权数据
- **用途**: 交易追踪、可比交易分析、买方名单

### 10. **Chronograph**
- **URL**: `https://ai.chronograph.pe/mcp`
- **类型**: HTTP
- **所在插件**: financial-analysis（核心插件）
- **功能**: 私募股权和风险投资数据
- **用途**: 交易筛选、投资组合监控、回报分析

### 11. **Egnyte**
- **URL**: `https://mcp-server.egnyte.com/mcp`
- **类型**: HTTP
- **所在插件**: financial-analysis（核心插件）
- **功能**: 文件管理和文件共享
- **用途**: 文件存储、文档管理、报告发布

---

## 按插件分类的 MCP 服务分布

### Core Plugin: financial-analysis（核心插件）
包含所有 11 个 MCP 服务：
- ✅ Daloopa
- ✅ Morningstar
- ✅ S&P Global
- ✅ FactSet
- ✅ Moody's
- ✅ MT Newswires
- ✅ Aiera
- ✅ LSEG
- ✅ PitchBook
- ✅ Chronograph
- ✅ Egnyte

### Add-on Plugins（附加插件）

| 插件 | MCP 服务 |
|------|---------|
| **equity-research**（股票研究） | 无独立 MCP（继承 financial-analysis） |
| **investment-banking**（投资银行） | 无独立 MCP（继承 financial-analysis） |
| **private-equity**（私募股权） | 无独立 MCP（继承 financial-analysis） |
| **wealth-management**（财富管理） | 无独立 MCP（继承 financial-analysis） |

### Partner-Built Plugins（合作伙伴插件）

| 插件 | MCP 服务 | 说明 |
|------|---------|------|
| **partner-built/lseg** | LSEG | LSEG 数据专属集成 |
| **partner-built/spglobal** | S&P Global | S&P 数据专属集成 |

---

## MCP 服务按功能分类

### 📊 财务数据和建模
- **Daloopa** - 财务数据聚合
- **FactSet** - 综合财务数据
- **Morningstar** - 投资数据

### 🏢 公司和估值分析
- **S&P Global** - 行业分析、估值
- **Moody's** - 信用分析

### 📰 新闻和事件
- **MT Newswires** - 财务新闻
- **Aiera** - 盈利电话、市场事件

### 💼 M&A 和私募股权
- **PitchBook** - M&A 和私募股权交易
- **Chronograph** - 私募股权和风险投资

### 💹 固定收益和衍生品
- **LSEG** - 债券、外汇、期权、宏观

### 📁 文档管理
- **Egnyte** - 文件存储和管理

---

## 关键特点

### 集中化架构 🎯
- 所有 MCP 服务都在 **financial-analysis（核心插件）** 中声明
- 附加插件和合作伙伴插件**继承**核心插件的 MCP 服务
- 避免了重复配置和版本冲突

### 服务共享机制
```
financial-analysis（核心）
    ↓ 提供所有 MCP 服务
├── equity-research（股票研究）
├── investment-banking（投资银行）
├── private-equity（私募股权）
└── wealth-management（财富管理）

partner-built/lseg（LSEG 专属）
    ↓ 额外定制 LSEG 服务

partner-built/spglobal（S&P Global 专属）
    ↓ 额外定制 S&P Global 服务
```

### 认证和授权要求 🔐
根据 README.md：
> MCP 访问可能需要来自相应提供商的订阅或 API 密钥

需要配置的凭证：
- Daloopa API Key
- Morningstar API Key
- S&P Global/Kensho API Key
- FactSet API Key
- Moody's API Key
- MT Newswires API Key
- Aiera API Key
- LSEG API Key/OAuth
- PitchBook API Key
- Chronograph API Key
- Egnyte API Key

---

## 工作流中的 MCP 使用场景

### 研究到报告工作流
1. 使用 **Daloopa/FactSet** 拉取财务数据
2. 使用 **MT Newswires/Aiera** 获取新闻和事件
3. 使用 **S&P Global** 获取行业分析
4. 使用 **Moody's** 获取信用分析
5. 生成出版就绪的股票研究报告

### 可比公司分析（Comps）
1. 使用 **FactSet/Daloopa** 获取财务指标
2. 使用 **PitchBook** 获取交易倍数
3. 使用 **S&P Global** 获取行业基准

### M&A 工作流
1. 使用 **PitchBook** 识别买方列表
2. 使用 **FactSet/Daloopa** 获取目标财务数据
3. 使用 **Moody's** 评估信用风险

### 固定收益分析（LSEG 插件）
1. 使用 **LSEG** 进行债券定价
2. 分析收益曲线
3. 评估 FX 套息交易
4. 期权估值
5. 构建宏观仪表板

### 私募股权工作流
1. 使用 **Chronograph** 进行交易筛选
2. 使用 **FactSet** 进行单位经济分析
3. 使用 **PitchBook** 进行可比交易分析

---

## 架构优势

| 优势 | 说明 |
|------|------|
| **一次配置，多处使用** | 在 financial-analysis 中配置一次，所有插件都能使用 |
| **版本一致性** | 不会出现不同插件使用不同版本的问题 |
| **易于维护** | 更新或替换 MCP 只需修改一个地方 |
| **灵活扩展** | 合作伙伴可以添加专属的 MCP 服务 |
| **降低复杂性** | 附加插件可以专注于业务逻辑，而不是数据连接 |

---

## 自定义建议

为了针对特定公司定制这个架构，你可以：

1. **替换数据源**
   - 编辑 `financial-analysis/.mcp.json`
   - 指向你公司内部的数据 API
   - 保持接口相同

2. **添加内部工具**
   - 为内部财务系统添加 MCP 服务
   - 为内部文档管理系统添加 MCP 服务
   - 为内部交易平台添加 MCP 服务

3. **配置特定的服务**
   - 某些公司可能只需要特定的数据提供商
   - 可以选择性地启用/禁用 MCP 服务

---

## 总结

✅ **11 个 MCP 服务**
✅ **集中在 financial-analysis 核心插件**
✅ **跨越金融研究、M&A、私募股权、固定收益等多个领域**
✅ **支持从数据收集到报告生成的完整工作流**
✅ **易于定制和扩展**
