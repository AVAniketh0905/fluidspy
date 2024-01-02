from abc import ABC
from abc import abstractmethod
from typing import List
from typing import Set

from ..constant import DIRS


class BoundaryCondition(ABC):
    def __init__(self, dirs: Set[DIRS]):
        self.dirs = dirs

    @abstractmethod
    def apply(self, state: List[List], *args):
        pass


class Constant(BoundaryCondition):
    def __init__(self, dirs: Set[DIRS]):
        super().__init__(dirs)

    def apply(self, state: List[List], *args):
        if "left" in self.dirs:
            state[0] = args[0]
        if "right" in self.dirs:
            state[-1] = args[-1]

        return state


class Insulated(BoundaryCondition):
    def __init__(self, dirs: Set[DIRS]):
        super().__init__(dirs)

    def apply(self, state):
        if "left" in self.dirs:
            state[0] = state[1]
        if "right" in self.dirs:
            state[-1] = state[-2]

        return state
