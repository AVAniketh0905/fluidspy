from abc import ABC
from abc import abstractmethod
from typing import List

import numpy as np

from ..boundary.composite import CompositeBoundary
from ..material_properties import MaterialProperties
from ..material_properties import ThermalProperties
from ..state import SimulationState


class FiniteDifferentialMethod(ABC):
    def __init__(
        self,
        state: SimulationState,
        properties: ThermalProperties,
        boundary_conditions: CompositeBoundary,
    ):
        self.state = state
        self.properties = properties
        self.bounds = boundary_conditions

    @abstractmethod
    def parametric(self):
        pass

    def solve(self):
        """
        Solves the PDE using the FTCS method.

        Args:
            step (List): The vector of step size for time and space axes.
            alpha (float): The constant for the PDE.

        Returns:
            List: The solution of the PDE.
        """

        print("before para", self.state.get_state())
        self.parametric()
        print("after para", self.state.get_state())
        self.bounds.apply()
        print("after boundary", self.state.get_state())
        return self.state.get_state()

    def run(self, num_iterations: int):
        """
        Runs the solver for a given number of iterations.

        Args:
            num_iterations (int): The number of iterations to run the solver.

        Returns:
            List: The list of states after each iteration.
        """
        states = [self.state.get_state()]

        for i in range(num_iterations):
            print("Running start:iter", i)
            states.append(self.solve())
            print("Running end:iter", i)
            print()

        return states


class FTCS(FiniteDifferentialMethod):
    def __init__(
        self,
        state: SimulationState,
        properties: ThermalProperties,
        boundary_conditions: CompositeBoundary,
        step: List[float],
    ):
        super().__init__(state, properties, boundary_conditions)
        self.alpha = self.properties.thermal_expansion_coefficient
        self.step = step

    def parametric(self):
        """
        Forward-time Central-space method for solving PDE's.

        Args:
            step (List): The vector of step size for time and space axes.
            alpha (float): The constant for the PDE.

        Returns:
            float: The solution of the PDE. (T(t+1, x))
        """

        F_o = self.alpha * self.step[0] / self.step[1] ** 2
        size = self.state.get_state().shape

        if F_o > 0.5:
            raise ValueError(
                "The solution is unstable! Please choose a smaller time step."
            )

        parametric_matrix = np.zeros(size)

        resultant = self.state.get_state() + parametric_matrix

        return self.state.set_state(resultant)
