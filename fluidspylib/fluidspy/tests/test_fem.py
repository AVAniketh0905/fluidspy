import pytest

from ..numerical.boundary.conditions import BoundaryCondition as BC
from ..numerical.pde.fem import Explicit
from ..numerical.pde.fem import finite_element_method

bc = [BC("constant", ["left", "right"])]


def test_explicit_initialization():
    explicit = finite_element_method("explicit", bc, True)
    assert isinstance(explicit, Explicit)
    assert explicit.method == "explicit"
    assert explicit.logging is True


def test_explicit_available_methods():
    explicit = finite_element_method("explicit", bc, True)
    assert "ftcs" in explicit._available_methods
    assert "richardson" in explicit._available_methods


def test_explicit_unavailable_method():
    with pytest.raises(ValueError):
        finite_element_method("unavailable_method", True)
