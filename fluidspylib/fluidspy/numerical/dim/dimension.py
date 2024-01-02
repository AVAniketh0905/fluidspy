from abc import ABC
from abc import abstractmethod
from typing import Any
from typing import List
from typing import Tuple
from typing import Union

import numpy as np


class Dimension(ABC):
    """Abstract class for dimensions."""

    initial_conditions: Any = None

    @abstractmethod
    def validate(self):
        """Validate initial conditions."""
        pass

    @abstractmethod
    def create_grid(
        self, num_points: Union[int, Tuple[int, int]], base_value: float = 0.0
    ):
        self.initial_conditions = np.zeros(num_points, dtype=float)
        self.initial_conditions.fill(base_value)


class OneDimSpatial(Dimension):
    """One dimensional spatial dimension.

    Args:
        initial_conditions (List[float]): Initial conditions for the simulation.
    """

    initial_conditions: List[float] = None

    @staticmethod
    def validate(initial_conditions: List[float]):
        return len(initial_conditions) == 1

    def create_grid(self, num_points: int, base_value: float = 0.0):
        """Create a grid of num_points points with base_value(or 0).

        Args:
            num_points (int): Number of points.
            base_value (float): Base value for the grid. Defaults to 0.0.

        Returns:
            np.ndarray: Grid of num_points points with base_value. (1D)
        """
        super().create_grid(num_points, base_value)


class TwoDimSpatial(Dimension):
    """Two dimensional spatial dimension.

    Args:
        initial_conditions (List[List[float]]): Initial conditions for the simulation.
    """

    initial_conditions: List[List[float]] = None

    @staticmethod
    def validate(initial_conditions: List[List[float]]):
        return len(initial_conditions) == 2

    def create_grid(self, num_points: Tuple[int, int], base_value: float = 0.0):
        """Create a grid of n_x * n_y points with base_value.

        Args:
            num_points (Tuple[int, int]): Number of points in each dimension.
            base_value (float): Base value for the grid. Defaults to 0.0.

        Returns:
            np.ndarray: Grid of n_x * n_y points with base_value. (2D)
        """
        super().create_grid(num_points, base_value)
