from abc import ABC
from abc import abstractmethod

import numpy as np


class BoundaryCondition(ABC):
    """Abstract class for boundary conditions."""

    def init_apply(self, initial_value: float, state: np.ndarray):
        """Apply boundary conditions."""
        if isinstance(initial_value, float):
            state = initial_value
        else:
            state = np.full_like(state, initial_value, dtype=np.float64)

        return state

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
        super().init_apply(initial_value, state)
        return state


class Insulated(BoundaryCondition):
    """Insulated boundary condition."""

    def apply(
        self, initial_value: float, state: np.ndarray, adjacent_states: np.ndarray
    ):
        state = np.copy(adjacent_states)

        return state
