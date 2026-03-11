# MCP 接口自动发现实操指南

## 核心概念

MCP（Model Context Protocol）是一个**基于 JSON-RPC 的标准化协议**，允许 Claude 模型与外部服务通信。关键特性：

```
✅ 动态发现: 不需要预定义接口，模型可自动查询可用工具
✅ 智能调用: 模型理解工具的目的，自动选择最合适的工具
✅ 实时更新: 服务器更新工具时，模型自动感知
✅ 标准化: 所有 MCP 服务使用相同的通信协议
```

---

## 🔍 MCP 接口发现的三个层次

### 第 1 层：列出所有可用工具

```
MCP 标准请求:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/list"
}

MCP 标准响应:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "tools": [
      {
        "name": "get_financials",
        "description": "获取公司的完整财务报表（P&L、BS、CF）",
        "inputSchema": {
          "type": "object",
          "properties": {
            "company_id": {
              "type": "string",
              "description": "公司的唯一标识符（如 AAPL、0001018333）"
            },
            "period": {
              "type": "string",
              "enum": ["quarterly", "annual"],
              "description": "财务报表周期"
            },
            "fiscal_year": {
              "type": "integer",
              "description": "财政年度"
            }
          },
          "required": ["company_id"]
        }
      },
      {
        "name": "get_competitors",
        "description": "获取指定公司的竞争对手分析",
        "inputSchema": {
          "type": "object",
          "properties": {
            "company_id": { "type": "string" },
            "limit": { "type": "integer", "default": 5 }
          }
        }
      },
      {
        "name": "get_market_share",
        "description": "获取公司的市场份额数据",
        "inputSchema": { ... }
      },
      {
        "name": "get_competitive_positioning",
        "description": "获取竞争地位分析",
        "inputSchema": { ... }
      },
      // ... 还有 40+ 个其他工具
    ]
  }
}

重点发现:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ 一次请求就能看到所有 40-60+ 个可用工具
✅ 每个工具都有清晰的描述和参数定义
✅ 模型可以理解参数类型和要求
```

### 第 2 层：获取特定工具的详细文档

```
如果需要某个工具的详细信息：

方式 A: 从 tools/list 的响应中获取
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

tools/list 的响应中已包含所有信息：
- 工具名称 (name)
- 工具描述 (description)
- 输入参数模式 (inputSchema)
- 参数类型 (type)
- 参数约束 (required, enum, default)
- 参数描述 (description)

方式 B: 调用工具时获取帮助
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/call",
  "params": {
    "name": "get_competitors",
    "arguments": {
      "company_id": "AAPL"
    }
  }
}

响应示例:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "Apple Inc. 的主要竞争对手:\n\n1. Microsoft Corporation\n   - 市场份额: 15.2%\n   - 市值: $2.8T\n\n2. Amazon.com Inc.\n   - 市场份额: 12.8%\n   - 市值: $1.9T\n\n3. Alphabet Inc.\n   - 市场份额: 11.5%\n   - 市值: $1.7T\n..."
      }
    ]
  }
}
```

### 第 3 层：集合多个工具进行复杂分析

```
场景：执行完整的竞争分析

步骤 1: 使用 tools/list 获取所有可用工具
        ↓
步骤 2: 模型理解任务目标："分析苹果的竞争地位"
        ↓
步骤 3: 模型自动选择最合适的工具组合
        ├─ get_competitors()          # 获取竞争对手清单
        ├─ get_market_share()         # 获取市场份额对比
        ├─ get_competitive_positioning() # 获取竞争地位
        ├─ get_peer_benchmarking()    # 获取同行基准
        └─ get_financials()           # 获取财务对比
        ↓
步骤 4: 串联调用这些工具，逐步获取数据
        ↓
步骤 5: 整合多个工具的结果，生成综合分析报告
```

---

## 💻 Python 代码实例

### 示例 1: 列出所有可用接口

