from abc import ABC
from abc import abstractmethod

from ..boundary.composite import CompositeBoundary
from ..dim import Dimension
from ..material_properties import ThermalProperties
from ..state import SimulationState
from ..step import Step


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
            # print("state {}\n".format(i + 1), states[-1])
            # print("Running end:iter", i)
            # print()

        return states
