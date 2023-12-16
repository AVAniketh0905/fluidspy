import pytest
from ..numerical.pde.fem import Explicit, Implicit


def test_explicit_initialization():
    explicit = Explicit("ftcs", True)
    assert isinstance(explicit, Explicit)
    assert explicit.method == "ftcs"
    assert explicit.logging == True


def test_explicit_available_methods():
    explicit = Explicit("ftcs", True)
    assert "ftcs" in explicit.available_methods
    assert "richardson" in explicit.available_methods


def test_Explicit_unavailable_method():
    with pytest.raises(ValueError):
        Explicit("unavailable_method", True)
