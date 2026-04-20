"""
Equity Price API Server
Exposes: GET /api/v1/equity/price/quote?symbol=<TICKER>
Runs on: https://127.0.0.1:6901

Live data providers (priority order, set via env var):
  POLYGON_API_KEY      -> polygon.io  (https://polygon.io/dashboard)
  FINNHUB_API_KEY      -> finnhub.io  (https://finnhub.io/register)
  ALPHA_VANTAGE_API_KEY-> alphavantage.co (https://www.alphavantage.co/support/#api-key)

Falls back to mock data when no key is configured.
"""

import math
import os
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

import requests
from fastapi import FastAPI, Query, HTTPException
import uvicorn

app = FastAPI(title="Equity Price API", version="1.0.0")

CERTS_DIR = Path(__file__).parent / "certs"
_HTTP = requests.Session()
_HTTP.headers.update({"User-Agent": "equity-price-api/1.0"})


# ---------------------------------------------------------------------------
# Live provider implementations
# ---------------------------------------------------------------------------

def _fetch_polygon(symbol: str) -> dict:
    key = os.environ["POLYGON_API_KEY"]
    url = f"https://api.polygon.io/v2/snapshot/locale/us/markets/stocks/tickers/{symbol.upper()}"
    r = _HTTP.get(url, params={"apiKey": key}, timeout=8)
    if r.status_code == 404:
        raise HTTPException(404, f"Symbol '{symbol}' not found")
    if r.status_code == 403:
        raise HTTPException(403, "Invalid Polygon API key")
    r.raise_for_status()
    snap = r.json().get("ticker", {})
    day = snap.get("day", {})
    prev = snap.get("prevDay", {})
    last_trade = snap.get("lastTrade", {})
    price = last_trade.get("p") or day.get("c")
    prev_close = prev.get("c")
    return {
        "symbol": symbol.upper(),
        "name": None,
        "exchange": snap.get("ticker", symbol.upper()),
        "instrument_type": "EQUITY",
        "currency": "USD",
        "price": price,
        "previous_close": prev_close,
        "change": round(price - prev_close, 4) if price and prev_close else None,
        "change_percent": round((price - prev_close) / prev_close * 100, 4) if price and prev_close else None,
        "day_high": day.get("h"),
        "day_low": day.get("l"),
        "volume": day.get("v"),
        "fifty_two_week_high": None,
        "fifty_two_week_low": None,
        "market_cap": None,
        "data_source": "polygon",
    }


def _fetch_finnhub(symbol: str) -> dict:
    key = os.environ["FINNHUB_API_KEY"]
    r = _HTTP.get(
        "https://finnhub.io/api/v1/quote",
        params={"symbol": symbol.upper(), "token": key},
        timeout=8,
    )
    r.raise_for_status()
    d = r.json()
    if d.get("c") == 0:
        raise HTTPException(404, f"Symbol '{symbol}' not found")
    price = d["c"]
    prev_close = d["pc"]
    # Fetch profile for name/exchange
    prof = _HTTP.get(
        "https://finnhub.io/api/v1/stock/profile2",
        params={"symbol": symbol.upper(), "token": key},
        timeout=8,
    ).json()
    return {
        "symbol": symbol.upper(),
        "name": prof.get("name"),
        "exchange": prof.get("exchange"),
        "instrument_type": "EQUITY",
        "currency": prof.get("currency", "USD"),
        "price": price,
        "previous_close": prev_close,
        "change": round(price - prev_close, 4),
        "change_percent": round(d.get("dp", 0), 4),
        "day_high": d.get("h"),
        "day_low": d.get("l"),
        "volume": None,
        "fifty_two_week_high": None,
        "fifty_two_week_low": None,
        "market_cap": prof.get("marketCapitalization"),
        "data_source": "finnhub",
    }


