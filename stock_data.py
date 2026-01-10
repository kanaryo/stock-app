from datetime import date, timedelta

#ダミー株価ロジック
def get_dummy_stock_prices(symbol: str):
    today = date.today()
    prices = [150, 152, 149, 153, 155]

    return [
        {
            "date": today - timedelta(days=i),
            "price": prices[i]
        }
        for i in range(len(prices))
    ][::-1]
