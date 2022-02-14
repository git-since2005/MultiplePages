# Open Sublime text editor, create a new Python file, copy the following code in it and save it as 'census_main.py'.

# Import modules
import numpy as np
import pandas as pd
import streamlit as st

# Import mutliple pages
import home
import data
import plots
import predict

st.set_page_config(page_title = 'Car Price Prediction',
					page_icon = ':car:',
					layout = 'centered',
					initial_sidebar_state = 'auto')

@st.cache()
def load_data():
	# Load the Adult Income dataset into DataFrame.

	df = pd.read_csv('adult (1).csv', header=None)
	df.head()

	# Rename the column names in the DataFrame using the list given above. 

	# Create the list
	column_name =['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 
               'relationship', 'race','gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']

	# Rename the columns using 'rename()'
	for i in range(df.shape[1]):
	  df.rename(columns={i:column_name[i]},inplace=True)

	# Print the first five rows of the DataFrame
	df.head()

	# Replace the invalid values ' ?' with 'np.nan'.

	df['native-country'] = df['native-country'].replace(' ?',np.nan)
	df['workclass'] = df['workclass'].replace(' ?',np.nan)
	df['occupation'] = df['occupation'].replace(' ?',np.nan)

	# Delete the rows with invalid values and the column not required 

	# Delete the rows with the 'dropna()' function
	df.dropna(inplace=True)

	# Delete the column with the 'drop()' function
	df.drop(columns='fnlwgt',axis=1,inplace=True)

	return df

census_df = load_data()

# Start designing the app
# Add navigation bar
st.sidebar.title("Navigate")
pages_dict = {'Home': home,
			'Data': data,
			'Plots': plots,
			'Predict': predict}
user_choice = st.sidebar.radio("Go to", ('Home', 'Data', 'Plots', 'Predict'))
if user_choice == 'Home':
	home.app()
elif user_choice == 'Data':
	data.app(census_df)
else:
	selected_page = pages_dict[user_choice]
