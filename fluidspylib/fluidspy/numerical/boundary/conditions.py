from abc import ABC
from abc import abstractmethod
from typing import List
from typing import Set

from ..constant import DIRS


class BoundaryCondition(ABC):
    """Abstract class for boundary conditions."""

    def __init__(self, dirs: Set[DIRS]):
        self.dirs = dirs

    @abstractmethod
    def apply(self, state: List[List], *args):
        """Apply boundary conditions."""
        pass


class Constant(BoundaryCondition):
    """Constant boundary condition.

    Args:
        dirs (Set[DIRS]): Set of directions to apply the boundary condition.
    """

    def __init__(self, dirs: Set[DIRS]):
        super().__init__(dirs)

    def apply(self, state: List[List], *args):
        """Apply boundary conditions.

        Args:
            state (List[List]): State of the system.
            args (List[float]): Constant values to apply to the boundary based on the direction.
        """
        if "left" in self.dirs:
            state[0] = args[0]
        if "right" in self.dirs:
            state[-1] = args[-1]

        return state


class Insulated(BoundaryCondition):
    """Insulated boundary condition.

    Args:
        dirs (Set[DIRS]): Set of directions to apply the boundary condition.
    """

    def __init__(self, dirs: Set[DIRS]):
        super().__init__(dirs)

    def apply(self, state):
        if "left" in self.dirs:
            state[0] = state[1]
        if "right" in self.dirs:
            state[-1] = state[-2]

        return state
