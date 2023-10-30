import numpy as np

from ..numerical.orders.first_order import FirstOrder
from ..numerical.orders.second_order import SecondOrder


def test_first_order():
    assert FirstOrder("forward", "one").dim == "one"


def test_second_order():
    assert SecondOrder("central", "two").dim == "two"


def test_first_order_one_dim():
    def f(x):
        return x**2

    result = FirstOrder("forward", "one")(f, 2.0, 0.1)
    assert round(result, 1) == 4.1


def test_second_order_two_dim():
    def g(t, x):
        return np.cos(x) * np.sin(t)

    result = SecondOrder("forward", "two")(g, [1, 2], [0, 0.1], 1)
    assert round(result, 3) == 0.424
