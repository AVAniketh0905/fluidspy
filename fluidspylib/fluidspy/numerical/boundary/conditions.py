from abc import ABC
from abc import abstractmethod

import numpy as np


class BoundaryCondition(ABC):
    """Abstract class for boundary conditions."""

    @abstractmethod
    def apply(
        self, initial_value: float, state: np.ndarray, adjacent_states: np.ndarray
    ):
        """Apply boundary conditions."""
        pass


class Constant(BoundaryCondition):
    """Constant boundary condition."""

    def apply(
        self, initial_value: float, state: np.ndarray, adjacent_states: np.ndarray
    ):
        state = list(map(lambda x: initial_value, state))


class Insulated(BoundaryCondition):
    """Insulated boundary condition."""

    def apply(
        self, initial_value: float, state: np.ndarray, adjacent_states: np.ndarray
    ):
        for i in range(len(state)):
            state[i] = adjacent_states[i]
