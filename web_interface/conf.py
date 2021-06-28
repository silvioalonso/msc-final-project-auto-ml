# importing streamlit to handle web pages
import streamlit as st

# function to set web page configuration
def config_page():
	# page expands to full width
	st.set_page_config(page_title='The Machine Learning Hyperparameter Optimization App',
	layout='wide')