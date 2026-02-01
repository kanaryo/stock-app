from datetime import date, timedelta
import yfinance as yf
import pandas as pd

# ダミー株価ロジック
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

# Yahoo Finance から株価取得ロジック
def get_stock_prices(symbol: str, period: str = "1mo"):
    """
    Yahoo Finance から株価取得
    period: 5d / 1mo / 3mo / 1y など
    """

    df = yf.download(symbol, period=period, progress=False)

    df = df.reset_index()[["Date", "Close"]]
    df.columns = ["date", "price"]

    return df