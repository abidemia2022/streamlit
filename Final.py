"""
Streamlit Interactive Plots Demo
    
Example of a line chart of time-series simulation in Matplotlib
"""

import streamlit as st
import pandas as pd
import plotly.express as px


#Two Charts

st.title("Consumer Price Index (CPI)")



final4 = pd.read_csv("final4.csv")
final5 = pd.read_csv("final5.csv")

#Drop first year due to scaling

final4 = final4[final4['year'] != 2013]
final5 = final5[final5['year'] != 2013]

#Change percent to  %

final4['percent_change'] = final4['percent_change']*100
final5['percent_change'] = final5['percent_change']*100

slist = final4['seriesID'].unique()

series = st.sidebar.selectbox("Select a CPI series:",slist)

st.header("Urban Consumers")

col1,col2 = st.columns(2)

#Chart 1

fig = px.line(final4[final4['seriesID'] == series], x = "date_time", y = "percent_change", title = series).update_layout(xaxis_title="Date", yaxis_title="Percent Change (%)")

col1.plotly_chart(fig)

#Chart 2

fig2 = px.line(final5[final5['seriesID'] == series], x = 'period', y = 'percent_change', title = series + ' per Year',color = 'year').update_layout(xaxis_title="Month", yaxis_title="Percent Change (%)")

col2.plotly_chart(fig2, use_container_width = True)

# Notes:
# - Switch from function to procedural
# - Lag in rendering
# - When you deploy you have to add an external dependency file (requirements.txt)
