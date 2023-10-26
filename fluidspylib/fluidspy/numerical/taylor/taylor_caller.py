from typing import Callable

from ..constant import DIM
from ..constant import DIRECTION
from ..constant import ORDER
from ..orders.first_order import FirstOrder
from ..orders.second_order import SecondOrder


def taylor_methods(direction: DIRECTION, order: ORDER, dim: DIM) -> Callable:
    """
    Returns the Taylor approximation method based on the direction and order.

    Args:
        direction (DIRECTION): The direction of the Taylor approximation.
        order (ORDER): The order of the Taylor approximation.
        dim (DIM): The dimension of the function.
    """
    if order == "first":
        return FirstOrder(direction, dim)
    elif order == "second":
        return SecondOrder(direction, dim)
    else:
        raise ValueError("Invalid order!")
