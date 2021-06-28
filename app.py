
# __author__ = "Silvio Alonso"
# __contact__ = "silvioalonsomarques@gmail.com"
# __date__ = "2021/06/25"
# __version__ = "1.3.0"


# importing web_interface functions that create the web app components
from web_interface.conf import config_page
from web_interface.header import create_header
from web_interface.input_dataset import create_input_dataset
from web_interface.input_parameters import create_input_parameters
from web_interface.results import create_initial_results, create_results
from web_interface.request_sample_dataset import create_awaiting_file, call_sample_data

# importing ml_model function
# currently the random forest regressor is the implemented algorithm
from ml_model.random_forest_regressor import build_model

# importing helpers to handle the dataset
from util.dataset import get_y_name, get_dataset_head

# importing helpers to handle the csv imported by the user
from util.csv import read_csv

# importing module to get sample data (diabetes dataset) to be used as an example
from sample_data.sample_data import get_diabetes_data



# setting web app configuration and setting layout properties
config_page()
create_header()

# creates file input component and saves uploaded file to variable
uploaded_file = create_input_dataset()

# creates parameters input components and saves InputParametersDto return to variable
input_parameters = create_input_parameters()

# call methods that display results
def get_results(df):
	create_initial_results(get_dataset_head(df), get_y_name(df))
	create_results(build_model(df, input_parameters))


if uploaded_file is not None: # action when user uploads a dataset
	df = read_csv(uploaded_file)
	get_results(df)
else: 
	create_awaiting_file() # creates awaiting file warning
	if call_sample_data(): # action when user chooses to use sample dataset
		df = get_diabetes_data()
		get_results(df)