# importing streamlit to handle web pages
import streamlit as st


# creates header in main panel
def create_header():
    st.write("""
    # The Machine Learning Hyperparameter Optimization App
    **(Regression Edition)**

    In this implementation, the *RandomForestRegressor()* function is used in this app for build a regression model using the **Random Forest** algorithm.

    """)

    st.subheader('Dataset')