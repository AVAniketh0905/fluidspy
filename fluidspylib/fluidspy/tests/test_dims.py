import pytest

from ..numerical.dim import OneDimSpatial
from ..numerical.dim import TwoDimSpatial


def test_one_dim_spatial():
    # Test init
    pytest.raises(ValueError, OneDimSpatial, [[1, 2], [3, 4]])

    # Test create_grid
    one_dim_spatial = OneDimSpatial([1])
    one_dim_spatial.create_grid(10, 1)
    assert one_dim_spatial.initial_conditions.shape == (10,)


def test_two_dim_spatial():
    # Test init
    pytest.raises(ValueError, TwoDimSpatial, [1, 2, 3])

    # Test create_grid
    two_dim_spatial = TwoDimSpatial([[1, 2], [3, 4]])
    two_dim_spatial.create_grid(1, 10, 10)
    assert two_dim_spatial.initial_conditions.shape == (10, 10)
