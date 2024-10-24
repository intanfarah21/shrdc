import streamlit as st

st.set_page_config(page_icon="intan")
st.header("Banking Information")
st.sidebar.write('main page')


import pandas as pd
df = pd.read_csv('banking.csv')
df



