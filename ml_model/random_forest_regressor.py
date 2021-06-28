# importing packages to handle math analysis
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import GridSearchCV

# importing Dto used as function return
from dto.results_data import ResultsDataDto



# function that handles the predictive analysis using Random Forest Regression algorithm
# Parameters:
#	df - dataset
# 	inp - input parameters of type InputParametersDto set by user
# Return:
# 	ResultsDataDto - results obtained by model
def build_model(df, inp) -> ResultsDataDto:
	n_estimators_range = np.arange(inp.parameter_n_estimators[0], inp.parameter_n_estimators[1]+inp.parameter_n_estimators_step, inp.parameter_n_estimators_step)
	max_features_range = np.arange(inp.parameter_max_features[0], inp.parameter_max_features[1]+1, 1)
	param_grid = dict(max_features=max_features_range, n_estimators=n_estimators_range)

	X = df.iloc[:,:-1] # using all column except for the last column as X
	Y = df.iloc[:,-1] # selecting the last column as Y

	# data splitting
	X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=inp.split_size)

	rf = RandomForestRegressor(
		n_estimators=inp.parameter_n_estimators,
		random_state=inp.parameter_random_state,
		max_features=inp.parameter_max_features,
		criterion=inp.parameter_criterion,
		min_samples_split=inp.parameter_min_samples_split,
		min_samples_leaf=inp.parameter_min_samples_leaf,
		bootstrap=inp.parameter_bootstrap,
		oob_score=inp.parameter_oob_score,
		n_jobs=inp.parameter_n_jobs)

	grid = GridSearchCV(estimator=rf, param_grid=param_grid, cv=5)
	grid.fit(X_train, Y_train)

	Y_pred_test = grid.predict(X_test)
	r2_score_ = r2_score(Y_test, Y_pred_test)

	mean_error = mean_squared_error(Y_test, Y_pred_test)

	# process grid data
	grid_results = pd.concat([pd.DataFrame(grid.cv_results_["params"]),pd.DataFrame(grid.cv_results_["mean_test_score"], columns=["R2"])],axis=1)

	# segment data into groups based on the 2 hyperparameters
	grid_contour = grid_results.groupby(['max_features','n_estimators']).mean()
	# pivoting the data
	grid_reset = grid_contour.reset_index()
	grid_reset.columns = ['max_features', 'n_estimators', 'R2']
	grid_pivot = grid_reset.pivot('max_features', 'n_estimators')
	x = grid_pivot.columns.levels[1].values
	y = grid_pivot.index.values
	z = grid_pivot.values

	return ResultsDataDto(
		r2_score_, 
		mean_error, 
		grid.best_params_, 
		grid.best_score_,
		grid.get_params(),
		grid_results,
		x,
		y,
		z)