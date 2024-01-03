from typing import List

from .direction import Direction


class CompositeBoundary:
    children: List[Direction]

    def __init__(self, *args) -> None:
        self.children = list(args)

    def init_apply(self):
        for child in self.children:
            child.init_apply()

    def apply(self):
        for child in self.children:
            child.apply()
