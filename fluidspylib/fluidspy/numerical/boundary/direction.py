from abc import ABC
from abc import abstractmethod

import numpy as np

from ..dim.dimension import Dimension
from .conditions import BoundaryCondition


class Direction(ABC):
    """Abstract class for directions."""

    initial_value: float = None
    axis: int
    boundary_condition: BoundaryCondition = None

    def __init__(
        self,
        dim: Dimension,
        initial_value: float,
        boundary_condition: BoundaryCondition,
    ):
        self.axis = 0 if dim.get_dimension() == 1 else 1
        self.initial_value = initial_value
        self.boundary_condition = boundary_condition

    @abstractmethod
    def get_cells(self, state: np.ndarray):
        """Get appropriate cells."""
        pass

    def apply(self, state: np.ndarray):
        """Apply boundary conditions."""
        curr_cells, adjacent_cells = self.get_cells(state)
        self.boundary_condition.apply(self.initial_value, curr_cells, adjacent_cells)


class Left(Direction):
    """Left direction."""

    def get_cells(self, state: np.ndarray):
        left_cells = np.take(state, 0, axis=self.axis)
        adjacent_cells = np.take(state, 1, axis=self.axis)
        return left_cells, adjacent_cells


class Right(Direction):
    """Right direction."""

    def get_cells(self, state: np.ndarray):
        right_cells = np.take(state, -1, axis=self.axis)
        adjacent_cells = np.take(state, -2, axis=self.axis)
        return right_cells, adjacent_cells


class Top(Direction):
    """Top direction."""

    def __init__(
        self,
        dim: Dimension,
        initial_value: float,
        boundary_condition: BoundaryCondition,
    ):
        super().__init__(dim, initial_value, boundary_condition)
        if dim.get_dimension() == 1:
            raise ValueError("Top direction is not available for 1D.")

    def get_cells(self, state: np.ndarray):
        top_cells = np.take(state, 0, axis=0)
        adjacent_cells = np.take(state, 1, axis=0)
        return top_cells, adjacent_cells


class Bottom(Direction):
    """Bottom direction."""

    def __init__(
        self,
        dim: Dimension,
        initial_value: float,
        boundary_condition: BoundaryCondition,
    ):
        super().__init__(dim, initial_value, boundary_condition)
        if dim.get_dimension() == 1:
            raise ValueError("Bottom direction is not available for 1D.")

    def get_cells(self, state: np.ndarray):
        bottom_cells = np.take(state, -1, axis=0)
        adjacent_cells = np.take(state, -2, axis=0)
        return bottom_cells, adjacent_cells
