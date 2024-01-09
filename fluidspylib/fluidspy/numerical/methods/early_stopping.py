from typing import List

import numpy as np

from ..state import SimulationState


class EarlyStopping:
    def __call__(self, state: SimulationState, threshold: float) -> bool:
        """
        Checks if the solution has converged.

        Args:
            states_matrix (List[List]): The solution set of the PDE.
            threshold (float): The threshold value for convergence.

        Returns:
            bool: True if the solution has converged, False otherwise.
        """
        states_matrix = state.get_state()
        diff = np.array(states_matrix[-1]) - np.array(states_matrix[-2])
        return np.linalg.norm(diff) < threshold
