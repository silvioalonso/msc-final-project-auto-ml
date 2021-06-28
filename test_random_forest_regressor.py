import pytest

from ml_model.random_forest_regressor import build_model

def test_raises_exception_on_no_arguments():
    with pytest.raises(TypeError):
        build_model()