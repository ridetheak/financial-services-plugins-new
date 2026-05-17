# OpenBB Integration Implementation Guide

## Quick Start

### 1. Get API Key (5 minutes)
```bash
# Visit https://www.openbb.io/
# Sign up for free tier account
# Generate API key from settings

export OPENBB_API_KEY="your-api-key-here"
```

### 2. Install SDK (2 minutes)
```bash
pip install openbb requests
```

### 3. Verify Access (1 minute)
```bash
python3 tools/test_openbb_access.py
```

---

## Architecture: MCP Server Integration

### Current Architecture
```
Plugin (e.g., financial-analysis)
    ↓
.mcp.json (MCP configuration)
    ↓
External MCP Servers (Daloopa, Morningstar, FactSet, etc.)
    ↓
Claude Agent
```

### With OpenBB
```
Plugin (e.g., financial-analysis)
    ↓
.mcp.json (includes OpenBB)
    ↓
OpenBB Cloud API + Other MCP Servers
    ↓
Claude Agent
```

---

## Implementation Steps

### Step 1: Add OpenBB MCP Configuration

**File**: `financial-analysis/.mcp.json`

```json
{
  "mcpServers": {
    "openbb": {
      "type": "http",
      "url": "https://api.openbb.dev/v1"
    },
    "daloopa": {
      "type": "http",
      "url": "https://mcp.daloopa.com/server/mcp"
    },
    ...existing servers...
  }
}
```

**Environment Setup**:
```json
{
  "env": {
    "OPENBB_API_KEY": "${OPENBB_API_KEY}"
  }
}
```

### Step 2: Create Utility Module

**File**: `tools/openbb_utils.py`

```python
"""
OpenBB data retrieval utilities for financial services plugins.
"""

import os
from typing import Optional, Dict, Any, List
from datetime import datetime, timedelta

class OpenBBClient:
    """Wrapper for OpenBB API access."""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("OPENBB_API_KEY")
        self.base_url = "https://api.openbb.dev/v1"
        
        if not self.api_key:
            raise ValueError("OPENBB_API_KEY not set")
    
    def get_stock_fundamentals(self, symbol: str) -> Dict[str, Any]:
        """Get company fundamentals (income statement, balance sheet, etc.)."""
        # Implementation will depend on OpenBB API structure
        pass
    
    def get_financial_statements(
        self, 
        symbol: str, 
        period: str = "annual",
        limit: int = 10
    ) -> Dict[str, Any]:
        """Get historical financial statements."""
        pass
    
    def get_equity_valuations(self, symbol: str) -> Dict[str, Any]:
        """Get company valuation metrics."""
        pass
    
    def get_economic_data(
        self,
        indicator: str,
        start_date: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Get economic indicators (GDP, inflation, unemployment, etc.)."""
        pass
    
    def get_comparable_companies(
        self,
        symbol: str,
        sector: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Get peer/comparable companies."""
        pass
```

### Step 3: Add Skills to Plugins

#### Example: Investment Banking Plugin

**File**: `investment-banking/skills/market-data/SKILL.md`

```markdown
# Market Data Retrieval

Uses OpenBB to fetch real-time and historical market data.

## Capabilities

- Company fundamentals (P&L, balance sheet, cash flow)
- Valuation multiples (P/E, EV/EBITDA, etc.)
- Peer/competitor analysis
- Economic data for context

## Example Usage

\`\`\`
Get Apple's latest financial metrics:
/openbb:fundamentals AAPL

Get comparative valuation vs peers:
/openbb:comps AAPL

Get industry economic indicators:
/openbb:economy technology
\`\`\`
```

#### Example: Financial Analysis Plugin

**File**: `financial-analysis/skills/valuation-data/SKILL.md`

```markdown
# Valuation Reference Data

Provides comparable company data and historical valuations from OpenBB.

## Capabilities

- Historical P/E, EV/EBITDA ratios
- Peer group selection and metrics
- Industry average valuation
- Margin and growth historical data

## Use in DCF Models

\`\`\`python
# In DCF analysis
comps_data = openbb.get_comparable_companies("TARGET")
terminal_multiple = comps_data["avg_ev_ebitda"]
```

---

## Configuration Examples

### Setup for Development

**File**: `.claude/OPENBB.local.md` (user-specific, gitignored)

```markdown
# OpenBB Configuration

## API Key
Set in your environment:
\`\`\`bash
export OPENBB_API_KEY="your-key-here"
\`\`\`

## Data Refresh Strategy
- Cache fundamentals for 1 day
- Cache quotes for 15 minutes
- Cache economic data for 1 month

## Rate Limiting
Free tier: ~100 requests/day
```

### Plugin-Specific Settings

**File**: `financial-analysis/.claude/OPENBB.md`

