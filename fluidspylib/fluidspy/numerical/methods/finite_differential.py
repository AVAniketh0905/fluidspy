from abc import ABC

from ..boundary.composite import CompositeBoundary
from ..material_properties import MaterialProperties
from ..state import SimulationState


class FiniteDifferentialMethod(ABC):
    def __init__(
        self,
        state: SimulationState,
        properties: MaterialProperties,
        boundary_conditions: CompositeBoundary,
    ):
        self.state = state
        self.properties = properties
        self.bounds = boundary_conditions
