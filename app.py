from web_interface.conf import config_page
from web_interface.layout import create_layout
from web_interface.input_dataset import create_input_dataset
from web_interface.input_parameters import create_input_parameters
from web_interface.results import create_initial_results, create_results
from web_interface.request_sample_dataset import create_sample_dataset, call_sample_data

from ml_model.random_forest_regressor import build_model

from util.dataset import get_y_name, get_dataset_head
from util.csv import read_csv

from sample_data.sample_data import get_diabetes_data

config_page()
create_layout()

uploaded_file = create_input_dataset()
input_parameters = create_input_parameters()


def get_results(df):
	create_initial_results(get_dataset_head(df), get_y_name(df))
	create_results(build_model(df, input_parameters))


if uploaded_file is not None:
	df = read_csv(uploaded_file)
	get_results(df)
else:
	create_sample_dataset()
	if call_sample_data():
		df = get_diabetes_data()
		get_results(df)


