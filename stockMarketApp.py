import streamlit as st
import yfinance as yf   #install yahoo finance stock market data of different companies
import datetime

ticker_symbol = st.text_input("Enter the stock name", "AAPL")

col1, col2 = st.columns(2)

with col1:
    start_date = st.date_input("Start_date", datetime.date(2019, 7, 6))
with col2:
    end_date = st.date_input("Start_date", datetime.date(2023, 7, 6))

data = yf.download(ticker_symbol, start = start_date, end = end_date)

st.write(data)

st.line_chart(data["Close"])


st.bar_chart(data["Volume"])