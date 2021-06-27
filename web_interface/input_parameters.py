import streamlit as st
from dto.input_parameters import InputParametersDto

def create_input_parameters() -> InputParametersDto:
    # Sidebar - Specify parameter settings
    st.sidebar.header('Set Parameters')
    split_size = st.sidebar.slider('Data split ratio (% for Training Set)', 10, 90, 80, 5)

    st.sidebar.subheader('Learning Parameters')
    parameter_n_estimators = st.sidebar.slider('Number of estimators (n_estimators)', 0, 500, (10,50), 50)
    parameter_n_estimators_step = st.sidebar.number_input('Step size for n_estimators', 10)
    st.sidebar.write('---')
    parameter_max_features = st.sidebar.slider('Max features (max_features)', 1, 50, (1,3), 1)
    st.sidebar.number_input('Step size for max_features', 1)
    st.sidebar.write('---')
    parameter_min_samples_split = st.sidebar.slider('Minimum number of samples required to split an internal node (min_samples_split)', 1, 10, 2, 1)
    parameter_min_samples_leaf = st.sidebar.slider('Minimum number of samples required to be at a leaf node (min_samples_leaf)', 1, 10, 2, 1)

    st.sidebar.subheader('General Parameters')
    parameter_random_state = st.sidebar.slider('Seed number (random_state)', 0, 1000, 42, 1)
    parameter_criterion = st.sidebar.select_slider('Performance measure (criterion)', options=['mse', 'mae'])
    parameter_bootstrap = st.sidebar.select_slider('Bootstrap samples when building trees (bootstrap)', options=[True, False])
    parameter_oob_score = st.sidebar.select_slider('Whether to use out-of-bag samples to estimate the R^2 on unseen data (oob_score)', options=[False, True])
    parameter_n_jobs = st.sidebar.select_slider('Number of jobs to run in parallel (n_jobs)', options=[1, -1])


    return InputParametersDto(
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
        parameter_n_jobs)