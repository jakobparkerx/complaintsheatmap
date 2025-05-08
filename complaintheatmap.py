import streamlit as st
import pandas as pd
import numpy as np

# Load the CSV file with error handling
try:
    df = pd.read_csv("complaintheatmap/postcode_coordinates.csv")
except FileNotFoundError:
    st.error("CSV file not found. Please ensure the file path is correct.")
    st.stop()
except pd.errors.EmptyDataError:
    st.error("CSV file is empty. Please provide a valid file.")
    st.stop()
except Exception as e:
    st.error(f"An unexpected error occurred: {e}")
    st.stop()

# Validate that the required columns exist
required_columns = {'postcode', 'lat', 'lon', 'sub_category'}
if not required_columns.issubset(df.columns):
    st.error(f"CSV file is missing one or more required columns: {required_columns}")
    st.stop()

# Add noise to coordinates to avoid overlapping points
noise = np.random.normal(0, 0.0001, df.shape[0])  # Small random noise to add to coordinates
df['lon'] = df['lon'] + noise
df['lat'] = df['lat'] + noise

# Streamlit app
st.title("UK Postcode Complaints Heatmap")

# Add a dropdown to select the complaint sub-category
sub_categories = df['sub_category'].unique()
selected_sub_category = st.selectbox("Select Complaint Sub-Category", sub_categories)

# Filter the dataframe based on the selected sub-category
filtered_df = df[df['sub_category'] == selected_sub_category]

# Display the filtered map
st.map(filtered_df)
