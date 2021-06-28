# importing streamlit to handle web pages
import streamlit as st

# importing Dto of results obtained by ml model
from dto.results_data import ResultsDataDto

# importing function that plots chart
from web_interface.results_chart import plot

# importing csv download function
from util.csv import csv_download

# function that presents initial results
def create_initial_results(df_head, y_name: str):
	st.write(df_head)
	st.markdown('A model is being built to predict the following **Y** variable:')
	st.info(y_name)

# function that present full results to user
# Parameters:
# 	ResultsDataDto with results obtained by model
def create_results(results_data: ResultsDataDto):
	
	st.subheader('Model Performance')

	st.write('Coefficient of determination ($R^2$):')
	st.info(results_data.r2_score)

	st.write('Error (MSE or MAE):')
	st.info(results_data.mean_error)

	st.write("The best parameters are %s with a score of %0.2f"
		% (results_data.grid_best_params, results_data.grid_best_score))

	st.subheader('Model Parameters')
	st.write(results_data.grid_params)

	st.subheader('Model Parameters')
	st.write(results_data.grid_results)

	fig = plot(results_data.plot_x, results_data.plot_y, results_data.plot_z)
	st.plotly_chart(fig)

	st.markdown(csv_download(results_data.grid_results), unsafe_allow_html=True)