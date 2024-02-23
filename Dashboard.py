import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt
import plotly.express as px

#Page Configurations
st.set_page_config(layout="wide",initial_sidebar_state="expanded")

st.sidebar.header("Input Parameters")
st.sidebar.header("Line Chart Parameters")
plot_data=st.sidebar.multiselect("Select Data",["Actual Productivity","Targeted Productivity"],["Actual Productivity","Targeted Productivity"])

st.sidebar.header("Select date Parameters")
d_min = st.sidebar.date_input("Select Start Date", dt.date(2015, 1, 1))
d_max = st.sidebar.date_input("Select End Date", dt.date(2015, 3, 11))
d_min=pd.to_datetime(d_min)
d_max=pd.to_datetime(d_max)

st.sidebar.header("Bar Chart 1 Parameters")
barchat1_parameter=st.sidebar.selectbox("Select a parameter",['Average Productivity', 'SMV', 'Incentive Pay','Number of Workers'])

st.sidebar.header("Bar Chart 2 Parameters")
barchat2_parameter=st.sidebar.selectbox("Select a parameter",['SMV', 'Incentive Pay','Number of Workers'])

#Dataset value
df=pd.read_csv("D:/University/3rd Year/2nd Semester/ST3082 Statistical Learning/Project APP/pythonProject/mydata.csv")
df.date=pd.to_datetime(df.date)
df=df.sort_values(by=['date'])
df = df[(df['date'] > d_min) & (df['date'] < d_max)]
df_teams=pd.DataFrame({"Team":list(range(1,13)),"Average Productivity":list(df.groupby(["team"]).actual_productivity.agg(np.mean)),"SMV":list(df.groupby(["team"]).smv.agg(np.mean)),"Incentive Pay":list(df.groupby(["team"]).incentive.agg(np.mean)),"Number of Workers":list(df.groupby(["team"]).no_of_workers.agg(np.mean))})

col1,col2=st.columns(2)
with col1:
    st.header("Teamwise Productivity")
    st.bar_chart(df_teams, y=barchat1_parameter, x="Team")

    st.header("Daily Productivity")
    df_date_nums_mean = df.groupby(["date_num"]).actual_productivity.agg(np.mean)
    df_date_nums_mean_targeted = df.groupby(["date_num"]).targeted_productivity.agg(np.mean)
    df_date_nums_mean = list(df_date_nums_mean)
    df_date_nums_mean_targeted = list(df_date_nums_mean_targeted)
    df_dates_means = pd.DataFrame({"Date": list(sorted(df.date_num.unique())), "Actual Productivity": df_date_nums_mean,
                                   "Targeted Productivity": df_date_nums_mean_targeted})
    st.line_chart(df_dates_means, x='Date', y=plot_data, height=500, width=500)

with col2:
    st.header("Teamwise Statistics")
    st.bar_chart(df_teams,y=barchat2_parameter,x="Team")
    #st.bar_chart(pd.DataFrame(df.groupby(["team"]).actual_productivity.agg(np.mean)),y='actual_productivity')
    st.header("Important KPI's")
    metricol1,metricol2=st.columns(2)
    with metricol1:
        st.metric("Workers", sum(df.no_of_workers))
        st.metric("Percentage of of Idle Workers", round(np.mean(df.idle_men),4)*100)
        st.metric("Total Incentive Pay in Dollars", (sum(df.incentive)))
    with metricol2:
        st.metric("Average Productivity", round(np.mean(df.actual_productivity), 4))
        st.metric("Totale Idle Time", sum(df.idle_time))
        st.metric("Total Overtime Pay in Dollars", (sum(df.over_time)))



