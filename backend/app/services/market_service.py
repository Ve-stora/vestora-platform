# Market data service — fetch from USE data feeds or mock data
class MarketService:
    def get_market_summary(self):
        # TODO: Connect to live USE data feed
        return {"status": "open", "total_volume": 0, "advancers": 0, "decliners": 0}
