from typing import List
from typing import Set

from ..constant import BC
from ..constant import DIRS


class BoundaryCondition:
    def __init__(self, type: BC, dirs: Set[DIRS]):
        self.type = type
        self.dirs = dirs

    def apply(self, state: List[List], *args):
        if self.type == "constant":
            return self.constant(state, *args)
        elif self.type == "insulated":
            return self.insulated(state)
        else:
            raise ValueError(f"Unknown boundary condition type: {self.type}")

    def constant(self, state: List[List], *args):
        if "left" in self.dirs:
            state[0] = args[0]
        if "right" in self.dirs:
            state[-1] = args[-1]

        return state

    def insulated(self, state):
        if "left" in self.dirs:
            state[0] = state[1]
        if "right" in self.dirs:
            state[-1] = state[-2]

        return state
