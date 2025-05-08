import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title("UK Postcode Complaints Scatter Map")

# Try to load the default CSV file automatically
default_file = "postcode_coordinates.csv"
df = None

try:
    df = pd.read_csv(default_file)
except FileNotFoundError:
    st.warning(f"Default CSV not found at {default_file}. Please upload a CSV file.")

# Allow user to upload their own CSV file if default is missing
uploaded_file = st.file_uploader("Upload your CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

# If data loaded, validate columns and show map
if df is not None:
    required_columns = {'postcode', 'lat', 'lon', 'sub_category'}
    if required_columns.issubset(df.columns):
        # Add slight noise to prevent overlapping points
        noise = np.random.normal(0, 0.0001, df.shape[0])
        df['lon'] = df['lon'] + noise
        df['lat'] = df['lat'] + noise

        # Display scatter map
        st.map(df)

    else:
        st.error(f"CSV file is missing required columns: {required_columns}")


