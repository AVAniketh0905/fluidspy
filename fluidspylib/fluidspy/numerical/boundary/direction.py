from abc import ABC
from abc import abstractmethod

import numpy as np

from ..state import SimulationState
from .conditions import BoundaryCondition


class Direction(ABC):
    """Abstract class for directions."""

    initial_value: float = None
    boundary_condition: BoundaryCondition = None

    def __init__(
        self,
        initial_value: float,
        state: SimulationState,
        boundary_condition: BoundaryCondition,
    ):
        self.axis = 0 if state.get_dimension() == 1 else 1
        self.initial_value = initial_value

        self.state = state
        self.boundary_condition = boundary_condition

    @abstractmethod
    def get_cells(self):
        """Get appropriate cells."""
        pass

    @abstractmethod
    def init_apply(self):
        """Apply initial boundary conditions."""
        pass

    def apply(self):
        """Apply boundary conditions."""
        pass


class Left(Direction):
    """Left direction."""

    def init_apply(self):
        """Apply boundary conditions."""
        cell_indices = self.get_cell_indices()

        new_state = self.state.get_state()
        np.put_along_axis(
            new_state,
            cell_indices,
            self.initial_value,
            axis=self.axis,
        )
        self.state.set_state(new_state)

    def get_cell_indices(self):
        if self.axis == 1:
            return np.array([[0] for _ in range(self.state.get_state().shape[0])])

        return np.array([0])

    def get_cells(self):
        left_cells = np.take(self.state.get_state(), 0, axis=self.axis)
        left_cells_indices = (
            0
            if self.axis != 1
            else np.array([[0] for _ in range(self.state.get_state().shape[0])])
        )
        adjacent_cells = np.take(self.state.get_state(), 1, axis=self.axis)

        return left_cells, left_cells_indices, adjacent_cells


class Right(Direction):
    """Right direction."""

    def init_apply(self):
        """Apply boundary conditions."""
        cell_indices = self.get_cell_indices()

        new_state = self.state.get_state()
        np.put_along_axis(
            new_state,
            cell_indices,
            self.initial_value,
            axis=self.axis,
        )
        self.state.set_state(new_state)

    def get_cell_indices(self):
        if self.axis == 1:
            return np.array([[-1] for _ in range(self.state.get_state().shape[0])])

        return np.array([-1])

    def get_cells(self):
        right_cells = np.take(self.state.get_state(), -1, axis=self.axis)
        right_cells_indices = (
            -1
            if self.axis != 1
            else np.array([[-1] for _ in range(self.state.get_state().shape[0])])
        )

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
        if self.state.get_dimension() == 1:
            raise ValueError("Top direction is not available for 1D.")

    def init_apply(self):
        """Apply boundary conditions."""
        cell_indices = self.get_cell_indices()

        new_state = self.state.get_state()
        np.put_along_axis(
            new_state,
            cell_indices,
            self.initial_value,
            axis=0,
        )
        self.state.set_state(new_state)

    def get_cell_indices(self):
        return np.array([[0 for _ in range(self.state.get_state().shape[1])]])

    def get_cells(self):
        top_cells = np.take(self.state.get_state(), 0, axis=0)
        top_cells_indices = np.array(
            [[0 for _ in range(self.state.get_state().shape[1])]]
        )

        adjacent_cells = np.take(self.state.get_state(), 1, axis=0)
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
        if self.state.get_dimension() == 1:
            raise ValueError("Bottom direction is not available for 1D.")

    def init_apply(self):
        """Apply boundary conditions."""
        cell_indices = self.get_cell_indices()

        new_state = self.state.get_state()
        np.put_along_axis(
            new_state,
            cell_indices,
            self.initial_value,
            axis=0,
        )
        self.state.set_state(new_state)

    def get_cell_indices(self):
        return np.array([[-1 for _ in range(self.state.get_state().shape[1])]])

    def get_cells(self):
        bottom_cells = np.take(self.state.get_state(), -1, axis=0)
        bottom_cells_indices = np.array(
            [[-1 for _ in range(self.state.get_state().shape[1])]]
        )

        adjacent_cells = np.take(self.state.get_state(), -2, axis=0)
        return bottom_cells, bottom_cells_indices, adjacent_cells
