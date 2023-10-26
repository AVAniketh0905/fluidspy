from typing import Callable
from typing import List
from typing import Optional

from ..constant import DIM
from ..constant import DIRECTION


class Order:
    """
    The Order class is a callable class that implements the Taylor approximation of a function.

    Args:
        direction (DIRECTION): The direction of the Taylor approximation.
        dim (DIM): The dimension of the function.
    """

    def __init__(self, direction: DIRECTION, dim: DIM) -> None:
        self.direction = direction
        self.dim = dim

    def __call__(
        self,
        f: Callable,
        vector: List | float,
        step: List | float,
        axis: Optional[int] = 0,
    ) -> None:
        """
        The __call__ method is a special method that is called when an instance of the class is called.

        Args:
            f (Callable): The function to be approximated.
            vector (List | float): The vector of the function.
            step (List | float): The step of the function.
            axis (Optional[int]): The axis of the function. Defaults to 0.
        """
        if self.dim == "one":
            if isinstance(vector, float) and isinstance(step, float):
                return self.one_dim(f, vector, step)
            raise ValueError("Invalid! `vector` or `step` values must be a float.")
        elif self.dim == "two":
            if isinstance(vector, list) and isinstance(step, list):
                return self.two_dim(f, vector, step, axis)
            raise ValueError("Invalid! `vector` or `step` values must be a list.")
        elif self.dim == "three":
            raise ValueError("Not implemented yet!")
        else:
            raise ValueError("Invalid dimension!")

    def __str__(self) -> str:
        return f"Calling from FirstOrder with {self.direction} difference with a function of {self.dim} dimension."
