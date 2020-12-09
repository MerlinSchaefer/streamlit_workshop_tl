# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 10:50:04 2020

@author: ms101
"""


#STREAMLIT STOCK PRICES (DATAPROF TUTORIAL)

import streamlit as st
import pandas as pd
import plotly.express as px
import yfinance as yf



url_sp500 = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
@st.cache
def load_data(url):
    html = pd.read_html(url,header=0)
    df = html[0]
    return df

df = load_data(url_sp500)
sector = df.groupby('GICS Sector')



## STREAMLIT

st.header("S&P 500 Stock Data")

st.write("""You can use this WebApp to View the S&P 500 Stock Data for the past month.
         Use the sidebar to choose a sector and the dropdown menu to select a specific company.
         The companies stock data will be shown in the interactive plot.
         The basic descriptive data for all companies from the selected sector(s) can 
         be found under 'Company Data'. """)
         
st.write("*Note:* It may take a moment to load the complete current stock data.")

sorted_sector_unique = sorted( df['GICS Sector'].unique() )
selected_sector = st.sidebar.multiselect('Sector', sorted_sector_unique, sorted_sector_unique)

# Filtering data
df_selected_sector = df[ (df['GICS Sector'].isin(selected_sector)) ]

st.header('Display Companies in Selected Sector')
st.write('Data Dimension: ' + str(df_selected_sector.shape[0]) + ' rows and ' + str(df_selected_sector.shape[1]) + ' columns.')
if st.button("View Company Data"):
    st.dataframe(df_selected_sector)
    if st.button("Hide"):
        st.button = "False"#change or take out


stock_data = yf.download(
        tickers = list(df_selected_sector[:].Symbol),
        period = "ytd",
        interval = "1d",
        group_by = 'ticker',
        auto_adjust = True,
        prepost = True,
        threads = True,
        proxy = None
    )


def price_plot(symbol):
    df = pd.DataFrame(stock_data[symbol].Close)
    df['Date'] = df.index
    fig = px.line(df, x = "Date", 
                  y = "Close", 
                  title = (df_selected_sector.loc[df_selected_sector['Symbol'] == symbol, 'Security'].iloc[0] +" "+"("+symbol+")"),
                           labels=dict(Date="Date", Close="Close ($)")
                  )
    fig.update_xaxes(nticks = 12,tickangle=55)
    fig.update_yaxes(range = [0,max(df["Close"]+50)])
    return st.plotly_chart(fig)


company = st.sidebar.selectbox("Select a company",list(df_selected_sector.Security))

st.header('Stock Closing Price')

price_plot(df_selected_sector.loc[df_selected_sector['Security'] == company, 'Symbol'].iloc[0])    