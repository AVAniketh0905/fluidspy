from abc import ABC
from abc import abstractmethod
from typing import List

import numpy as np


class Dimension(ABC):
    """Abstract class for dimensions."""

    @abstractmethod
    def validate(self, initial_conditions):
        """Validate initial conditions."""
        pass

    @abstractmethod
    def create_grid(self):
        pass


class OneDimSpatial(Dimension):
    """One dimensional spatial dimension.

    Args:
        initial_conditions (List[float]): Initial conditions for the simulation.
    """

    initial_conditions: List[float]

    def __init__(self, initial_conditions: List[float]):
        if not self.validate(initial_conditions):
            raise ValueError("Invalid initial conditions for 1D spatial dimension")
        self.initial_conditions = initial_conditions

    def validate(self, initial_conditions: List[float]):
        return len(initial_conditions) == 1

    def create_grid(self, n: int, length: float):
        """Create a grid of n points with length L.

        Args:
            n (int): Number of points.
            length (float): Length of the grid.

        Returns:
            np.ndarray: Grid of n points with length L. (1D)
        """
        grid = np.linspace(0, length, n)
        self.initial_conditions = grid


class TwoDimSpatial(Dimension):
    """Two dimensional spatial dimension.

    Args:
        initial_conditions (List[List[float]]): Initial conditions for the simulation.
    """

    initial_conditions: List[List[float]]

    def __init__(self, initial_conditions: List[List[float]]):
        if not self.validate(initial_conditions):
            raise ValueError("Invalid initial conditions for 2D spatial dimension")
        self.initial_conditions = initial_conditions

    def validate(self, initial_conditions: List[List[float]]):
        return len(initial_conditions) == 2

    def create_grid(self, length, num_points_x, num_points_y):
        """Create a grid of n_x * n_y points with length L.

        Args:
            length (float): Length of the grid.
            num_points_x (int): Number of points in x direction.
            num_points_y (int): Number of points in y direction.

        Returns:
            np.ndarray: Grid of n_x * n_y points with length L. (2D)
        """
        grid_x, grid_y = np.meshgrid(
            np.linspace(0, length, num_points_x),
            np.linspace(0, length, num_points_y),
        )
        self.initial_conditions = grid_y if num_points_y > num_points_x else grid_x
