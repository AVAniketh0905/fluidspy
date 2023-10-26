from typing import Callable
from typing import List
from typing import Optional

from .orders_caller import Order


class SecondOrder(Order):
    """
    The SecondOrder class is a callable class that implements the second-order Taylor approximation of a function.

    Args:
        direction (DIRECTION): The direction of the Taylor approximation.
        dim (DIM): The dimension of the function.
    """

    def one_dim(self, f: Callable, vector: float, step: float) -> float:
        x, h = vector, step
        if self.direction == "forward":
            return (f(x + 2 * h) - 2 * f(x + h) + f(x)) / (h**2)
        elif self.direction == "backward":
            return (f(x) - 2 * f(x - h) + f(x - 2 * h)) / (h**2)
        elif self.direction == "central":
            return (f(x + h) - 2 * f(x) + f(x - h)) / (h**2)
        else:
            raise ValueError("Invalid direction!")

    def two_dim(
        self, f: Callable, vector: List, step: List, axis: Optional[int]
    ) -> float:
        if not step[axis]:
            raise ValueError(
                f"Invalid axis! The axis values shoulde be less than {len(vector)}."
            )

        if self.direction == "forward":
            return (
                f(vector[0] + 2 * step[0], vector[1] + 2 * step[1])
                - 2 * f(vector[0] + step[0], vector[1] + step[1])
                + f(vector[0], vector[1])
            ) / (step[axis] ** 2)
        elif self.direction == "backward":
            return (
                f(vector[0], vector[1])
                - 2 * f(vector[0] - step[0], vector[1] - step[1])
                + f(vector[0] - 2 * step[0], vector[1] - 2 * step[1])
            ) / (step[axis] ** 2)
        elif self.direction == "central":
            return (
                f(vector[0] + step[0], vector[1] + step[1])
                - 2 * f(vector[0], vector[1])
                + f(vector[0] - step[0], vector[1] - step[1])
            ) / (step[axis] ** 2)
        else:
            raise ValueError("Invalid direction!")
