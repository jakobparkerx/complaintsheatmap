import streamlit as st
import pandas as pd
import pydeck as pdk

# Load your CSV
df = pd.read_csv("postcode_coordinates.csv")

# Streamlit app title
st.title("UK Postcode Complaints Heatmap")

# Dropdown to select sub_category
sub_categories = df['sub_category'].unique()
selected_sub_category = st.selectbox("Select Complaint Sub-Category", sub_categories)

# Filter data
filtered_df = df[df['sub_category'] == selected_sub_category]

# Pydeck scatter map
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

# Show the map
st.pydeck_chart(pdk.Deck(layers=[layer], initial_view_state=view_state))

