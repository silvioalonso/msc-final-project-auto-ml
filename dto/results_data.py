class ResultsDataDto:
	def __init__(
		self, 
		r2_score,
		mean_error,
		grid_best_params,
		grid_best_score,
		grid_params,
		grid_results,
		plot_x,
		plot_y,
		plot_z):

		self.r2_score = r2_score
		self.mean_error = mean_error
		self.grid_best_params = grid_best_params
		self.grid_best_score = grid_best_score
		self.grid_params = grid_params
		self.grid_results = grid_results
		self.plot_x = plot_x
		self.plot_y = plot_y
		self.plot_z = plot_z