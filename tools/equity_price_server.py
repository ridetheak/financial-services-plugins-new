"""
Equity Price API Server
Exposes: GET /api/v1/equity/price/quote?symbol=<TICKER>
Runs on: https://127.0.0.1:6901

Uses realistic mock data with seeded intraday variation.
"""

import math
import time
from datetime import datetime, timezone
from pathlib import Path

from fastapi import FastAPI, Query, HTTPException
import uvicorn

app = FastAPI(title="Equity Price API", version="1.0.0")

CERTS_DIR = Path(__file__).parent / "certs"

# Realistic reference data: (price, prev_close, day_high, day_low, 52w_high, 52w_low, volume, market_cap, exchange)
MOCK_EQUITIES: dict[str, dict] = {
    "AAPL":  {"price": 213.55, "prev_close": 211.40, "day_high": 214.90, "day_low": 210.85, "w52_high": 237.23, "w52_low": 164.08, "volume": 58_432_100, "market_cap": 3_245_000_000_000, "exchange": "NMS",  "name": "Apple Inc."},
    "MSFT":  {"price": 421.30, "prev_close": 418.75, "day_high": 423.10, "day_low": 417.20, "w52_high": 468.35, "w52_low": 344.79, "volume": 21_876_400, "market_cap": 3_130_000_000_000, "exchange": "NMS",  "name": "Microsoft Corporation"},
    "GOOGL": {"price": 175.85, "prev_close": 174.10, "day_high": 176.90, "day_low": 173.65, "w52_high": 207.05, "w52_low": 140.53, "volume": 19_543_200, "market_cap": 2_190_000_000_000, "exchange": "NMS",  "name": "Alphabet Inc."},
    "AMZN":  {"price": 205.40, "prev_close": 203.90, "day_high": 206.75, "day_low": 202.55, "w52_high": 242.52, "w52_low": 151.61, "volume": 35_218_900, "market_cap": 2_200_000_000_000, "exchange": "NMS",  "name": "Amazon.com, Inc."},
    "NVDA":  {"price": 875.40, "prev_close": 861.25, "day_high": 882.50, "day_low": 858.10, "w52_high": 974.00, "w52_low": 462.41, "volume": 42_876_100, "market_cap": 2_155_000_000_000, "exchange": "NMS",  "name": "NVIDIA Corporation"},
    "TSLA":  {"price": 248.50, "prev_close": 244.10, "day_high": 251.30, "day_low": 241.80, "w52_high": 414.50, "w52_low": 138.80, "volume": 98_432_700, "market_cap": 795_000_000_000,   "exchange": "NMS",  "name": "Tesla, Inc."},
    "META":  {"price": 513.20, "prev_close": 508.75, "day_high": 516.40, "day_low": 506.30, "w52_high": 638.40, "w52_low": 414.50, "volume": 14_329_800, "market_cap": 1_305_000_000_000, "exchange": "NMS",  "name": "Meta Platforms, Inc."},
    "JPM":   {"price": 234.85, "prev_close": 232.40, "day_high": 236.10, "day_low": 231.50, "w52_high": 280.25, "w52_low": 183.49, "volume": 10_218_300, "market_cap": 671_000_000_000,   "exchange": "NYSE", "name": "JPMorgan Chase & Co."},
    "GS":    {"price": 512.30, "prev_close": 508.10, "day_high": 515.20, "day_low": 506.80, "w52_high": 601.89, "w52_low": 395.63, "volume": 3_218_700,  "market_cap": 168_000_000_000,   "exchange": "NYSE", "name": "The Goldman Sachs Group, Inc."},
    "BAC":   {"price": 42.85,  "prev_close": 42.30,  "day_high": 43.10,  "day_low": 42.05,  "w52_high": 48.08,  "w52_low": 31.74,  "volume": 52_318_000, "market_cap": 338_000_000_000,   "exchange": "NYSE", "name": "Bank of America Corporation"},
    "WFC":   {"price": 71.40,  "prev_close": 70.85,  "day_high": 71.90,  "day_low": 70.25,  "w52_high": 81.50,  "w52_low": 50.07,  "volume": 18_432_100, "market_cap": 237_000_000_000,   "exchange": "NYSE", "name": "Wells Fargo & Company"},
    "BRK.B": {"price": 474.30, "prev_close": 471.50, "day_high": 475.80, "day_low": 470.20, "w52_high": 496.15, "w52_low": 354.10, "volume": 4_218_900,  "market_cap": 1_026_000_000_000, "exchange": "NYSE", "name": "Berkshire Hathaway Inc."},
    "V":     {"price": 341.25, "prev_close": 338.90, "day_high": 342.50, "day_low": 337.80, "w52_high": 369.73, "w52_low": 271.41, "volume": 8_543_200,  "market_cap": 693_000_000_000,   "exchange": "NYSE", "name": "Visa Inc."},
    "MA":    {"price": 508.40, "prev_close": 504.75, "day_high": 510.20, "day_low": 503.10, "w52_high": 571.26, "w52_low": 426.99, "volume": 5_218_700,  "market_cap": 471_000_000_000,   "exchange": "NYSE", "name": "Mastercard Incorporated"},
    "XOM":   {"price": 107.85, "prev_close": 106.40, "day_high": 108.90, "day_low": 105.75, "w52_high": 126.34, "w52_low": 95.77,  "volume": 24_318_900, "market_cap": 446_000_000_000,   "exchange": "NYSE", "name": "Exxon Mobil Corporation"},
    "CVX":   {"price": 145.20, "prev_close": 143.80, "day_high": 146.10, "day_low": 142.90, "w52_high": 172.75, "w52_low": 130.24, "volume": 11_218_300, "market_cap": 255_000_000_000,   "exchange": "NYSE", "name": "Chevron Corporation"},
    "UNH":   {"price": 285.40, "prev_close": 281.90, "day_high": 287.50, "day_low": 280.20, "w52_high": 630.73, "w52_low": 249.50, "volume": 7_432_100,  "market_cap": 261_000_000_000,   "exchange": "NYSE", "name": "UnitedHealth Group Incorporated"},
    "LLY":   {"price": 843.50, "prev_close": 836.20, "day_high": 848.90, "day_low": 832.40, "w52_high": 972.53, "w52_low": 680.84, "volume": 3_218_400,  "market_cap": 803_000_000_000,   "exchange": "NYSE", "name": "Eli Lilly and Company"},
    "SPY":   {"price": 548.70, "prev_close": 544.85, "day_high": 550.20, "day_low": 543.40, "w52_high": 613.23, "w52_low": 480.04, "volume": 85_432_900, "market_cap": None,               "exchange": "NYSE", "name": "SPDR S&P 500 ETF Trust"},
    "QQQ":   {"price": 471.30, "prev_close": 467.50, "day_high": 473.10, "day_low": 466.20, "w52_high": 540.81, "w52_low": 394.93, "volume": 47_218_300, "market_cap": None,               "exchange": "NMS",  "name": "Invesco QQQ Trust Series 1"},
}