def _fetch_alpha_vantage(symbol: str) -> dict:
    key = os.environ["ALPHA_VANTAGE_API_KEY"]
    r = _HTTP.get(
        "https://www.alphavantage.co/query",
        params={"function": "GLOBAL_QUOTE", "symbol": symbol.upper(), "apikey": key},
        timeout=10,
    )
    r.raise_for_status()
    d = r.json()
    if "Note" in d:
        raise HTTPException(429, "Alpha Vantage rate limit reached")
    gq = d.get("Global Quote", {})
    if not gq or not gq.get("05. price"):
        raise HTTPException(404, f"Symbol '{symbol}' not found")
    price = float(gq["05. price"])
    prev_close = float(gq["08. previous close"])
    return {
        "symbol": symbol.upper(),
        "name": None,
        "exchange": None,
        "instrument_type": "EQUITY",
        "currency": "USD",
        "price": price,
        "previous_close": prev_close,
        "change": float(gq["09. change"]),
        "change_percent": float(gq["10. change percent"].rstrip("%")),
        "day_high": float(gq["03. high"]),
        "day_low": float(gq["04. low"]),
        "volume": int(gq["06. volume"]),
        "fifty_two_week_high": None,
        "fifty_two_week_low": None,
        "market_cap": None,
        "data_source": "alpha_vantage",
    }


def _fetch_yahoo(symbol: str) -> dict:
    """Yahoo Finance – no API key required; uses cookie + crumb auth."""
    sym = symbol.upper()

    # Step 1: get session cookie
    consent = _HTTP.get(
        "https://fc.yahoo.com/",
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"},
        timeout=8,
    )

    # Step 2: get crumb
    crumb_resp = _HTTP.get(
        "https://query2.finance.yahoo.com/v1/test/getcrumb",
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=8,
    )
    crumb = crumb_resp.text.strip()

    # Step 3: fetch quote
    r = _HTTP.get(
        f"https://query2.finance.yahoo.com/v8/finance/chart/{sym}",
        params={"interval": "1d", "range": "1d", "crumb": crumb},
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=8,
    )
    if r.status_code == 404:
        raise HTTPException(404, f"Symbol '{sym}' not found")
    r.raise_for_status()
    result = r.json().get("chart", {}).get("result")
    if not result:
        raise HTTPException(404, f"No data returned for '{sym}'")
    meta = result[0]["meta"]
    price = meta.get("regularMarketPrice")
    prev_close = meta.get("chartPreviousClose") or meta.get("previousClose")
    change = round(price - prev_close, 4) if price and prev_close else None
    change_pct = round(change / prev_close * 100, 4) if change and prev_close else None
    return {
        "symbol": sym,
        "name": None,
        "exchange": meta.get("exchangeName"),
        "instrument_type": meta.get("instrumentType", "EQUITY"),
        "currency": meta.get("currency", "USD"),
        "price": price,
        "previous_close": prev_close,
        "change": change,
        "change_percent": change_pct,
        "day_high": meta.get("regularMarketDayHigh"),
        "day_low": meta.get("regularMarketDayLow"),
        "volume": meta.get("regularMarketVolume"),
        "fifty_two_week_high": meta.get("fiftyTwoWeekHigh"),
        "fifty_two_week_low": meta.get("fiftyTwoWeekLow"),
        "market_cap": meta.get("marketCap"),
        "data_source": "yahoo_finance",
    }


# ---------------------------------------------------------------------------
# Mock fallback
# ---------------------------------------------------------------------------

