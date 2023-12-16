from typing import List


def ftcs(initial_state: List[List], step: List, alpha: float) -> float:
    """
    Forward-time Central-space method for solving PDE's.

    Args:
        initial_state (List[List]): The initial state of the PDE. (T(t, x))
        step (List): The vector of step size for time and space axes.
        alpha (float): The constant for the PDE.

    Returns:
        float: The solution of the PDE. (T(t+1, x))
    """
    F_o = alpha * step[0] / step[1] ** 2
    size = len(initial_state)

    if F_o > 0.5:
        raise ValueError("The solution is unstable! Please choose a smaller time step.")

    parametric_matrix = [0 for _ in range(size)]
    for i in range(size):
        if i == 1:
            parametric_matrix[i] = 1 - 2 * F_o
        else:
            parametric_matrix[i] = F_o

    return np.matmul(parametric_matrix, initial_state)
