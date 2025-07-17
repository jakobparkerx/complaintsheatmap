import streamlit as st
import pandas as pd
import pydeck as pdk


df = pd.read_csv("postcode_coordinates.csv")


st.title("2024 'Appointment Needed' Complaints Heatmap")


sub_categories = df['sub_category'].unique()
selected_sub_category = st.selectbox("Select Complaint Sub-Category", sub_categories)


filtered_df = df[df['sub_category'] == selected_sub_category]


layer = pdk.Layer(
    'ScatterplotLayer',
    data=filtered_df,
    get_position='[lon, lat]',
    get_fill_color='[255, 0, 0, 255]',
    get_radius=1500,  
)

view_state = pdk.ViewState(
    latitude=filtered_df['lat'].mean(),
    longitude=filtered_df['lon'].mean(),
    zoom=7,
    pitch=0,
)


st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))

