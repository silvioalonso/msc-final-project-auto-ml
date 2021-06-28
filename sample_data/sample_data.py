# importing package to handle datasets
import pandas as pd

# importing diabetes database
from sklearn.datasets import load_diabetes

# function that returns the diabetes sample dataset
# Return:
#   diabetes sample dataset
def get_diabetes_data():
    diabetes = load_diabetes()
    X = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
    Y = pd.Series(diabetes.target, name='response')
    df = pd.concat([X,Y], axis=1)

    return df