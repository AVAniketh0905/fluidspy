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
from ..numerical.material_properties import ThermalProperties
from ..numerical.methods.finite_differential import FTCS
from ..numerical.state import SimulationState
from ..numerical.step import Step
from ..numerical.step import Vector


def create_state_dim(state, dim, shape):
    dim = dim(state)
    dim.create_grid(shape)

    return dim


def test_ftcs():
    state = SimulationState()
    dim = create_state_dim(state, OneDimSpatial, 10)
    boundary = CompositeBoundary(
        Left(5, state, Constant()), Right(10, state, Insulated())
    )
    boundary.init_apply()
    material = ThermalProperties("Copper", 8940, 385, 0.71, 401, 0.0016)
    step = Step(0.1, Vector(0.1))
    method = FTCS(
        state,
        dim,
        material,
        boundary,
        step,
    )
    method.run(10)

    assert state.get_state()[0] == 5
    assert state.get_state()[-1] != 10


def test_ftcs_two_dim():
    state = SimulationState()
    dim = create_state_dim(state, TwoDimSpatial, (5, 5))
    boundary = CompositeBoundary(
        Left(5, state, Constant()),
        Right(10, state, Constant()),
        Top(5, state, Constant()),
        Bottom(10, state, Constant()),
    )
    boundary.init_apply()
    material = ThermalProperties("Copper", 8940, 385, 0.71, 401, 0.016)
    step = Step(0.1, Vector(0.1, 0.1))
    method = FTCS(
        state,
        dim,
        material,
        boundary,
        step,
    )
    method.run(10)

    assert state.get_state()[0, 0] == 5
    assert state.get_state()[-1, -1] == 10
