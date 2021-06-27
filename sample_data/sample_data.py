import pandas as pd
from sklearn.datasets import load_diabetes

def get_diabetes_data():
    diabetes = load_diabetes()
    X = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
    Y = pd.Series(diabetes.target, name='response')
    df = pd.concat([X,Y], axis=1)

    return df