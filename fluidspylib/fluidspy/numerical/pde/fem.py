from typing import Callable
from typing import List

import numpy as np

from ..constant import METHOD
from .fdm_explicit import ftcs, richardson
from .fdm_implicit import btcs


class FiniteElementMethod:
    """
    The FiniteElementMethod class is a class that defines the finite element method for solving PDE's.

    Args:
        method (METHOD): The method used for solving the PDE.
        available_methods (dict): A dictionary containing the available methods for solving the PDE.
    """

    def __init__(self, method: METHOD, logging: bool = False) -> None:
        self.method = method
        self.logging = logging
        self.available_methods = {}

    def __call__(
        self,
        type_of_method: str,
        num_steps: int,
        initial_state: List[List],
        step: List,
        alpha: float,
        threshold: float = 1e-4,
    ) -> List[List]:
        """
        Solves the PDE using the finite element method.

        Args:
            type_of_method (str): name of finite element method.
            num_steps (int): num of iterations.
            initial_state (List[List]): intial state matrix of the PDE.
            step (List): step size for time and space axes.
            alpha (float): constant for the PDE.
            threshold (float): threshold value for convergence.

        Returns:
            List[List]: The solution set of the PDE.
        """
        if type_of_method not in self.available_methods:
            raise ValueError("Invalid method! Does not exist in the available methods.")

        return self.solve(
            self.available_methods[type_of_method],
            num_steps,
            initial_state,
            step,
            alpha,
            threshold,
        )

    def solve(
        self,
        method: Callable,
        num_steps: int,
        initial_state: List[List],
        step: List,
        alpha: float,
        threshold: float,
    ) -> List[List]:
        states_matrix = [initial_state]

        for j in range(num_steps):
            new_state = [initial_state[0]]

            for i in range(1, len(initial_state) - 1):
                try:
                    state = [
                        initial_state[i - 1],
                        initial_state[i],
                        initial_state[i + 1],
                    ]
                    new_state.append(method(state, step, alpha))
                except Exception as e:
                    print(f"Error at {i+1}th index in {j+1}th time step. {e}")
                    return
            new_state.append(initial_state[-1])

            if self.logging:
                print(f"The solution at {j+1}th iteration is {new_state}")
            states_matrix.append(new_state)

            if self.early_stopping(states_matrix, threshold):
                print(f"Early stopping at {j+1}th iteration!")
                return states_matrix

            initial_state = new_state

        return states_matrix

    def early_stopping(self, states_matrix: List[List], threshold: float) -> bool:
        """
        Checks if the solution has converged.

        Args:
            states_matrix (List[List]): The solution set of the PDE.
            threshold (float): The threshold value for convergence.

        Returns:
            bool: True if the solution has converged, False otherwise.
        """
        diff = np.array(states_matrix[-1]) - np.array(states_matrix[-2])
        return np.linalg.norm(diff) < threshold

    def __str__(self) -> str:
        return f"{self.method} finite element method."


class Explicit(FiniteElementMethod):
    """
    Explicit finite element method for solving PDE's.
    """

    def __init__(self, method: METHOD = "explicit", logging: bool = False) -> None:
        super().__init__(method, logging)
        self.available_methods = {"ftcs": ftcs.ftcs, "richardson": richardson.richardson}


class Implicit(FiniteElementMethod):
    """
    Implicit finite element method for solving PDE's.
    """

    def __init__(self, method: METHOD = "implicit") -> None:
        super().__init__(method)
        self.available_methods = {"btcs": btcs.btcs}


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
