from unittest import TestCase
from src.orders.first_order import FirstOrder


class TestFirstOrder(TestCase):
    def test_first_order(self):
        self.assertEqual(FirstOrder().first_order(), 1)
