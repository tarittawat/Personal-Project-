from windows_toasts import WindowsToaster,Toast
import time
import streamlit as st
import yfinance as yf
from App_Thingy import sidebar

st.header("Notify when a stock goes above/below YOUR threshold!",divider="gray")
sidebar()

stock_name = st.text_input("Input stock symbol")
if stock_name:
    ticker  = yf.Ticker(stock_name)
    data = ticker.history(period="1d")
    above_below = st.selectbox("Alert Threshold?",("above","below"))
    match above_below:
        case "above":
            alert_threshold = st.number_input("Your Alert threshold")
            if alert_threshold:
                while True:
                    current = float(data["Close"].iloc[-1])
                    st.caption("Current %s prices: %f" %(stock_name,current))
                    if alert_threshold < current:
                        in_yo_face = WindowsToaster("Stock tracking app")
                        bread = Toast()
                        bread.text_fields = ["%s is above %.6f currently at: %.6f!!!!!!" %(stock_name,alert_threshold,current)]
                        in_yo_face.show_toast(bread)
                    time.sleep(60)
        case "below":
            alert_threshold = st.number_input("Your Alert threshold")
            if alert_threshold:
                while True:
                    current = float(data["Close"].iloc[-1])
                    st.caption("Current %s prices: %f" %(stock_name,current))
                    if alert_threshold > current:
                        in_yo_face = WindowsToaster("Stock tracking app")
                        bread = Toast()
                        bread.text_fields = ["%s is below %.6f currently at: %.6f!!!!!!" %(stock_name,alert_threshold,current)]
                        in_yo_face.show_toast(bread)
                    time.sleep(60)



