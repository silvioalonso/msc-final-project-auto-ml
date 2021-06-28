# Dto to pass input parameters set by the user
class InputParametersDto:
    def __init__(
        self, 
        split_size, 
        parameter_n_estimators,
        parameter_n_estimators_step,
        parameter_max_features,
        parameter_min_samples_split,
        parameter_min_samples_leaf,
        parameter_random_state,
        parameter_criterion,
        parameter_bootstrap,
        parameter_oob_score,
        parameter_n_jobs):

        self.split_size = split_size
        self.parameter_n_estimators = parameter_n_estimators
        self.parameter_n_estimators_step = parameter_n_estimators_step
        self.parameter_max_features = parameter_max_features
        self.parameter_min_samples_split = parameter_min_samples_split
        self.parameter_min_samples_leaf = parameter_min_samples_leaf
        self.parameter_random_state = parameter_random_state
        self.parameter_criterion = parameter_criterion
        self.parameter_bootstrap = parameter_bootstrap
        self.parameter_oob_score = parameter_oob_score
        self.parameter_n_jobs = parameter_n_jobs