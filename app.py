import streamlit as st
import pandas as pd

from stock_data import get_dummy_stock_prices

st.set_page_config(page_title="Stock App", layout="wide")

st.title("📈 Stock App")
st.write("Hello Streamlit!")

symbol = st.selectbox("銘柄", ["NFLX"])

data = get_dummy_stock_prices(symbol)
df = pd.DataFrame(data)

st.subheader(f"{symbol} の株価推移")
st.line_chart(df.set_index("date")["price"])