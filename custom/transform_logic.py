from typing import Optional

import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


def dimension_reduction_by_pca(
    X_train: np.ndarray,
    y_train: np.ndarray,
    X_val: Optional[np.ndarray],
    y_val: Optional[np.ndarray],
    X_test: np.ndarray,
    y_test: np.ndarray,
    n_components: int,
) -> tuple[np.ndarray, np.ndarray, Optional[np.ndarray], Optional[np.ndarray], np.ndarray, np.ndarray]:
    scaler = StandardScaler()
    scaler.fit(X_train)
    X_train_scaled = scaler.transform(X_train)
    X_val_scaled = scaler.transform(X_val) if X_val is not None else None
    X_test_scaled = scaler.transform(X_test)

    pca = PCA(n_components=n_components)
    pca.fit(X_train_scaled)
    X_train_pca = pca.transform(X_train_scaled)
    X_val_pca = pca.transform(X_val_scaled) if X_val_scaled is not None else None
    X_test_pca = pca.transform(X_test_scaled)

    return X_train_pca, y_train, X_val_pca, y_val, X_test_pca, y_test
