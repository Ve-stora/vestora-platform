# Notification service — email and push alert delivery
class NotificationService:
    def send_price_alert(self, user_id: int, symbol: str, price: float):
        # TODO: Integrate email / push notification
        print(f"ALERT: {symbol} hit {price} for user {user_id}")
