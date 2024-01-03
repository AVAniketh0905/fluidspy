from venv import create

import pytest

from ..numerical.boundary import Bottom
from ..numerical.boundary import CompositeBoundary
from ..numerical.boundary import Constant
from ..numerical.boundary import Insulated
from ..numerical.boundary import Left
from ..numerical.boundary import Right
from ..numerical.boundary import Top
from ..numerical.dim.dimension import OneDimSpatial
from ..numerical.dim.dimension import TwoDimSpatial
from ..numerical.state import SimulationState

state = SimulationState()


def create_state_dim(state, dim, shape):
    dim = dim(state)
    dim.create_grid(shape)


def test_composite_boundary():
    create_state_dim(state, OneDimSpatial, 10)
    boundary = CompositeBoundary(
        Left(25, state, Constant()), Right(35, state, Insulated())
    )
    boundary.init_apply()

    assert state.get_state()[0] == 25
    assert state.get_state()[-1] == 35


def test_composite_boundary_wrong_condition():
    create_state_dim(state, OneDimSpatial, 10)
    with pytest.raises(ValueError):
        CompositeBoundary(Left(25, state, Constant()), Top(35, state, Constant()))


def test_two_dim_composite_boundary():
    create_state_dim(state, TwoDimSpatial, (5, 3))

    boundary = CompositeBoundary(
        Left(25, state, Constant()),
        Right(35, state, Insulated()),
        Top(45, state, Constant()),
        Bottom(55, state, Insulated()),
    )
    boundary.init_apply()
    print(state.get_state())

    assert (state.get_state()[1:-1, 0] == [25 for _ in range(3)]).all()
    assert (state.get_state()[1:-1, -1] == [35 for _ in range(3)]).all()
    assert (state.get_state()[0, :] == [45 for _ in range(3)]).all()
    assert (state.get_state()[-1, :] == [55 for _ in range(3)]).all()
