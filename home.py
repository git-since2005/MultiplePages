import streamlit as st
import pandas as pd

def app(df):
	st.title("Census visualisation web app")
	st.write("This app allows a user to explore and visualise the census data")

	if st.checkbox("Show column names of dataset"):
		st.write(df.columns)
	elif st.checkbox("Show columns data-type"):
		col = st.selectbox('Select column', df.columns)
		st.write(f'{col}')
		st.write(f'Data-type:{df[col].dtype}')
	elif st.checkbox("Show column summary"):
		col1 = st.selectbox('Select column', df.describe().columns)
		st.write(f'Name: {col1}')
		st.write(f'Mean of {col1}: {df[col1].mean()}')
		st.write(f'Median of {col1}: {df[col1].median()}')
		st.write(f'Mode of {col1}: {df[col1].mode()}')
		st.write(f'Standard deviation of {col1}: {df[col1].std()}')
