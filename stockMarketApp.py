import streamlit as st
import yfinance as yf   #install yahoo finance stock market data of different companies
import datetime

ticker_symbol = st.text_input("Enter the stock name", "AAPL")
start_date = st.date_input("Start_date", datetime.date(2019, 7, 6))
end_date = st.date_input("Start_date", datetime.date(2023, 7, 6))

data = yf.download(ticker_symbol, start = start_date, end = end_date)

data.write(data)