_MOCK: dict[str, dict] = {
    "AAPL":  {"price": 213.55, "prev": 211.40, "hi": 214.90, "lo": 210.85, "w52h": 237.23, "w52l": 164.08, "vol": 58_432_100, "mc": 3_245_000_000_000, "exch": "NMS",  "name": "Apple Inc."},
    "MSFT":  {"price": 421.30, "prev": 418.75, "hi": 423.10, "lo": 417.20, "w52h": 468.35, "w52l": 344.79, "vol": 21_876_400, "mc": 3_130_000_000_000, "exch": "NMS",  "name": "Microsoft Corporation"},
    "GOOGL": {"price": 175.85, "prev": 174.10, "hi": 176.90, "lo": 173.65, "w52h": 207.05, "w52l": 140.53, "vol": 19_543_200, "mc": 2_190_000_000_000, "exch": "NMS",  "name": "Alphabet Inc."},
    "AMZN":  {"price": 205.40, "prev": 203.90, "hi": 206.75, "lo": 202.55, "w52h": 242.52, "w52l": 151.61, "vol": 35_218_900, "mc": 2_200_000_000_000, "exch": "NMS",  "name": "Amazon.com, Inc."},
    "NVDA":  {"price": 875.40, "prev": 861.25, "hi": 882.50, "lo": 858.10, "w52h": 974.00, "w52l": 462.41, "vol": 42_876_100, "mc": 2_155_000_000_000, "exch": "NMS",  "name": "NVIDIA Corporation"},
    "TSLA":  {"price": 248.50, "prev": 244.10, "hi": 251.30, "lo": 241.80, "w52h": 414.50, "w52l": 138.80, "vol": 98_432_700, "mc": 795_000_000_000,   "exch": "NMS",  "name": "Tesla, Inc."},
    "META":  {"price": 513.20, "prev": 508.75, "hi": 516.40, "lo": 506.30, "w52h": 638.40, "w52l": 414.50, "vol": 14_329_800, "mc": 1_305_000_000_000, "exch": "NMS",  "name": "Meta Platforms, Inc."},
    "JPM":   {"price": 234.85, "prev": 232.40, "hi": 236.10, "lo": 231.50, "w52h": 280.25, "w52l": 183.49, "vol": 10_218_300, "mc": 671_000_000_000,   "exch": "NYSE", "name": "JPMorgan Chase & Co."},
    "GS":    {"price": 512.30, "prev": 508.10, "hi": 515.20, "lo": 506.80, "w52h": 601.89, "w52l": 395.63, "vol": 3_218_700,  "mc": 168_000_000_000,   "exch": "NYSE", "name": "The Goldman Sachs Group, Inc."},
    "BAC":   {"price": 42.85,  "prev": 42.30,  "hi": 43.10,  "lo": 42.05,  "w52h": 48.08,  "w52l": 31.74,  "vol": 52_318_000, "mc": 338_000_000_000,   "exch": "NYSE", "name": "Bank of America Corporation"},
    "WFC":   {"price": 71.40,  "prev": 70.85,  "hi": 71.90,  "lo": 70.25,  "w52h": 81.50,  "w52l": 50.07,  "vol": 18_432_100, "mc": 237_000_000_000,   "exch": "NYSE", "name": "Wells Fargo & Company"},
    "BRK.B": {"price": 474.30, "prev": 471.50, "hi": 475.80, "lo": 470.20, "w52h": 496.15, "w52l": 354.10, "vol": 4_218_900,  "mc": 1_026_000_000_000, "exch": "NYSE", "name": "Berkshire Hathaway Inc."},
    "V":     {"price": 341.25, "prev": 338.90, "hi": 342.50, "lo": 337.80, "w52h": 369.73, "w52l": 271.41, "vol": 8_543_200,  "mc": 693_000_000_000,   "exch": "NYSE", "name": "Visa Inc."},
    "MA":    {"price": 508.40, "prev": 504.75, "hi": 510.20, "lo": 503.10, "w52h": 571.26, "w52l": 426.99, "vol": 5_218_700,  "mc": 471_000_000_000,   "exch": "NYSE", "name": "Mastercard Incorporated"},
    "XOM":   {"price": 107.85, "prev": 106.40, "hi": 108.90, "lo": 105.75, "w52h": 126.34, "w52l": 95.77,  "vol": 24_318_900, "mc": 446_000_000_000,   "exch": "NYSE", "name": "Exxon Mobil Corporation"},
    "CVX":   {"price": 145.20, "prev": 143.80, "hi": 146.10, "lo": 142.90, "w52h": 172.75, "w52l": 130.24, "vol": 11_218_300, "mc": 255_000_000_000,   "exch": "NYSE", "name": "Chevron Corporation"},
    "UNH":   {"price": 285.40, "prev": 281.90, "hi": 287.50, "lo": 280.20, "w52h": 630.73, "w52l": 249.50, "vol": 7_432_100,  "mc": 261_000_000_000,   "exch": "NYSE", "name": "UnitedHealth Group Incorporated"},
    "LLY":   {"price": 843.50, "prev": 836.20, "hi": 848.90, "lo": 832.40, "w52h": 972.53, "w52l": 680.84, "vol": 3_218_400,  "mc": 803_000_000_000,   "exch": "NYSE", "name": "Eli Lilly and Company"},
    "SPY":   {"price": 548.70, "prev": 544.85, "hi": 550.20, "lo": 543.40, "w52h": 613.23, "w52l": 480.04, "vol": 85_432_900, "mc": None,               "exch": "NYSE", "name": "SPDR S&P 500 ETF Trust"},
    "QQQ":   {"price": 471.30, "prev": 467.50, "hi": 473.10, "lo": 466.20, "w52h": 540.81, "w52l": 394.93, "vol": 47_218_300, "mc": None,               "exch": "NMS",  "name": "Invesco QQQ Trust Series 1"},
}


