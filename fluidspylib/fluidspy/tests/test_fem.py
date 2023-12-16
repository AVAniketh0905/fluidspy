import pytest
from ..numerical.pde.fem import Explicit
from ..numerical.pde.finite_element_methods import finite_element_method


def test_explicit_initialization():
    explicit = finite_element_method("explicit", True)
    assert isinstance(explicit, Explicit)
    assert explicit.method == "explicit"
    assert explicit.logging == True


def test_explicit_available_methods():
    explicit = finite_element_method("explicit", True)
    assert "ftcs" in explicit.available_methods
    assert "richardson" in explicit.available_methods


def test_Explicit_unavailable_method():
    with pytest.raises(ValueError):
        finite_element_method("unavailable_method", True)
