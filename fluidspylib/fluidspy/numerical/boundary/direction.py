from abc import ABC
from abc import abstractmethod

import numpy as np

from ..state import SimulationState
from .conditions import BoundaryCondition


class Direction(ABC):
    """Abstract class for directions."""

    axis: int = None
    initial_value: float = None
    state: SimulationState = None
    boundary_condition: BoundaryCondition = None

    def __init__(
        self,
        initial_value: float,
        state: SimulationState,
        boundary_condition: BoundaryCondition,
    ):
        self.initial_value = initial_value

        self.state = state
        self.boundary_condition = boundary_condition

    @abstractmethod
    def get_cells(self):
        """Get appropriate cells."""
        pass

    def put_along_direction(
        self,
        cell_indices: np.ndarray,
        new_cells: np.ndarray,
    ):
        new_state = self.state.get_state()
        np.put_along_axis(
            new_state,
            cell_indices,
            new_cells,
            axis=self.axis,
        )
        self.state.set_state(new_state)

    def init_apply(self):
        """Apply boundary conditions."""
        cell_indices = self.get_cell_indices()
        self.put_along_direction(cell_indices, self.initial_value)

    def apply(self):
        """Apply boundary conditions."""
        cells, cell_indices, adjacent_cells = self.get_cells()
        # print(
        #     "cells, cell_indices, adjacent_cells", cells, cell_indices, adjacent_cells
        # )
        new_cells = self.boundary_condition.apply(
            self.initial_value, cells, adjacent_cells
        )
        # print("new_cells", new_cells)
        self.put_along_direction(cell_indices, new_cells)


class Left(Direction):
    """Left direction."""

    def __init__(
        self,
        initial_value: float,
        state: SimulationState,
        boundary_condition: BoundaryCondition,
    ):
        super().__init__(initial_value, state, boundary_condition)
        self.axis = 0 if state.get_dimension() == 1 else 1

    def get_cell_indices(self):
        if self.axis == 1:
            return np.array([[0] for _ in range(self.state.get_state().shape[0])])

        return np.array([0])

    def get_cells(self):
        left_cells = np.take(self.state.get_state(), 0, axis=self.axis)
        left_cells_indices = self.get_cell_indices()
        adjacent_cells = np.take(self.state.get_state(), 1, axis=self.axis)

        return left_cells, left_cells_indices, adjacent_cells


class Right(Direction):
    """Right direction."""

    def __init__(
        self,
        initial_value: float,
        state: SimulationState,
        boundary_condition: BoundaryCondition,
    ):
        super().__init__(initial_value, state, boundary_condition)
        self.axis = 0 if state.get_dimension() == 1 else 1

    def get_cell_indices(self):
        if self.axis == 1:
            return np.array([[-1] for _ in range(self.state.get_state().shape[0])])

        return np.array([-1])

    def get_cells(self):
        right_cells = np.take(self.state.get_state(), -1, axis=self.axis)
        right_cells_indices = self.get_cell_indices()
        adjacent_cells = np.take(self.state.get_state(), -2, axis=self.axis)
        return right_cells, right_cells_indices, adjacent_cells


class Top(Direction):
    """Top direction."""

    def __init__(
        self,
        initial_value: float,
        state: SimulationState,
        boundary_condition: BoundaryCondition,
    ):
        super().__init__(initial_value, state, boundary_condition)
        self.axis = 0

        if self.state.get_dimension() == 1:
            raise ValueError("Top direction is not available for 1D.")

    def get_cell_indices(self):
        return np.array([[0 for _ in range(self.state.get_state().shape[1])]])

    def get_cells(self):
        top_cells = np.take(self.state.get_state(), 0, axis=self.axis)
        top_cells_indices = self.get_cell_indices()
        adjacent_cells = np.take(self.state.get_state(), 1, axis=self.axis)
        return top_cells, top_cells_indices, adjacent_cells


class Bottom(Direction):
    """Bottom direction."""

    def __init__(
        self,
        initial_value: float,
        state: SimulationState,
        boundary_condition: BoundaryCondition,
    ):
        super().__init__(initial_value, state, boundary_condition)
        self.axis = 0

        if self.state.get_dimension() == 1:
            raise ValueError("Bottom direction is not available for 1D.")

    def get_cell_indices(self):
        return np.array([[-1 for _ in range(self.state.get_state().shape[1])]])

    def get_cells(self):
        bottom_cells = np.take(self.state.get_state(), -1, axis=self.axis)
        bottom_cells_indices = self.get_cell_indices()
        adjacent_cells = np.take(self.state.get_state(), -2, axis=self.axis)
        return bottom_cells, bottom_cells_indices, adjacent_cells
