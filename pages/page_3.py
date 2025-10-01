import yfinance as yf
import streamlit as st 
import pandas as pd
from App_Thingy import sidebar

st.header("Create your personal table")
st.divider()
sidebar()

#Start storing session state data
if 'stock_data' not in st.session_state:
    st.session_state.stock_data = pd.DataFrame(columns=[
        "Stock", "Shares", "Buying Price", "Current price", "p/l(per stock)"
    ])

c1,c2,c3 = st.columns(3,vertical_alignment="center")
with c1:
     stock_input = st.text_input("Stock symbol")
with c2:
     shares_input = st.number_input("How many shares do you own?")
with c3:
     buying_price = st.number_input("What is your buying price?")

total = 0
if st.button("Add Stock"):
    if stock_input and shares_input and buying_price:
        ticker = yf.Ticker(stock_input)
        data = ticker.history(period="1d")
        profit_loss = (data["Close"].iloc[-1] - buying_price) * shares_input
        new_row = pd.DataFrame([{
            "Stock": stock_input,
            "Shares": shares_input,
            "Buying Price": buying_price,
            "Current price": data["Close"].iloc[-1],
            "p/l(per stock)": profit_loss
        }])
        # Add new values
        st.session_state.stock_data = pd.concat([st.session_state.stock_data, new_row], ignore_index=True)

# Display the updated table
if not st.session_state.stock_data.empty:
 st.dataframe(st.session_state.stock_data, hide_index=True)


