import numpy as np

from fluidspy.numerical.pde.finite_element_methods import finite_element_method
from fluidspy.numerical.taylor.taylor_caller import taylor_methods


def testing_one_dim_taylor():
    def f(x):
        return np.sin(x)

    x, h = 2.0, 0.1

    taylor = taylor_methods("central", "first", "one")
    print(taylor, f"{taylor(f, x, h):.3f}")

    taylor = taylor_methods("central", "second", "one")
    print(taylor, f"{taylor(f, x, h):.3f}")


def testting_twi_dim_taylor():
    def g(t, x):
        return np.cos(x) * np.sin(t)

    taylor = taylor_methods("central", "first", "two")
    print(taylor, "step in time axis", f"{taylor(g, [1, 1], [0.1, 0], 0):.3f}")

    taylor = taylor_methods("forward", "second", "two")
    print(taylor, "step in space axis", f"{taylor(g, [1, 2], [0, 0.1], 1):.3f}")


def testing_ftcs():
    initial_state = [1, 2, 4, 6, 4, 2, 1]
    step, alpha = [0.1, 0.5], 5e-3

    fem = finite_element_method("explicit", logging=True)
    fem("ftcs", 10, initial_state, step, alpha, 1e-4)
    F_o = alpha * step[0] / step[1] ** 2

    print("F_o = {:.3f}".format(F_o))


# def plot_states(states, F_o):
#     plt.title("Solution of the PDE with F_o = {:.3f}".format(F_o))
#     for i in range(0, len(states), len(states) // 10):
#         plt.plot(states[i], label=f"t = {i}", c='C{}'.format(i))
#     plt.legend()
#     plt.show()


if __name__ == "__main__":
    # testing_one_dim_taylor()
    # testting_twi_dim_taylor()
    testing_ftcs()
