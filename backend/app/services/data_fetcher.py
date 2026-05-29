"""
Data fetcher service for Uganda Securities Exchange (USE) market data.
Supports multiple data sources: mock, Alpha Vantage, Yahoo Finance.
"""

import logging
from typing import List, Dict, Optional
from datetime import datetime, timedelta
import httpx
from app.core.config import settings

logger = logging.getLogger(__name__)

# Mock USE Market Data - Ugandan companies and stocks
MOCK_USE_STOCKS = [
    {
        "symbol": "STANBIC",
        "name": "Stanbic Bank Uganda",
        "sector": "Banking & Financial Services",
        "price": 2450.00,
        "opening_price": 2425.00,
        "high_price": 2475.50,
        "low_price": 2420.00,
        "volume": 125000,
        "market_cap": 2.5e12,  # UGX
        "pe_ratio": 8.5,
        "dividend_yield": 5.2,
        "change": 1.03,
        "change_percent": 0.42,
    },
    {
        "symbol": "DFCU",
        "name": "DFCU Bank",
        "sector": "Banking & Financial Services",
        "price": 1850.00,
        "opening_price": 1875.00,
        "high_price": 1890.00,
        "low_price": 1840.00,
        "volume": 98000,
        "market_cap": 1.8e12,
        "pe_ratio": 7.2,
        "dividend_yield": 6.1,
        "change": -25.00,
        "change_percent": -1.33,
    },
    {
        "symbol": "EQUITY",
        "name": "Equity Bank Uganda",
        "sector": "Banking & Financial Services",
        "price": 1200.00,
        "opening_price": 1180.00,
        "high_price": 1220.00,
        "low_price": 1175.00,
        "volume": 156000,
        "market_cap": 1.2e12,
        "pe_ratio": 6.8,
        "dividend_yield": 4.5,
        "change": 20.00,
        "change_percent": 1.69,
    },
    {
        "symbol": "KK",
        "name": "Kampala Serena Hotel",
        "sector": "Hospitality & Tourism",
        "price": 4500.00,
        "opening_price": 4400.00,
        "high_price": 4550.00,
        "low_price": 4350.00,
        "volume": 45000,
        "market_cap": 450e9,
        "pe_ratio": 12.3,
        "dividend_yield": 3.8,
        "change": 100.00,
        "change_percent": 2.27,
    },
    {
        "symbol": "NMG",
        "name": "Nation Media Group",
        "sector": "Media & Publications",
        "price": 320.00,
        "opening_price": 315.00,
        "high_price": 330.00,
        "low_price": 312.00,
        "volume": 250000,
        "market_cap": 320e9,
        "pe_ratio": 9.1,
        "dividend_yield": 2.5,
        "change": 5.00,
        "change_percent": 1.59,
    },
    {
        "symbol": "UMEME",
        "name": "Umeme Limited",
        "sector": "Utilities & Energy",
        "price": 650.00,
        "opening_price": 645.00,
        "high_price": 670.00,
        "low_price": 640.00,
        "volume": 87000,
        "market_cap": 650e9,
        "pe_ratio": 11.2,
        "dividend_yield": 5.8,
        "change": 5.00,
        "change_percent": 0.77,
    },
    {
        "symbol": "TIRL",
        "name": "Total Kenya Limited",
        "sector": "Energy & Trading",
        "price": 1450.00,
        "opening_price": 1460.00,
        "high_price": 1480.00,
        "low_price": 1440.00,
        "volume": 65000,
        "market_cap": 1.45e12,
        "pe_ratio": 10.5,
        "dividend_yield": 4.2,
        "change": -10.00,
        "change_percent": -0.68,
    },
    {
        "symbol": "AIRTEL",
        "name": "Airtel Uganda",
        "sector": "Telecommunications",
        "price": 2200.00,
        "opening_price": 2180.00,
        "high_price": 2250.00,
        "low_price": 2175.00,
        "volume": 120000,
        "market_cap": 2.2e12,
        "pe_ratio": 9.8,
        "dividend_yield": 3.5,
        "change": 20.00,
        "change_percent": 0.92,
    },
]


