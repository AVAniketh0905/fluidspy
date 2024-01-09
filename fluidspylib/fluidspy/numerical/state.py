from dataclasses import dataclass
from types import NoneType

import numpy as np


@dataclass
class SimulationState:
    state: np.ndarray | NoneType = None

    def get_state(self) -> np.ndarray:
        return self.state

    def set_state(self, value: np.ndarray):
        self.state = value

    def get_dimension(self):
        return self.state.ndim
