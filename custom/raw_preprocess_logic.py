import numpy as np


def sampling_by_each_class(
    X: np.ndarray, y: np.ndarray, n_samples: int, labels: list[int]
) -> tuple[np.ndarray, np.ndarray]:

    y = np.array([int(label) for label in y])
    indices = np.where(np.isin(y, labels))[0]
    X, y = X[indices][:n_samples], y[indices][:n_samples]

    return X, y
