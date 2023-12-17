from .constant import DIM
from .constant import DIRECTION
from .constant import METHOD
from .constant import ORDER
from .orders.first_order import FirstOrder
from .orders.orders_caller import Order
from .orders.second_order import SecondOrder
from .pde.fem import FiniteElementMethod, Explicit, Implicit, finite_element_method
from .taylor.taylor_caller import taylor_methods
