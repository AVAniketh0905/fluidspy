from dataclasses import dataclass

from numpy import inf


@dataclass(order=True)
class Vector:
    x: float
    y: float
    z: float

    def __init__(self, x=inf, y=inf, z=inf) -> None:
        """
        Create the spatial step.
        """
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"


class Step:
    time: float
    vec: Vector

    def __init__(
        self,
        time: float,
        vec: Vector = Vector(),
    ):
        """
        Create the time step and the spatial step.

        Args:
            time (float): The time step.
            vec (Vector): The spatial step. Defaults to (0, 0, 0).
        """

        self.time = time
        self.vec = vec

    def __repr__(self) -> str:
        return f"({self.time}, {self.vec})"
