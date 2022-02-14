# Import modules
import pandas as pd 
import numpy as np
import streamlit as st

# Define a function for info for the dataset
def app(df):
    st.header("View data")
    with st.expander("View data"):
        st.table(df)
    st.subheader("Columns Description:")
    beta_col1, beta_col2, beta_col3 = st.columns(3)
    with beta_col1:
        if st.checkbox("Show all column names"):
            st.table(list(df.columns))
    with beta_col2:
        if st.checkbox("View column data"):
            column_data = st.selectbox("Select column", tuple(df.columns))
            st.write(df[column_data])
    with beta_col3:
        if st.checkbox("View column data types"):
            col_names = st.selectbox('Select column', df.columns)
            st.write(f"Name: {col_names} \nData type: {df[col_names].dtype}")
    if st.checkbox("Show Summary"):
        st.table(df.describe())