from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class MaterialProperties:
    """Material properties.

    Args:
        name (str): Material name.
        density (float): Material density.(kg/m^3)
        specific_heat (float): Material specific heat.(J/kg.K)
        prandtl (float): Material Prandtl number.
    """

    name: str
    density: float
    specific_heat: float
    prandtl: float


@dataclass(frozen=True, order=True)
class ThermalProperties(MaterialProperties):
    """Thermal properties.

    Args:
        name (str): Material name.
        density (float): Material density.(kg/m^3)
        specific_heat (float): Material specific heat.(J/kg.K)
        prandtl (float): Material Prandtl number.
        thermal_conductivity (float): Material thermal conductivity.(W/m.K)
        thermal_expansion_coefficient (float): Material thermal expansion coefficient.(1/K)
    """

    thermal_conductivity: float
    thermal_expansion_coefficient: float


@dataclass(frozen=True, order=True)
class FluidProperties(MaterialProperties):
    """Fluid properties.

    Args:
        name (str): Material name.
        density (float): Material density.(kg/m^3)
        specific_heat (float): Material specific heat.(J/kg.K)
        prandtl (float): Material Prandtl number.
        thermal_conductivity (float): Material thermal conductivity.(W/m.K)
        thermal_expansion_coefficient (float): Material thermal expansion coefficient.(1/K)
        viscosity (float): Material viscosity.(Pa.s)
    """

    viscosity: float
