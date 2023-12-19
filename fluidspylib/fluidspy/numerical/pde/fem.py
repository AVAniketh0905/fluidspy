from typing import Callable
from typing import List

import numpy as np

from ..boundary.conditions import BC
from ..constant import METHOD
from .fdm_explicit import ftcs
from .fdm_explicit import richardson
from .fdm_implicit import btcs


class FiniteElementMethod:
    """
    The FiniteElementMethod class is a class that defines the finite element method for solving PDE's.

    Args:
        method (METHOD): The method used for solving the PDE.
        available_methods (dict): A dictionary containing the available methods for solving the PDE.
    """

    def __init__(self, method: METHOD, bc: BC, logging: bool = False) -> None:
        self.method = method
        self._bc = bc
        self.logging = logging
        self._available_methods = {}

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
        if type_of_method not in self._available_methods:
            raise ValueError("Invalid method! Does not exist in the available methods.")

        return self.solve(
            self._available_methods[type_of_method],
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
        curr_state, states_matrix = initial_state, [initial_state]

        for j in range(num_steps):
            try:
                new_state = self.single_time_step(curr_state, method, step, alpha)
            except IndexError as e:
                print(f"IndexError at {j+1}th iteration. {e}")
                return
            except ValueError as e:
                print(f"ValueError at {j+1}th iteration. {e}")
                return

            new_state = self._bc.apply(new_state, initial_state[0], initial_state[-1])

            if self.logging and j % (num_steps * 0.1) == 0:
                print(f"The solution at {j+1}th iteration is {new_state}")
            states_matrix.append(new_state)

            if self.early_stopping(states_matrix, threshold):
                print(f"Early stopping at {j+1}th iteration!")
                return states_matrix

            curr_state = new_state

        return states_matrix

    def single_time_step(self, curr_state, method, step, alpha):
        new_state = list()

        for i in range(len(curr_state)):
            state = self.create_state_matrix(i, curr_state)

            try:
                new_state.append(method(state, step, alpha))
            except IndexError as e:
                raise IndexError(f"IndexError at {i+1}th index. {e}")
            except ValueError as e:
                raise ValueError(f"ValueError at {i+1}th index. {e}")

        return new_state

    def create_state_matrix(self, i, curr_state):
        if i == 0:
            # CHW: shuld be ignored
            state = [curr_state[i], curr_state[i], curr_state[i + 1]]
        elif i == len(curr_state) - 1:
            # CHW: shuld be ignored
            state = [curr_state[i - 1], curr_state[i], curr_state[i]]
        else:
            state = [
                curr_state[i - 1],
                curr_state[i],
                curr_state[i + 1],
            ]

        return state

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

    def __init__(
        self, bc: BC, method: METHOD = "explicit", logging: bool = False
    ) -> None:
        super().__init__(method, bc, logging)
        self._available_methods = {
            "ftcs": ftcs.ftcs,
            "richardson": richardson.richardson,
        }


class Implicit(FiniteElementMethod):
    """
    Implicit finite element method for solving PDE's.
    """

    def __init__(
        self, bc: BC, method: METHOD = "implicit", logging: bool = "False"
    ) -> None:
        super().__init__(method, bc, logging)
        self._available_methods = {"btcs": btcs.btcs}


def finite_element_method(method: METHOD, bc: BC, logging: bool = False) -> Callable:
    """
    Returns the finite element method based on the method.

    Args:
        method (METHOD): The method used for solving the PDE.
    """
    if method == "explicit":
        return Explicit(bc, method, logging)
    elif method == "implicit":
        pass
    else:
        raise ValueError("Invalid method!")
