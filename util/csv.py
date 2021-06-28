# importing package to handle encodes
import base64

# importing package to handle datasets
import pandas as pd


# function to read uploaded file
# Return:
#   dataset
def read_csv(uploaded_file):
    return pd.read_csv(uploaded_file)

# function to download dataset as csv file
# Return:
#   link to download file
def csv_download(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="model_performance.csv">Download CSV File</a>'
    return href