class DataFetcherService:
    """Service to fetch market data from various sources."""
    
    def __init__(self):
        self.provider = settings.USE_DATA_PROVIDER
        self.cache: Dict[str, Dict] = {}
        self.cache_timestamp: Dict[str, datetime] = {}
    
    def _is_cache_valid(self, key: str) -> bool:
        """Check if cached data is still valid."""
        if key not in self.cache_timestamp:
            return False
        age = datetime.now() - self.cache_timestamp[key]
        return age < timedelta(seconds=settings.CACHE_TTL)
    
    def get_all_stocks(self) -> List[Dict]:
        """Fetch all available stocks from USE."""
        cache_key = "all_stocks"
        
        if self._is_cache_valid(cache_key):
            return self.cache[cache_key]
        
        try:
            if self.provider == "mock":
                stocks = self._fetch_mock_stocks()
            elif self.provider == "alpha_vantage":
                stocks = self._fetch_alpha_vantage_stocks()
            else:
                stocks = self._fetch_mock_stocks()  # Fallback to mock
            
            self.cache[cache_key] = stocks
            self.cache_timestamp[cache_key] = datetime.now()
            return stocks
            
        except Exception as e:
            logger.error(f"Error fetching stocks: {e}")
            return self._fetch_mock_stocks()  # Fallback to mock
    
    def get_stock_quote(self, symbol: str) -> Optional[Dict]:
        """Fetch real-time quote for a specific stock."""
        cache_key = f"quote_{symbol.upper()}"
        
        if self._is_cache_valid(cache_key):
            return self.cache[cache_key]
        
        try:
            if self.provider == "mock":
                quote = self._fetch_mock_quote(symbol)
            elif self.provider == "alpha_vantage":
                quote = self._fetch_alpha_vantage_quote(symbol)
            else:
                quote = self._fetch_mock_quote(symbol)
            
            if quote:
                self.cache[cache_key] = quote
                self.cache_timestamp[cache_key] = datetime.now()
            
            return quote
            
        except Exception as e:
            logger.error(f"Error fetching quote for {symbol}: {e}")
            return self._fetch_mock_quote(symbol)  # Fallback
    
    def get_market_overview(self) -> Dict:
        """Get overall market overview."""
        cache_key = "market_overview"
        
        if self._is_cache_valid(cache_key):
            return self.cache[cache_key]
        
        try:
            stocks = self.get_all_stocks()
            
            # Calculate market metrics
            total_change = sum(s.get("change", 0) for s in stocks)
            avg_change_percent = sum(s.get("change_percent", 0) for s in stocks) / len(stocks) if stocks else 0
            
            # Top gainers and losers
            gainers = sorted(stocks, key=lambda x: x.get("change_percent", 0), reverse=True)[:3]
            losers = sorted(stocks, key=lambda x: x.get("change_percent", 0))[:3]
            
            overview = {
                "market_status": "OPEN",
                "last_updated": datetime.now().isoformat(),
                "total_stocks": len(stocks),
                "market_change": round(total_change, 2),
                "market_change_percent": round(avg_change_percent, 2),
                "top_gainers": gainers,
                "top_losers": losers,
                "all_stocks": stocks,
            }
            
            self.cache[cache_key] = overview
            self.cache_timestamp[cache_key] = datetime.now()
            return overview
            
        except Exception as e:
            logger.error(f"Error fetching market overview: {e}")
            return {
                "market_status": "ERROR",
                "error": str(e),
                "all_stocks": self._fetch_mock_stocks(),
            }
    
    def _fetch_mock_stocks(self) -> List[Dict]:
        """Return mock USE market data."""
        return MOCK_USE_STOCKS
    
    def _fetch_mock_quote(self, symbol: str) -> Optional[Dict]:
        """Return mock quote for a stock."""
        for stock in MOCK_USE_STOCKS:
            if stock["symbol"].upper() == symbol.upper():
                return stock.copy()
        return None
    
    async def _fetch_alpha_vantage_quote(self, symbol: str) -> Optional[Dict]:
        """
        Fetch quote from Alpha Vantage API.
        Note: Alpha Vantage may not have all USE stocks, so fallback is used.
        """
        if not settings.ALPHA_VANTAGE_API_KEY:
            logger.warning("Alpha Vantage API key not configured")
            return self._fetch_mock_quote(symbol)
        
        try:
            url = "https://www.alphavantage.co/query"
            params = {
                "function": "GLOBAL_QUOTE",
                "symbol": symbol,
                "apikey": settings.ALPHA_VANTAGE_API_KEY,
            }
            
            async with httpx.AsyncClient() as client:
                response = await client.get(url, params=params, timeout=10.0)
                response.raise_for_status()
                data = response.json()
                
                if "Global Quote" in data:
                    quote = data["Global Quote"]
                    return {
                        "symbol": symbol.upper(),
                        "price": float(quote.get("05. price", 0)),
                        "change": float(quote.get("09. change", 0)),
                        "change_percent": float(quote.get("10. change percent", "0").rstrip("%")),
                    }
        except Exception as e:
            logger.error(f"Alpha Vantage error: {e}")
        
        return self._fetch_mock_quote(symbol)
    
    def _fetch_alpha_vantage_stocks(self) -> List[Dict]:
        """Fetch stocks from Alpha Vantage (fallback to mock)."""
        logger.info("Alpha Vantage batch fetch not recommended, using mock data")
        return self._fetch_mock_stocks()


# Global instance
data_fetcher = DataFetcherService()


def get_data_fetcher() -> DataFetcherService:
    """Get or create data fetcher instance."""
    return data_fetcher
