import numpy as np

from ...boundary import CompositeBoundary
from ...dim import Dimension
from ...material_properties import ThermalProperties
from ...methods import FiniteDifferentialMethod
from ...state import SimulationState
from ...step import Step
from ...step import Vector


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
            return np.array([self.F_o.x, -2 * self.F_o.x, self.F_o.x])

        return np.array(
            [
                [0, self.F_o.y, 0],
                [self.F_o.x, -2 * (self.F_o.x + self.F_o.y), self.F_o.x],
                [0, self.F_o.y, 0],
            ]
        )
