import streamlit as st

def create_input_dataset():
    st.sidebar.header('Upload your CSV data')
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"]) 
    st.sidebar.markdown("""
    [Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv)
    """)

    return uploaded_file

# def uploaded_file():
#     return st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])