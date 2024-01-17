import numpy as np

from ..animate.animation import SimulationAnimation
from ..numerical.boundary import CompositeBoundary
from ..numerical.boundary import Constant
from ..numerical.boundary import Insulated
from ..numerical.boundary import Left
from ..numerical.boundary import Right
from ..numerical.dim.dimension import OneDimSpatial
from ..numerical.material_properties import ThermalProperties
from ..numerical.methods.fdm import FTCS
from ..numerical.state import SimulationState
from ..numerical.step import Step
from ..numerical.step import Vector


def one_dim_constant_heat_transfer(iterations=10):
    state = SimulationState()

    dim = OneDimSpatial(state)
    dim.create_grid(10)

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
    states = method.run(iterations)

    new_states = []
    for i, state in enumerate(states):
        nstate = [np.zeros(len(state)), state, np.zeros(len(state))]
        new_states.append(nstate)

    simulation_animation = SimulationAnimation(new_states, repeat=False)

    simulation_animation.show_animation()

    return new_states
