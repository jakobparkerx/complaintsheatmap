# save this as app.py

import streamlit as st
import pandas as pd
import pydeck as pdk

# Load your postcode_coordinates.csv file
df = pd.read_csv("postcode_coordinates.csv")

# Streamlit app
st.title("UK Postcode Heatmap")

st.map(df)  # Simple scatter map

# Optional: Pydeck Heatmap
st.subheader("Heatmap of Postcodes")
heatmap = pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(
        latitude=df['lat'].mean(),
        longitude=df['lon'].mean(),
        zoom=5,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'HeatmapLayer',
            data=df,
            get_position='[lon, lat]',
            aggregation=pdk.types.String("MEAN"),
            get_weight=1,
            radiusPixels=60,
        ),
    ],
)

st.pydeck_chart(heatmap)
