import pytest
import numpy as np
# TODO: add necessary import
from sklearn.ensemble import RandomForestClassifier

from ml.data import apply_label
from ml.model import compute_model_metrics, inference, train_model


# TODO: implement the first test. Change the function name and input as needed
def test_apply_labels():
    """
    Check that apply_label returns the expected string for binary labels (0 -> <=50K, 1 -> >50K).
    """
    assert apply_label(np.array([0])) == "<=50K"
    assert apply_label(np.array([1])) == ">50K"


# TODO: implement the second test. Change the function name and input as needed
def test_train_model():
    """
    Check that train_model returns a RandomForestClassifier fit on the training data.
    """
    X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [10, 11]])
    y = np.array([0, 1, 0, 1, 0])
    model = train_model(X, y)
    assert isinstance(model, RandomForestClassifier)
    assert hasattr(model, "predict")
    preds = model.predict(X)
    assert len(preds) == len(y)


# TODO: implement the third test. Change the function name and input as needed
def test_compute_model_metrics():
    """
    Check that compute_model_metrics returns three floats (precision, recall, fbeta) in [0, 1].
    """
    y = np.array([0, 1, 1, 0])
    preds = np.array([0, 1, 0, 0])
    precision, recall, fbeta = compute_model_metrics(y, preds)
    assert isinstance(precision, float) and 0 <= precision <= 1
    assert isinstance(recall, float) and 0 <= recall <= 1
    assert isinstance(fbeta, float) and 0 <= fbeta <= 1

# souces used:
# https://docs.pytest.org/en/stable/example/simple.html
# https://docs.python.org/3/library/unittest.html