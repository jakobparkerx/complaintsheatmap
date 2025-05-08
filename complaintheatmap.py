import streamlit as st
import pandas as pd

# Try to load the default CSV file
default_file = "postcode_coordinates.csv"

df = None

if st.button("Load default CSV"):
    try:
        df = pd.read_csv(default_file)
        st.success(f"Loaded default CSV: {default_file}")
    except FileNotFoundError:
        st.warning(f"Default CSV not found at {default_file}")

# Allow user to upload their own CSV file
uploaded_file = st.file_uploader("Or upload your CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("Uploaded CSV file successfully!")

# Display the dataframe if loaded
if df is not None:
    st.write("Preview of the data:")
    st.dataframe(df)


