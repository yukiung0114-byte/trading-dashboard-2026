import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="VCP Trader Dashboard", layout="wide")

st.title("📈 VCP Market Scanner")

# Sidebar for inputs
ticker = st.sidebar.text_input("Enter Ticker", value="NVDA")

if st.sidebar.button("Run Analysis"):
    data = yf.download(ticker, period="1y")
    st.subheader(f"Technical Data for {ticker}")
    st.write(data.tail())
    st.line_chart(data['Close'])