# MCP Interface Auto-Discovery Practical Guide

## Core Concepts

MCP (Model Context Protocol) is a **standardized JSON-RPC-based protocol** that allows Claude models to communicate with external services. Key characteristics:

```
✅ Dynamic discovery: No need to pre-define interfaces; the model can query available tools automatically
✅ Intelligent invocation: The model understands the purpose of tools and selects the most appropriate one
✅ Real-time updates: When the server updates its tools, the model detects the change automatically
✅ Standardization: All MCP services use the same communication protocol
```

---

## Three Levels of MCP Interface Discovery

### Level 1: List All Available Tools

```
MCP standard request:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/list"
}

MCP standard response:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "tools": [
      {
        "name": "get_financials",
        "description": "Retrieve a company's complete financial statements (P&L, BS, CF)",
        "inputSchema": {
          "type": "object",
          "properties": {
            "company_id": {
              "type": "string",
              "description": "Unique identifier for the company (e.g. AAPL, 0001018333)"
            },
            "period": {
              "type": "string",
              "enum": ["quarterly", "annual"],
              "description": "Financial statement period"
            },
            "fiscal_year": {
              "type": "integer",
              "description": "Fiscal year"
            }
          },
          "required": ["company_id"]
        }
      },
      {
        "name": "get_competitors",
        "description": "Retrieve competitor analysis for a specified company",
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
        "description": "Retrieve market share data for a company",
        "inputSchema": { ... }
      },
      {
        "name": "get_competitive_positioning",
        "description": "Retrieve competitive positioning analysis",
        "inputSchema": { ... }
      },
      // ... 40+ additional tools
    ]
  }
}

Key finding:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ A single request reveals all 40-60+ available tools
✅ Each tool has a clear description and parameter definitions
✅ The model can understand parameter types and requirements
```

### Level 2: Retrieve Detailed Documentation for a Specific Tool

```
To get detailed information on a specific tool:

Method A: From the tools/list response
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

The tools/list response already contains all information:
- Tool name (name)
- Tool description (description)
- Input parameter schema (inputSchema)
- Parameter types (type)
- Parameter constraints (required, enum, default)
- Parameter descriptions (description)

Method B: Get help when calling the tool
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

Example response:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "Apple Inc. main competitors:\n\n1. Microsoft Corporation\n   - Market share: 15.2%\n   - Market cap: $2.8T\n\n2. Amazon.com Inc.\n   - Market share: 12.8%\n   - Market cap: $1.9T\n\n3. Alphabet Inc.\n   - Market share: 11.5%\n   - Market cap: $1.7T\n..."
      }
    ]
  }
}
```

### Level 3: Combining Multiple Tools for Complex Analysis

```
Scenario: Perform a full competitive analysis

Step 1: Use tools/list to get all available tools
        ↓
Step 2: Model understands the task goal: "Analyze Apple's competitive position"
        ↓
Step 3: Model automatically selects the best combination of tools
        ├─ get_competitors()              # Get list of competitors
        ├─ get_market_share()             # Get market share comparison
        ├─ get_competitive_positioning()  # Get competitive position
        ├─ get_peer_benchmarking()        # Get peer benchmarks
        └─ get_financials()               # Get financial comparison
        ↓
Step 4: Call these tools in sequence, retrieving data step by step
        ↓
Step 5: Combine results from multiple tools into a comprehensive analysis report
```

---

## Python Code Examples

### Example 1: List All Available Interfaces

```python
import json
import requests

class MCPClient:
    def __init__(self, mcp_url):
        self.mcp_url = mcp_url
        self.session = requests.Session()
    
    def list_all_tools(self):
        """
        List all available tools from the MCP service
        """
        payload = {
            "jsonrpc": "2.0",
            "id": 1,
            "method": "tools/list"
        }
        
        response = self.session.post(self.mcp_url, json=payload)
        data = response.json()
        
        tools = data.get("result", {}).get("tools", [])
        
        print(f"\nDiscovered {len(tools)} available tools:\n")
        print("=" * 80)
        
        for i, tool in enumerate(tools, 1):
            print(f"\n{i}. {tool['name']}")
            print(f"   Description: {tool['description']}")
            print(f"   Parameters: {', '.join(tool['inputSchema'].get('properties', {}).keys())}")
            
            required = tool['inputSchema'].get('required', [])
            if required:
                print(f"   Required parameters: {', '.join(required)}")
        
        print("\n" + "=" * 80)
        return tools


# Usage example
def discover_daloopa_interfaces():
    """Discover all Daloopa interfaces"""
    client = MCPClient("https://mcp.daloopa.com/server/mcp")
    tools = client.list_all_tools()
    
    # Save to file
    with open("daloopa_interfaces.json", "w", encoding="utf-8") as f:
        json.dump(tools, f, indent=2, ensure_ascii=False)
    
    print(f"\nSaved {len(tools)} interfaces to daloopa_interfaces.json")


# Run discovery
if __name__ == "__main__":
    discover_daloopa_interfaces()
    
# Sample output:
"""
Discovered 47 available tools:

================================================================================

1. get_financials
   Description: Retrieve a company's complete financial statements (P&L, BS, CF)
   Parameters: company_id, period, fiscal_year
   Required parameters: company_id

2. get_competitors
   Description: Retrieve competitor analysis for a specified company
   Parameters: company_id, limit, sector_filter
   Required parameters: company_id

3. get_market_share
   Description: Retrieve market share data for a company
   Parameters: company_id, region, year
   Required parameters: company_id

... (44 additional tools)

================================================================================

Saved 47 interfaces to daloopa_interfaces.json
"""
```

