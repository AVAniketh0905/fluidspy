from typing import List

from ..state import SimulationState
from .direction import Direction


class CompositeBoundary:
    children: List[Direction]
    state: SimulationState

    def __init__(self, state, *args) -> None:
        self.state = state
        self.children = list(args)

    def apply(self):
        for child in self.children:
            child.apply(self.state)