def _intraday_variation(symbol: str, base: float) -> float:
    """Return a small deterministic intraday variation so prices aren't static."""
    seed = hash(symbol + str(int(time.time() // 300))) & 0xFFFF  # changes every 5 min
    variation_pct = (math.sin(seed) * 0.003)  # ±0.3%
    return round(base * (1 + variation_pct), 2)


@app.get("/api/v1/equity/price/quote")
def get_equity_quote(symbol: str = Query(..., description="Stock ticker symbol, e.g. AAPL")):
    key = symbol.upper()
    if key not in MOCK_EQUITIES:
        raise HTTPException(
            status_code=404,
            detail=f"Symbol '{symbol}' not found. Supported symbols: {', '.join(sorted(MOCK_EQUITIES))}",
        )

    eq = MOCK_EQUITIES[key]
    price = _intraday_variation(key, eq["price"])
    prev_close = eq["prev_close"]
    change = round(price - prev_close, 4)
    change_pct = round((change / prev_close) * 100, 4)
    now = datetime.now(tz=timezone.utc)

    return {
        "symbol": key,
        "name": eq["name"],
        "exchange": eq["exchange"],
        "instrument_type": "EQUITY",
        "currency": "USD",
        "price": price,
        "previous_close": prev_close,
        "change": change,
        "change_percent": change_pct,
        "day_high": eq["day_high"],
        "day_low": eq["day_low"],
        "volume": eq["volume"],
        "fifty_two_week_high": eq["w52_high"],
        "fifty_two_week_low": eq["w52_low"],
        "market_cap": eq["market_cap"],
        "quote_time": now.isoformat(),
        "retrieved_at": now.isoformat(),
    }


@app.get("/health")
def health():
    return {"status": "ok", "timestamp": datetime.now(tz=timezone.utc).isoformat()}


if __name__ == "__main__":
    cert = str(CERTS_DIR / "cert.pem")
    key = str(CERTS_DIR / "key.pem")
    uvicorn.run(
        app,
        host="127.0.0.1",
        port=6901,
        ssl_certfile=cert,
        ssl_keyfile=key,
        log_level="info",
    )