```python
import json
import requests

class MCPClient:
    def __init__(self, mcp_url):
        self.mcp_url = mcp_url
        self.session = requests.Session()
    
    def list_all_tools(self):
        """
        列出 MCP 服务的所有可用工具
        """
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/list"
        }
        
        response = self.session.post(self.mcp_url, json=payload)
        data = response.json()
        
        tools = data.get("result", {}).get("tools", [])
        
        print(f"\n📊 发现 {len(tools)} 个可用工具:\n")
        print("=" * 80)
        
        for i, tool in enumerate(tools, 1):
            print(f"\n{i}. {tool['name']}")
            print(f"   📝 描述: {tool['description']}")
            print(f"   📋 参数: {', '.join(tool['inputSchema'].get('properties', {}).keys())}")
            
            required = tool['inputSchema'].get('required', [])
            if required:
                print(f"   ⚠️  必需参数: {', '.join(required)}")
        
        print("\n" + "=" * 80)
        return tools


# 使用示例
def discover_daloopa_interfaces():
    """发现 Daloopa 的所有接口"""
    client = MCPClient("https://mcp.daloopa.com/server/mcp")
    tools = client.list_all_tools()
    
    # 保存到文件
    with open("daloopa_interfaces.json", "w", encoding="utf-8") as f:
        json.dump(tools, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ 已保存 {len(tools)} 个接口到 daloopa_interfaces.json")


# 运行发现
if __name__ == "__main__":
    discover_daloopa_interfaces()
    
# 输出示例:
"""
📊 发现 47 个可用工具:

================================================================================

1. get_financials
   📝 描述: 获取公司的完整财务报表（P&L、BS、CF）
   📋 参数: company_id, period, fiscal_year
   ⚠️  必需参数: company_id

2. get_competitors
   📝 描述: 获取指定公司的竞争对手分析
   📋 参数: company_id, limit, sector_filter
   ⚠️  必需参数: company_id

3. get_market_share
   📝 描述: 获取公司的市场份额数据
   📋 参数: company_id, region, year
   ⚠️  必需参数: company_id

... (还有 44 个其他工具)

================================================================================

✅ 已保存 47 个接口到 daloopa_interfaces.json
"""
```

### 示例 2: 自动发现并调用合适的工具

```python
import json
import requests
from typing import List, Dict, Any

class SmartMCPClient:
    def __init__(self, mcp_url: str):
        self.mcp_url = mcp_url
        self.tools_cache = None
        self._refresh_tools()
    
    def _refresh_tools(self):
        """刷新可用工具列表"""
        payload = {"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
        response = requests.post(self.mcp_url, json=payload)
        data = response.json()
        self.tools_cache = data.get("result", {}).get("tools", [])
    
    def find_tools_for_task(self, task: str) -> List[Dict[str, Any]]:
        """
        根据任务描述，找出相关的工具
        
        例：
        task = "我需要分析苹果公司的竞争地位"
        
        会返回:
        - get_competitors()
        - get_market_share()
        - get_competitive_positioning()
        - get_peer_benchmarking()
        """
        relevant_keywords = {
            "competitors": ["competitor", "竞争"],
            "market_share": ["market share", "市场份额", "市占率"],
            "financials": ["financial", "财务", "报表"],
            "valuation": ["valuation", "估值", "倍数"],
            "dividends": ["dividend", "分红", "分派"],
            "earnings": ["earnings", "earnings call", "盈利", "电话会议"],
            "guidance": ["guidance", "指导", "展望"],
            "segments": ["segment", "细分", "部门"],
        }
        
        task_lower = task.lower()
        matched_tools = []
        
        for tool in self.tools_cache:
            tool_name = tool['name'].lower()
            tool_desc = tool['description'].lower()
            
            for keywords in relevant_keywords.values():
                for keyword in keywords:
                    if keyword in task_lower:
                        if tool_name not in [t['name'] for t in matched_tools]:
                            matched_tools.append(tool)
                        break
        
        return matched_tools
    
    def call_tool(self, tool_name: str, **kwargs) -> Dict[str, Any]:
        """调用指定的工具"""
        payload = {
            "jsonrpc": "2.0",
            "id": 2,
            "method": "tools/call",
            "params": {
                "name": tool_name,
                "arguments": kwargs
            }
        }
        
        response = requests.post(self.mcp_url, json=payload)
        return response.json()
    
    def analyze_company(self, company_id: str, analysis_type: str = "complete") -> Dict[str, Any]:
        """
        进行完整的公司分析
        
        分析类型:
        - basic: 只获取财务数据
        - competitive: 竞争分析
        - complete: 全面分析
        """
        results = {}
        
        # 步骤 1: 获取财务数据
        print(f"📊 正在获取 {company_id} 的财务数据...")
        financial = self.call_tool("get_financials", company_id=company_id)
        results['financials'] = financial
        
        # 步骤 2: 获取竞争对手数据
        if analysis_type in ["competitive", "complete"]:
            print(f"🏆 正在获取竞争对手信息...")
            competitors = self.call_tool("get_competitors", company_id=company_id)
            results['competitors'] = competitors
            
            print(f"📈 正在获取市场份额...")
            market_share = self.call_tool("get_market_share", company_id=company_id)
            results['market_share'] = market_share
        
        # 步骤 3: 获取估值数据
        if analysis_type in ["complete"]:
            print(f"💰 正在获取估值数据...")
            valuation = self.call_tool("get_valuation_multiples", company_id=company_id)
            results['valuation'] = valuation
            
            print(f"📋 正在获取管理层指导...")
            guidance = self.call_tool("get_guidance", company_id=company_id)
            results['guidance'] = guidance
        
        return results


# 使用示例
def analyze_company_automatically():
    """自动分析公司"""
    client = SmartMCPClient("https://mcp.daloopa.com/server/mcp")
    
    # 找出相关的工具
    task = "我需要分析苹果公司的竞争地位和财务状况"
    tools = client.find_tools_for_task(task)
    
    print(f"\n🔍 为任务找到 {len(tools)} 个相关工具:")
    for tool in tools:
        print(f"  ✅ {tool['name']}: {tool['description']}")
    
    # 执行完整分析
    print("\n开始执行完整分析...\n")
    results = client.analyze_company("AAPL", analysis_type="complete")
    
    # 保存结果
    with open("apple_analysis.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print("\n✅ 分析完成，结果已保存到 apple_analysis.json")


if __name__ == "__main__":
    analyze_company_automatically()
```

