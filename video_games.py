#from alpha_vantage.timeseries import TimeSeries
import streamlit as st
import pandas as pd
#key = '49FFUFQG9LOCTHR'

#ts = TimeSeries(key, output_format='pandas')
#data = ts.get_monthly_adjusted('MSFT')


df = pd.read_csv("C:\more.csv")

st.dataframe(df)

#Y