def _fetch_mock(symbol: str) -> dict:
    key = symbol.upper()
    if key not in _MOCK:
        raise HTTPException(
            404,
            f"Symbol '{symbol}' not found in mock data. Supported: {', '.join(sorted(_MOCK))}",
        )
    eq = _MOCK[key]
    seed = hash(key + str(int(time.time() // 300))) & 0xFFFF
    price = round(eq["price"] * (1 + math.sin(seed) * 0.003), 2)
    prev = eq["prev"]
    change = round(price - prev, 4)
    return {
        "symbol": key,
        "name": eq["name"],
        "exchange": eq["exch"],
        "instrument_type": "EQUITY",
        "currency": "USD",
        "price": price,
        "previous_close": prev,
        "change": change,
        "change_percent": round(change / prev * 100, 4),
        "day_high": eq["hi"],
        "day_low": eq["lo"],
        "volume": eq["vol"],
        "fifty_two_week_high": eq["w52h"],
        "fifty_two_week_low": eq["w52l"],
        "market_cap": eq["mc"],
        "data_source": "mock",
    }


# ---------------------------------------------------------------------------
# Provider selection
# ---------------------------------------------------------------------------

_PROVIDERS = [
    ("POLYGON_API_KEY",       _fetch_polygon),
    ("FINNHUB_API_KEY",       _fetch_finnhub),
    ("ALPHA_VANTAGE_API_KEY", _fetch_alpha_vantage),
]


def _active_provider() -> Optional[tuple[str, callable]]:
    for env_key, fn in _PROVIDERS:
        if os.environ.get(env_key):
            return env_key, fn
    # Yahoo Finance needs no key but requires working network
    if os.environ.get("USE_YAHOO_FINANCE", "").lower() in ("1", "true", "yes"):
        return "USE_YAHOO_FINANCE", _fetch_yahoo
    return None


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@app.get("/api/v1/equity/price/quote")
def get_equity_quote(symbol: str = Query(..., description="Stock ticker symbol, e.g. AAPL")):
    provider = _active_provider()
    now = datetime.now(tz=timezone.utc)

    if provider:
        env_key, fetch_fn = provider
        try:
            data = fetch_fn(symbol)
        except HTTPException:
            raise
        except Exception as exc:
            raise HTTPException(502, f"Data provider error: {exc}") from exc
    else:
        data = _fetch_mock(symbol)

    data["quote_time"] = now.isoformat()
    data["retrieved_at"] = now.isoformat()
    return data


@app.get("/health")
def health():
    provider = _active_provider()
    return {
        "status": "ok",
        "data_source": provider[0].lower() if provider else "mock",
        "timestamp": datetime.now(tz=timezone.utc).isoformat(),
    }


if __name__ == "__main__":
    cert = str(CERTS_DIR / "cert.pem")
    key  = str(CERTS_DIR / "key.pem")
    active = _active_provider()
    print(f"Data source: {active[0] if active else 'mock (set POLYGON_API_KEY, FINNHUB_API_KEY, or ALPHA_VANTAGE_API_KEY for live data)'}")
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=6901,
        ssl_certfile=cert,
        ssl_keyfile=key,
        log_level="info",
    )