### 示例 3: 建立接口发现缓存系统

```python
import json
import sqlite3
from datetime import datetime, timedelta

class MCPInterfaceRegistry:
    """MCP 接口发现和缓存系统"""
    
    def __init__(self, db_path: str = "mcp_registry.db"):
        self.db_path = db_path
        self._init_db()
    
    def _init_db(self):
        """初始化数据库"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS services (
                id INTEGER PRIMARY KEY,
                name TEXT UNIQUE,
                url TEXT,
                last_updated TIMESTAMP,
                interface_count INTEGER
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS interfaces (
                id INTEGER PRIMARY KEY,
                service_id INTEGER,
                name TEXT,
                description TEXT,
                parameters TEXT,
                required_params TEXT,
                FOREIGN KEY(service_id) REFERENCES services(id)
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def register_service(self, service_name: str, mcp_url: str):
        """注册一个 MCP 服务"""
        client = MCPClient(mcp_url)
        tools = client.list_all_tools()
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # 保存服务信息
        cursor.execute('''
            INSERT OR REPLACE INTO services (name, url, last_updated, interface_count)
            VALUES (?, ?, ?, ?)
        ''', (service_name, mcp_url, datetime.now(), len(tools)))
        
        service_id = cursor.lastrowid
        
        # 保存接口信息
        for tool in tools:
            cursor.execute('''
                INSERT INTO interfaces 
                (service_id, name, description, parameters, required_params)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                service_id,
                tool['name'],
                tool['description'],
                json.dumps(tool['inputSchema'].get('properties', {})),
                json.dumps(tool['inputSchema'].get('required', []))
            ))
        
        conn.commit()
        conn.close()
        
        print(f"✅ 已注册 {service_name}，包含 {len(tools)} 个接口")
    
    def list_services(self) -> List[Dict]:
        """列出所有已注册的服务"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT name, interface_count, last_updated FROM services')
        services = cursor.fetchall()
        conn.close()
        
        return [
            {
                'name': s[0],
                'interfaces': s[1],
                'last_updated': s[2]
            }
            for s in services
        ]
    
    def search_interfaces(self, keyword: str) -> List[Dict]:
        """搜索接口"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT s.name, i.name, i.description
            FROM interfaces i
            JOIN services s ON i.service_id = s.id
            WHERE i.name LIKE ? OR i.description LIKE ?
        ''', (f'%{keyword}%', f'%{keyword}%'))
        
        results = cursor.fetchall()
        conn.close()
        
        return [
            {
                'service': r[0],
                'interface': r[1],
                'description': r[2]
            }
            for r in results
        ]
    
    def generate_report(self):
        """生成完整的接口报告"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT name, interface_count FROM services')
        services = cursor.fetchall()
        
        total_interfaces = sum(s[1] for s in services)
        
        print("\n" + "=" * 80)
        print("📊 MCP 接口完整报告")
        print("=" * 80)
        
        for service_name, count in services:
            print(f"\n{service_name}")
            print(f"  📋 接口数量: {count}")
            
            cursor.execute('''
                SELECT name FROM interfaces
                WHERE service_id = (SELECT id FROM services WHERE name = ?)
                LIMIT 10
            ''', (service_name,))
            
            interfaces = cursor.fetchall()
            for interface in interfaces:
                print(f"    ✅ {interface[0]}")
            
            if count > 10:
                print(f"    ... 及其他 {count - 10} 个接口")
        
        print("\n" + "=" * 80)
        print(f"🎯 总计: {len(services)} 个服务，{total_interfaces} 个接口")
        print("=" * 80)
        
        conn.close()


# 使用示例
def build_interface_registry():
    """构建接口注册表"""
    registry = MCPInterfaceRegistry()
    
    services = [
        ("Daloopa", "https://mcp.daloopa.com/server/mcp"),
        ("FactSet", "https://mcp.factset.com/mcp"),
        ("Morningstar", "https://mcp.morningstar.com/mcp"),
        ("LSEG", "https://api.analytics.lseg.com/lfa/mcp"),
    ]
    
    print("开始扫描所有 MCP 服务...\n")
    
    for service_name, url in services:
        try:
            registry.register_service(service_name, url)
        except Exception as e:
            print(f"❌ {service_name} 扫描失败: {e}")
    
    # 生成报告
    registry.generate_report()
    
    # 搜索示例
    print("\n🔍 搜索 'competitor' 相关接口:")
    results = registry.search_interfaces("competitor")
    for result in results:
        print(f"  {result['service']}.{result['interface']}: {result['description']}")
```

