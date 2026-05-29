from typing import List, Optional
from app.models.stock import Stock

# Mock data for MVP
MOCK_STOCKS = [
    {"symbol": "STANBIC", "name": "Stanbic Bank Uganda", "sector": "Banking", "price": 2450.0, "pe_ratio": 8.5},
    {"symbol": "DFCU", "name": "DFCU Bank", "sector": "Banking", "price": 1850.0, "pe_ratio": 7.2},
    {"symbol": "EQUITY", "name": "Equity Bank Uganda", "sector": "Banking", "price": 1200.0, "pe_ratio": 6.8},
    {"symbol": "KK", "name": "Kampala Serena Hotel", "sector": "Hospitality", "price": 4500.0, "pe_ratio": 12.3},
    {"symbol": "NMG", "name": "Nation Media Group", "sector": "Media", "price": 320.0, "pe_ratio": 9.1},
]

def get_market_overview():
    """Return market overview with mock data"""
    return {
        "total_stocks": len(MOCK_STOCKS),
        "stocks": MOCK_STOCKS,
        "market_status": "open",
        "last_updated": "2026-05-29T10:00:00Z"
    }

def get_stock_data(symbol: str) -> Optional[dict]:
    """Get specific stock data"""
    for stock in MOCK_STOCKS:
        if stock["symbol"].upper() == symbol.upper():
            return stock
    return None