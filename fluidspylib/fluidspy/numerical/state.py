from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True, order=True)
class SimulationState:
    state: np.ndarray = None

    def set_state(self, state: np.ndarray):
        self.state = state

    def get_state(self):
        return self.state

    def get_dimension(self):
        return self.state.ndim
