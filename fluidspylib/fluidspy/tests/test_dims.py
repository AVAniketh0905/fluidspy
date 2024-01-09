from ..numerical.dim import OneDimSpatial
from ..numerical.dim import TwoDimSpatial
from ..numerical.state import SimulationState

state = SimulationState()


def test_one_dim_spatial():
    # Check that the shape is correct
    one_dim = OneDimSpatial(state)
    one_dim.create_grid(10)
    assert state.get_state().shape == (10,)
    assert state.get_dimension() == 1


def test_two_dim_spatial():
    two_dim = TwoDimSpatial(state)
    two_dim.create_grid((10, 10), base_value=1.0)

    # Check that the shape is correct
    assert state.get_state().shape == (10, 10)
    assert state.get_dimension() == 2

    # Check that the base value is set correctly
    assert state.get_state()[0][0] == 1.0
