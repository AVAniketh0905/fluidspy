from abc import ABC
from abc import abstractmethod
from typing import List

import numpy as np

from ..boundary.composite import CompositeBoundary
from ..dim import Dimension
from ..material_properties import MaterialProperties
from ..material_properties import ThermalProperties
from ..state import SimulationState
from ..step import Step
from ..step import Vector


class FiniteDifferentialMethod(ABC):
    def __init__(
        self,
        state: SimulationState,
        dim: Dimension,
        properties: ThermalProperties,
        boundary_conditions: CompositeBoundary,
        step: Step,
    ):
        self.state = state
        self.dim = dim
        self.properties = properties
        self.bounds = boundary_conditions
        self.step = step

    @abstractmethod
    def stability(self):
        pass

    @abstractmethod
    def get_parametric(self):
        pass

    def apply_parametric(self):
        parametric_matrix = self.get_parametric()

        resultant = self.state.get_state() + self.dim.convolution(
            self.state.get_state(), parametric_matrix
        )

        return self.state.set_state(resultant)

    def solve(self):
        """
        Solves the PDE.

        Returns:
            List: The solution of the PDE.
        """

        # print("before para", self.state.get_state())
        self.apply_parametric()
        # print("after para", self.state.get_state())
        self.bounds.apply()
        # print("after boundary", self.state.get_state())
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
            # print("Running start:iter", i)
            states.append(self.solve())
            print("state {}\n".format(i + 1), states[-1])
            # print("Running end:iter", i)
            # print()

        return states


class FTCS(FiniteDifferentialMethod):
    F_o: Vector

    def __init__(
        self,
        state: SimulationState,
        dim: Dimension,
        properties: ThermalProperties,
        boundary_conditions: CompositeBoundary,
        step: Step,
    ):
        super().__init__(state, dim, properties, boundary_conditions, step)
        self.alpha = self.properties.thermal_expansion_coefficient
        self.get_fourier_number()
        self.stability()

    def get_fourier_number(self):
        self.F_o = Vector()
        self.F_o.x = self.alpha * self.step.time / (self.step.vec.x**2)
        self.F_o.y = self.alpha * self.step.time / (self.step.vec.y**2)
        self.F_o.z = self.alpha * self.step.time / (self.step.vec.z**2)

    def stability(self):
        if self.F_o > Vector(0.5, 0.5, 0.5):
            raise ValueError(
                "The solution is unstable! Please choose a smaller time step."
            )

    def get_parametric(self):
        if self.state.get_dimension() == 1:
            return np.array([self.F_o.x, 1 - 2 * self.F_o.x, self.F_o.x])

        return np.array(
            [
                [0, self.F_o.y, 0],
                [self.F_o.x, -2 * (self.F_o.x + self.F_o.y), self.F_o.x],
                [0, self.F_o.y, 0],
            ]
        )
