# importing streamlit to handle web pages
import streamlit as st


# creates warning that no file has been uploaded
def create_awaiting_file():
    st.info('Awaiting for CSV file to be uploaded.')

# creates button to activate sample dataset
# Return:
#   True when button is pressed
def call_sample_data():
    return st.button('Press to use Example Dataset')