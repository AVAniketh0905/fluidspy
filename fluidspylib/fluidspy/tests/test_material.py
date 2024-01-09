from ..numerical.material_properties import FluidProperties
from ..numerical.material_properties import MaterialProperties
from ..numerical.material_properties import ThermalProperties


def test_material_properties():
    material = MaterialProperties("Steel", 7850, 500, 0.71)
    assert material.name == "Steel"
    assert material.density == 7850
    assert material.specific_heat == 500
    assert material.prandtl == 0.71


def test_thermal_properties():
    material = ThermalProperties("Copper", 8940, 385, 0.71, 401, 0.000016)
    assert material.name == "Copper"
    assert material.density == 8940
    assert material.specific_heat == 385
    assert material.prandtl == 0.71
    assert material.thermal_conductivity == 401
    assert material.thermal_expansion_coefficient == 0.000016


def test_fluid_properties():
    material = FluidProperties("Water", 1000, 4186, 7.0, 0.001)
    assert material.name == "Water"
    assert material.density == 1000
    assert material.specific_heat == 4186
    assert material.prandtl == 7.0
    assert material.viscosity == 0.001
