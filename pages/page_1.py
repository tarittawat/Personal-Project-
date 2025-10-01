import streamlit as st
import yfinance as yf
from App_Thingy import sidebar
def convert_for_download(data_real):
    return data_real.to_csv().encode("utf-8")

st.header("Plot a graph!!!!",divider="gray")

sidebar()


Box_input = st.text_input("Input a stock symbol")
if Box_input:
     period_input = st.text_input("What is your period to plot?:")
     ticker = yf.Ticker(Box_input)
     if period_input:
         data_real = ticker.history(period=period_input)
         csv = convert_for_download(data_real)
         data_show = st.selectbox("What data do you want to show?", ("Close","Open","Low","High"))
         if data_show:
              what_chart = st.selectbox("what chart: ", ("Line Chart","Area Chart","Bar Chart","Scatter Chart"))
              match what_chart:
                   case "Line Chart":
                         st.line_chart(data_real[data_show])
                   case "Area Chart":
                        st.area_chart(data_real[data_show])
                   case "Bar Chart":
                        st.bar_chart(data_real[data_show])
                   case "Scatter Chart":
                        st.scatter_chart(data_real[data_show])
              st.download_button(label="CSV file download",data = csv,file_name="Table.csv")


              