```markdown
# OpenBB Configuration for Financial Analysis

## Default Data Sources
1. OpenBB (primary, for fundamentals)
2. FactSet (secondary, for advanced metrics)
3. Morningstar (tertiary, for analyst data)

## Field Mappings
- Revenue → openbb.revenue
- EBITDA → openbb.operating_income + depreciation
- Free Cash Flow → openbb.cash_from_operations - capex
```

---

## API Endpoint Reference

### Stock Fundamentals
```
GET /equity/fundamental/income    # Income statement
GET /equity/fundamental/balance   # Balance sheet
GET /equity/fundamental/cash      # Cash flow statement
GET /equity/fundamental/ratios    # Key ratios
```

### Market Data
```
GET /equity/price/quote           # Current price
GET /equity/price/historical      # Historical prices
GET /equity/price/ohlcv           # OHLCV data
```

### Comparable Companies
```
GET /equity/search/compare        # Find comparables
GET /equity/profile/metrics       # Company metrics
```

### Economic Data
```
GET /economy/macro                # Macro indicators
GET /economy/gdp                  # GDP data
GET /economy/unemployment         # Employment data
```

---

## Error Handling

### Common Issues

**Issue 1: Invalid API Key**
```
Error: HTTP 401 Unauthorized
Solution: Check OPENBB_API_KEY environment variable
         Verify key hasn't expired
         Regenerate key in OpenBB dashboard
```

**Issue 2: Rate Limit Exceeded**
```
Error: HTTP 429 Too Many Requests
Solution: Implement caching for frequently accessed data
         Consider upgrading to paid tier
         Space out requests (batch retrieval)
```

**Issue 3: Data Not Available**
```
Error: HTTP 404 Not Found or empty response
Solution: Verify ticker symbol exists
         Check data availability date range
         Use fallback data source (FactSet, Morningstar)
```

### Caching Strategy

```python
from functools import lru_cache
from datetime import datetime, timedelta

cache_timestamps = {}
CACHE_DURATION = {
    "fundamentals": timedelta(days=1),
    "quotes": timedelta(minutes=15),
    "economic": timedelta(days=30),
}

def get_cached_data(key: str, fetch_func, *args):
    """Get data from cache or fetch new."""
    if key in cache and datetime.now() - cache_timestamps[key] < CACHE_DURATION.get(key, timedelta(hours=1)):
        return cache[key]
    
    data = fetch_func(*args)
    cache[key] = data
    cache_timestamps[key] = datetime.now()
    return data
```

---

## Testing

### Unit Tests

```python
import pytest
from tools.openbb_utils import OpenBBClient

@pytest.fixture
def openbb_client():
    return OpenBBClient()

def test_get_fundamentals(openbb_client):
    data = openbb_client.get_stock_fundamentals("AAPL")
    assert "revenue" in data
    assert "net_income" in data

def test_get_comparables(openbb_client):
    comps = openbb_client.get_comparable_companies("MSFT")
    assert len(comps) > 0
    assert "ticker" in comps[0]
```

### Integration Tests

```python
def test_end_to_end_valuation_analysis():
    """Test full valuation workflow using OpenBB data."""
    # Setup
    client = OpenBBClient()
    symbol = "AAPL"
    
    # Get fundamentals
    fundamentals = client.get_stock_fundamentals(symbol)
    assert fundamentals is not None
    
    # Get comparables
    comps = client.get_comparable_companies(symbol)
    assert len(comps) > 0
    
    # Verify data consistency
    assert fundamentals["ttm_pe"] > 0
    assert fundamentals["revenue"] > 0
```

---

## Monitoring & Observability

### Logging

```python
import logging

logger = logging.getLogger("openbb")
logger.setLevel(logging.INFO)

# Log API calls
logger.info(f"Fetching fundamentals for {symbol}")
logger.debug(f"API Response: {response.status_code}")

# Log rate limiting
logger.warning(f"Rate limit: {remaining_requests} requests remaining")
```

### Metrics to Track

- API response time
- Cache hit ratio
- Error rate by endpoint
- API quota usage
- Data freshness

---

## Production Rollout

### Phase 1: Internal Testing (Week 1-2)
- [ ] Install SDK in test environment
- [ ] Run comprehensive tests
- [ ] Validate data quality
- [ ] Set up monitoring

### Phase 2: Limited Rollout (Week 3-4)
- [ ] Deploy to development plugins (equity-research, financial-analysis)
- [ ] Gather feedback
- [ ] Monitor usage and costs

### Phase 3: Full Rollout (Week 5-6)
- [ ] Deploy to all plugins
- [ ] Update documentation
- [ ] Train plugin developers
- [ ] Monitor production usage

---

## Support & Resources

- **Documentation**: https://docs.openbb.dev/
- **API Reference**: https://docs.openbb.dev/api
- **Community**: https://openbb.io/community
- **Issues**: Report via OpenBB support portal
