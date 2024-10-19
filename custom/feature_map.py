import numpy as np
import pennylane as qml
from qxmt.feature_maps import BaseFeatureMap


class CustomFeatureMap(BaseFeatureMap):
    def __init__(self, n_qubits: int, reps: int) -> None:
        super().__init__("pennylane", n_qubits)
        self.reps: int = reps

    def feature_map(self, x: np.ndarray) -> None:
        for _ in range(self.reps):
            for i in range(self.n_qubits):
                qml.Hadamard(wires=i)
                qml.RZ(x[i], wires=i)
            for i in range(0, self.n_qubits - 1):
                qml.IsingZZ(2 * (np.pi - x[i]) * (np.pi - x[i + 1]), wires=[i, i + 1])

        for _ in range(self.reps):
            for i in range(self.n_qubits):
                qml.RX(x[i], wires=i)
            for i in range(0, self.n_qubits - 1):
                qml.IsingXX(2 * (np.pi - x[i]) * (np.pi - x[i + 1]), wires=[i, i + 1])
