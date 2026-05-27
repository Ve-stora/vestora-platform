MOCK_STOCKS = [
    {"symbol": "NCB", "name": "National Capital Bank", "price": 1200.00, "change": 2.5},
    {"symbol": "DFCU", "name": "DFCU Bank", "price": 1050.00, "change": -1.2},
    {"symbol": "EBL", "name": "Equity Bank", "price": 850.50, "change": 3.1},
    {"symbol": "UMEME", "name": "Umeme Limited", "price": 650.00, "change": 0.8},
    {"symbol": "TIRL", "name": "Total Kenya Limited", "price": 1450.00, "change": -0.5},
]

def get_market_overview():
    return {
        "market_index": 8542.35,
        "market_change": 1.2,
        "market_status": "OPEN",
        "top_gainers": MOCK_STOCKS[:2],
        "top_losers": MOCK_STOCKS[1:3],
        "all_stocks": MOCK_STOCKS
    }

def get_stock_data(symbol: str):
    stock = next((s for s in MOCK_STOCKS if s["symbol"] == symbol), None)
    return {**stock, "high": stock["price"]*1.05, "low": stock["price"]*0.95} if stock else None