### Example 2: Auto-Discover and Call the Right Tool

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
        """Refresh the list of available tools"""
        payload = {"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
        response = requests.post(self.mcp_url, json=payload)
        data = response.json()
        self.tools_cache = data.get("result", {}).get("tools", [])
    
    def find_tools_for_task(self, task: str) -> List[Dict[str, Any]]:
        """
        Find relevant tools based on a task description.
        
        Example:
        task = "I need to analyze Apple's competitive position"
        
        Returns:
        - get_competitors()
        - get_market_share()
        - get_competitive_positioning()
        - get_peer_benchmarking()
        """
        relevant_keywords = {
            "competitors": ["competitor", "competition"],
            "market_share": ["market share", "market position"],
            "financials": ["financial", "statements"],
            "valuation": ["valuation", "multiples"],
            "dividends": ["dividend", "distribution"],
            "earnings": ["earnings", "earnings call"],
            "guidance": ["guidance", "outlook"],
            "segments": ["segment", "division"],
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
        """Call the specified tool"""
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
        Perform a full company analysis.
        
        Analysis types:
        - basic: financial data only
        - competitive: competitive analysis
        - complete: comprehensive analysis
        """
        results = {}
        
        # Step 1: Get financial data
        print(f"Retrieving financial data for {company_id}...")
        financial = self.call_tool("get_financials", company_id=company_id)
        results['financials'] = financial
        
        # Step 2: Get competitor data
        if analysis_type in ["competitive", "complete"]:
            print(f"Retrieving competitor information...")
            competitors = self.call_tool("get_competitors", company_id=company_id)
            results['competitors'] = competitors
            
            print(f"Retrieving market share...")
            market_share = self.call_tool("get_market_share", company_id=company_id)
            results['market_share'] = market_share
        
        # Step 3: Get valuation data
        if analysis_type in ["complete"]:
            print(f"Retrieving valuation data...")
            valuation = self.call_tool("get_valuation_multiples", company_id=company_id)
            results['valuation'] = valuation
            
            print(f"Retrieving management guidance...")
            guidance = self.call_tool("get_guidance", company_id=company_id)
            results['guidance'] = guidance
        
        return results


# Usage example
def analyze_company_automatically():
    """Analyze a company automatically"""
    client = SmartMCPClient("https://mcp.daloopa.com/server/mcp")
    
    # Find relevant tools
    task = "I need to analyze Apple's competitive position and financial condition"
    tools = client.find_tools_for_task(task)
    
    print(f"\nFound {len(tools)} relevant tools for the task:")
    for tool in tools:
        print(f"  ✅ {tool['name']}: {tool['description']}")
    
    # Run full analysis
    print("\nStarting full analysis...\n")
    results = client.analyze_company("AAPL", analysis_type="complete")
    
    # Save results
    with open("apple_analysis.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print("\nAnalysis complete. Results saved to apple_analysis.json")


if __name__ == "__main__":
    analyze_company_automatically()
```

### Example 3: Build an Interface Discovery Cache System

```python
import json
import sqlite3
from datetime import datetime, timedelta

class MCPInterfaceRegistry:
    """MCP interface discovery and caching system"""
    
    def __init__(self, db_path: str = "mcp_registry.db"):
        self.db_path = db_path
        self._init_db()
    
    def _init_db(self):
        """Initialize the database"""
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
        """Register an MCP service"""
        client = MCPClient(mcp_url)
        tools = client.list_all_tools()
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Save service information
        cursor.execute('''
            INSERT OR REPLACE INTO services (name, url, last_updated, interface_count)
            VALUES (?, ?, ?, ?)
        ''', (service_name, mcp_url, datetime.now(), len(tools)))
        
        service_id = cursor.lastrowid
        
        # Save interface information
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
        
        print(f"Registered {service_name} with {len(tools)} interfaces")
    
    def list_services(self) -> List[Dict]:
        """List all registered services"""
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
        """Search interfaces by keyword"""
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
        """Generate a complete interface report"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT name, interface_count FROM services')
        services = cursor.fetchall()
        
        total_interfaces = sum(s[1] for s in services)
        
        print("\n" + "=" * 80)
        print("MCP Interface Complete Report")
        print("=" * 80)
        
        for service_name, count in services:
            print(f"\n{service_name}")
            print(f"  Interface count: {count}")
            
            cursor.execute('''
                SELECT name FROM interfaces
                WHERE service_id = (SELECT id FROM services WHERE name = ?)
                LIMIT 10
            ''', (service_name,))
            
            interfaces = cursor.fetchall()
            for interface in interfaces:
                print(f"    ✅ {interface[0]}")
            
            if count > 10:
                print(f"    ... and {count - 10} more interfaces")
        
        print("\n" + "=" * 80)
        print(f"Total: {len(services)} services, {total_interfaces} interfaces")
        print("=" * 80)
        
        conn.close()


# Usage example
def build_interface_registry():
    """Build the interface registry"""
    registry = MCPInterfaceRegistry()
    
    services = [
        ("Daloopa", "https://mcp.daloopa.com/server/mcp"),
        ("FactSet", "https://mcp.factset.com/mcp"),
        ("Morningstar", "https://mcp.morningstar.com/mcp"),
        ("LSEG", "https://api.analytics.lseg.com/lfa/mcp"),
    ]
    
    print("Starting scan of all MCP services...\n")
    
    for service_name, url in services:
        try:
            registry.register_service(service_name, url)
        except Exception as e:
            print(f"Failed to scan {service_name}: {e}")
    
    # Generate report
    registry.generate_report()
    
    # Search example
    print("\nSearching for interfaces related to 'competitor':")
    results = registry.search_interfaces("competitor")
    for result in results:
        print(f"  {result['service']}.{result['interface']}: {result['description']}")
```

---

## Step-by-Step Walkthrough

### Step 1: Discover interfaces for a single service

```bash
# Run the Python script
python discover_interfaces.py

# Output:
# Discovered 47 available tools
# Saved to daloopa_interfaces.json
```

### Step 2: Systematically discover all 11 MCP services

```bash
# Run the registry build script
python build_interface_registry.py

# Output:
# Starting scan of all MCP services...
# Registered Daloopa with 47 interfaces
# Registered FactSet with 102 interfaces
# Registered S&P Global with 78 interfaces
# ... (other services)
```

### Step 3: Generate a complete interface catalog

```bash
# Query the interface database
python -c "
from registry import MCPInterfaceRegistry
registry = MCPInterfaceRegistry()
registry.generate_report()
"

# Output:
# ════════════════════════════════════════════════════════
# MCP Interface Complete Report
# ════════════════════════════════════════════════════════
#
# Daloopa
#   Interface count: 47
#     ✅ get_financials
#     ✅ get_competitors
#     ... (45 other interfaces)
#
# FactSet
#   Interface count: 102
#     ✅ get_fundamentals
#     ✅ get_timeseries
#     ... (100 other interfaces)
#
# ... (other services)
#
# ════════════════════════════════════════════════════════
# Total: 11 services, 553 interfaces
# ════════════════════════════════════════════════════════
```

---

## Key Takeaways

### Advantages of MCP Interface Discovery

| Feature | Description |
|------|------|
| **Automation** | No need to manually write interface definitions |
| **Completeness** | All available interfaces are retrieved automatically |
| **Real-time** | Detects server updates automatically |
| **Intelligence** | Model can automatically select the right interface |
| **Standardization** | All MCP services use the same format |

### Common Questions

**Q: Is the discovered interface list complete?**
A: Yes. The list returned by `tools/list` contains all interfaces provided by that service.

**Q: Does adding a new interface require updating configuration?**
A: No. MCP supports dynamic discovery; once the server adds an interface, the model can use it automatically.

**Q: Where can I find interface documentation?**
A: The `tools/list` response already includes everything: descriptions, parameters, types, and more.

**Q: How are interface errors handled?**
A: The model captures error responses and automatically selects a fallback interface, or surfaces a meaningful error message.

---

## Suggested Next Steps

1. ✅ Run the interface discovery script to obtain the complete interface list
2. ✅ Set up an interface usage monitoring system to track actual usage
3. ✅ Optimize interface priority based on usage data
4. ✅ Communicate with MCP providers to provide feedback on interface needs
