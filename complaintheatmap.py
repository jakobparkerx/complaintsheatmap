import streamlit as st
import pandas as pd
import numpy as np
import os

# Set the default file path
default_file_path = "complaintheatmap/postcode_coordinates.csv"

# Function to dynamically resolve the file path
def get_csv_file_path():
    # Check if the file exists at the default path
    if os.path.exists(default_file_path):
        return default_file_path
    else:
        # Display a message to upload the file if not found
        st.warning("Default CSV file not found. Please upload the CSV file.")
        uploaded_file = st.file_uploader("Upload your CSV file", type="csv")
        if uploaded_file:
            return uploaded_file
        else:
            return None

# Load the CSV file with error handling
file_path = get_csv_file_path()
if file_path is None:
    st.error("No CSV file provided. Please upload a valid file.")
    st.stop()

try:
    if isinstance(file_path, str):
        df = pd.read_csv(file_path)
    else:
        df = pd.read_csv(file_path)  # For uploaded files
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
