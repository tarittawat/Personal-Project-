import streamlit as st


st.title("Welcome to the multi-tool stock thingy!!!")
st.subheader("Please choose a functionality")
st.divider()

#sidebar
class sidebar():
    def __init__(self):
        with st.sidebar:
            self.home_page = st.page_link("App_Thingy.py",label ="Home",icon = "🏠")
            self.page_1 = st.page_link("pages/page_1.py",label ="Track Plot",icon="📈")
            self.page_2 = st.page_link("pages/page_2.py",label="Live noti",icon="‼️")
            self.page_3 = st.page_link("pages/page_3.py",label="Your portfolio",icon="📋")

sidebar()

#columns 
col1,col2,col3 = st.columns(3,vertical_alignment="top")
with col1:
    st.page_link("pages/page_1.py",label ="Track Plot",icon="📈")
with col2:
    st.page_link("pages/page_2.py",label="Live noti",icon="‼️")
with col3:
    st.page_link("pages/page_3.py",label="Your portfolio",icon="📋")