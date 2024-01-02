from ..numerical.dim import OneDimSpatial
from ..numerical.dim import TwoDimSpatial


def test_one_dim_spatial():
    # Check that the shape is correct
    one_dim = OneDimSpatial()
    one_dim.create_grid(10)
    assert one_dim.initial_conditions.shape == (10,)


def test_two_dim_spatial():
    two_dim = TwoDimSpatial()
    two_dim.create_grid((10, 10), base_value=1.0)

    # Check that the shape is correct
    assert two_dim.initial_conditions.shape == (10, 10)

    # Check that the base value is set correctly
    assert two_dim.initial_conditions[0][0] == 1.0
