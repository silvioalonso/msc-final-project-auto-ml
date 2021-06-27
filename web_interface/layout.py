import streamlit as st

def create_layout():
    #---------------------------------#
    st.write("""
    # The Machine Learning Hyperparameter Optimization App
    **(Regression Edition)**

    In this implementation, the *RandomForestRegressor()* function is used in this app for build a regression model using the **Random Forest** algorithm.

    """)

    # Displays the dataset
    st.subheader('Dataset')