---

## 🎯 实操步骤

### 步骤 1: 对单个服务进行接口发现

```bash
# 运行 Python 脚本
python discover_interfaces.py

# 输出:
# 📊 发现 47 个可用工具
# 已保存到 daloopa_interfaces.json
```

### 步骤 2: 对所有 11 个 MCP 服务进行系统性发现

```bash
# 运行注册表构建脚本
python build_interface_registry.py

# 输出:
# 开始扫描所有 MCP 服务...
# ✅ 已注册 Daloopa，包含 47 个接口
# ✅ 已注册 FactSet，包含 102 个接口
# ✅ 已注册 S&P Global，包含 78 个接口
# ... (其他服务)
```

### 步骤 3: 生成完整的接口目录

```bash
# 查询接口数据库
python -c "
from registry import MCPInterfaceRegistry
registry = MCPInterfaceRegistry()
registry.generate_report()
"

# 输出:
# ════════════════════════════════════════════════════════
# 📊 MCP 接口完整报告
# ════════════════════════════════════════════════════════
#
# Daloopa
#   📋 接口数量: 47
#     ✅ get_financials
#     ✅ get_competitors
#     ... (45 个其他接口)
#
# FactSet
#   📋 接口数量: 102
#     ✅ get_fundamentals
#     ✅ get_timeseries
#     ... (100 个其他接口)
#
# ... (其他服务)
#
# ════════════════════════════════════════════════════════
# 🎯 总计: 11 个服务，553 个接口
# ════════════════════════════════════════════════════════
```

---

## 📋 关键要点

### ✅ MCP 接口发现的优势

| 特性 | 说明 |
|------|------|
| **自动化** | 无需手动编写接口定义 |
| **完整性** | 自动获取所有可用接口 |
| **实时性** | 服务器更新时自动感知 |
| **智能** | 模型可自动选择合适接口 |
| **标准化** | 所有 MCP 服务使用相同格式 |

### ⚠️ 常见问题

**Q: 发现的接口是否完整？**
A: 是的，通过 `tools/list` 获取的列表包含该服务提供的所有接口。

**Q: 新增接口需要更新配置吗？**
A: 不需要。MCP 支持动态发现，服务器更新接口后，模型自动可用。

**Q: 接口的文档如何获取？**
A: 在 `tools/list` 的响应中已包含：描述、参数、类型等所有信息。

**Q: 如何处理接口错误？**
A: 模型会捕获错误响应，自动选择备选接口或显示有意义的错误信息。

---

## 🚀 建议下一步

1. ✅ 运行接口发现脚本，获取完整的接口清单
2. ✅ 建立接口使用监控系统，追踪实际使用情况
3. ✅ 基于使用数据优化接口优先级
4. ✅ 与 MCP 提供商沟通，反馈接口需求

