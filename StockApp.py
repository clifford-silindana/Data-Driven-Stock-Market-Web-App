import yfinance as yf
import streamlit as st
import pandas as pd 


st.title("Stock Market App")
st.header("Looking at the market history of Apple Inc. ")

excel = pd.read_csv("AAPL.csv")

st.write("First 2.5 years of the period")
excel_head = excel.head()

st.write(excel_head)

ticker = "GOOG"
tickerData = yf.Ticker(ticker)
tickerHistory = tickerData.history(period = "6M", start = "2000-04-15", end = "2022-05-15")
st.line_chart(tickerHistory.Close)



excel_tail = excel.tail()
st.write("""Last 2.5 years of the period """)
st.write(excel_tail)


st.line_chart(tickerHistory.Volume)
