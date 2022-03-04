# Import Modules
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import seaborn as sns

# @st.cache(suppress_st_warning = True)
def app(df):
	# Plots for data
    st.subheader("Visualise Data")
    st.title("Visualisation Selector")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    features_list = st.multiselect("Select the x-axis values:", 
                                            (df.describe().columns))
    # Create scatter plots.
    for feature in features_list:
        st.subheader(f"Scatter plot between {feature} and price")
        plt.figure(figsize = (12, 6))
        sns.scatterplot(x = feature, y = 'income', data = df)
        st.pyplot()
    plots = st.multiselect("Select the Charts/Plots", ("Count Plot", "Box Plot", "Pie Chart"))
    if 'Pie Chart' in plots:
        pie_chart = st.multiselect("Select columns for pie chart", ('income', 'gender'))
        plt.figure(figsize = (17, 6))
        for i in pie_chart:
            dict1 = {}
            for j in range(len(df[i].value_counts().index)):
                dict1[df[i].value_counts().index[j]] = j
            st.write(f'Pie chart for {i}')
            plt.pie(df[i].map(dict1).value_counts(), autopct = '%.1f%%', explode = np.linspace(0.1, .00, len(df[i].value_counts())), labels = df[i].value_counts().index)
            st.pyplot()
            st.write(np.linspace(0.1, .10, len(df[i].value_counts())))
    elif 'Count Plot' in plots:
        plt.figure(figsize=(17, 6))
        sns.countplot('workclass', data = df, hue = 'income')
        st.pyplot()
    elif 'Box Plot' in plots:
        # Get input from user for columns needs to plot in box plot
        st.subheader("Box plot")
        box_plot = st.multiselect("Select columns for box plot", ('income', 'gender'))
        plt.figure(figsize = (17, 6))
        for i in box_plot:
            st.write(f'Box plot for {i}')
            sns.boxplot(x = df['hours-per-week'], y = df[i])
            st.pyplot()
