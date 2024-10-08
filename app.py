import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st

st.sidebar.title("India Data Analysis")
df = pd.read_csv("India_data.csv")
state_list  = list(df["State"].unique())
state_list.insert(0,"Overall India")


#this code for make a project frame how look our website
selected_state = st.sidebar.selectbox("Select any state",options=state_list)
primary = st.sidebar.selectbox("Select primary parameter",options = sorted(df.columns[6:]))
secondary = st.sidebar.selectbox("Select secondary parameter",options = sorted(df.columns[6:]))

plot = st.sidebar.button("Plot graph")

if plot:




    if selected_state == 'Overall India':
        # plot for india

        st.subheader(f"Top 10 state of maximum {primary} and it's {secondary}")
        for i in df.columns:
            for j in df.columns:
                if i == primary and j == secondary:
                    list_top5 = df.groupby("State")[[i,j]].sum().sort_values(by=[i,j],ascending=[False,False])
                    st.dataframe(list_top5)

        st.subheader('1)Size represent primary parameter')
        st.subheader('2)Color represents secondary parameter')
        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=4,size_max=35,
                                mapbox_style="carto-positron",width=1200,height=700,hover_name='District')

        st.plotly_chart(fig,use_container_width=True)
    else:
        state_df = df[df['State'] == selected_state]
        st.subheader(f"Top 10 district of maximum {primary} and it's {secondary}")
        for i in state_df.columns:
            for j in state_df.columns:
             if i == primary and j == secondary:
                list_top5 = state_df.groupby("District")[[i,j]].sum().sort_values(by=[i,j],ascending=[False,False]).head(10)
                st.dataframe(list_top5)




        st.subheader('*Size represent primary parameter')
        st.subheader('*Color represents secondary parameter')
        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=primary, color=secondary, zoom=6,
                                size_max=35,
                                mapbox_style="carto-positron", width=1200, height=700,
                                hover_name='District')



        st.plotly_chart(fig, use_container_width=True)