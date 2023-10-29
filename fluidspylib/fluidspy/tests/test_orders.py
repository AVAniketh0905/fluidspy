from ..numerical.orders.first_order import FirstOrder


def test_first_order():
    assert FirstOrder("forward", "one").dim == "one"


def test_first_order_one_dim():
    def f(x):
        return x**2

    result = FirstOrder("forward", "one")(f, 2.0, 0.1)
    assert round(result, 1) == 4.1
