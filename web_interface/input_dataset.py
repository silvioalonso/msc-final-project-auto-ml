# importing streamlit to handle web pages
import streamlit as st

# function that creates component to upload file to be used as dataset
# and presents example input file to user
# Return:
#   uploaded file
def create_input_dataset():
    st.sidebar.header('Upload your CSV data')
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"]) 
    st.sidebar.markdown("""
    [Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv)
    """)

    return uploaded_file