from typing import Callable

from ..constant import METHOD
from .explicit import Explicit


def finite_element_method(method: METHOD, logging: bool = False) -> Callable:
    """
    Returns the finite element method based on the method.

    Args:
        method (METHOD): The method used for solving the PDE.
    """
    if method == "explicit":
        return Explicit(method, logging)
    elif method == "implicit":
        pass
    else:
        raise ValueError("Invalid method!")
