from stock_data import get_dummy_stock_prices

# テスト目的：
# 株価取得関数が、例外を出さずに list 型のデータを返すことを確認する
def test_get_dummy_stock_prices_returns_list():
    data = get_dummy_stock_prices("AAPL")
    assert isinstance(data, list)

# テスト目的：
# 取得した株価データの各要素が、
# UI や API で利用する前提の構造（date / price）を持っていることを確認する
def test_get_dummy_stock_prices_structure():
    data = get_dummy_stock_prices("AAPL")

    first = data[0]
    assert "date" in first
    assert "price" in first
