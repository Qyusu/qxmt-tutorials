from typing import Any

import numpy as np
from qxmt.evaluation.metrics import BaseMetric
from sklearn.metrics import confusion_matrix


class CustomMetric(BaseMetric):
    def __init__(self) -> None:
        super().__init__("specificity")

    @staticmethod
    def evaluate(actual: np.ndarray, predicted: np.ndarray, **kwargs: Any) -> float:
        tn, fp, fn, tp = confusion_matrix(actual, predicted).ravel()
        return tn / (tn + fp)
