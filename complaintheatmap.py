import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title("UK Postcode Complaints Scatter Map")

# Load the default CSV file
default_file = "postcode_coordinates.csv"

try:
    df = pd.read_csv(default_file)
except FileNotFoundError:
    st.error(f"Default CSV not found at {default_file}. Please make sure the file exists.")
    st.stop()

# Validate required columns
required_columns = {'postcode', 'lat', 'lon', 'sub_category'}
if not required_columns.issubset(df.columns):
    st.error(f"CSV file is missing required columns: {required_columns}")
    st.stop()

# Add slight noise to prevent overlapping points
noise = np.random.normal(0, 0.0001, df.shape[0])
df['lon'] = df['lon'] + noise
df['lat'] = df['lat'] + noise

# Dropdown filter for sub_category
sub_categories = df['sub_category'].unique()
selected_sub_category = st.selectbox("Select Complaint Sub-Category", sub_categories)

# Filter data
filtered_df = df[df['sub_category'] == selected_sub_category]

# Display scatter map
st.map(filtered_df)

