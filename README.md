# AutoML app

Machine Learning Hyperparameter Optimizer App (Streamlit + Scikit-learn + Python)

## Reproducing this web app
To recreate this web app on your own computer, do the following.

### Create conda environment
Firstly, we will create a conda environment called *automl*
```
conda create -n automl python=3.7.9
```
Secondly, we will login to the *automl* environement
```
conda activate mlopt
```

Pip install libraries
```
pip install -r requirements.txt
```

###  Launch the app

```
streamlit run app.py
```
