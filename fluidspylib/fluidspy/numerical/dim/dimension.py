from abc import ABC
from abc import abstractmethod
from typing import List

import numpy as np
from colorama import init


class Dimension(ABC):
    @abstractmethod
    def validate(self):
        pass


class OneDimSpatial(Dimension):
    initial_conditions: List[float] = np.array()

    def __init__(self, initial_conditions):
        if not self.validate():
            raise ValueError("Invalid initial conditions for 1D spatial dimension")
        self.initial_conditions = initial_conditions

    def validate(self):
        return self.intial_conditions.shape == (1, 1)
