from typing import List

from ..constant import METHOD
from .fem import FiniteElementMethod


class Implicit(FiniteElementMethod):
    """
    Implicit finite element method for solving PDE's.
    """

    def __init__(self, method: METHOD) -> None:
        super().__init__(method)
        self.available_methods = {"ftcs": self.btcs}

    def btcs(self, next_state: List[List], step: List) -> float:
        """
        Backward-time Central-space method for solving PDE's.

        Args:
            next_state (List[List]): The initial state of the PDE.
            step (List): The vector of time step for time and space axes.

        Returns:
            float: The solution of the PDE. ()
        """
        # parametric_matrix = [[0, 1, 0], [0, 0, 0], [0, 0, 0]]

        pass
