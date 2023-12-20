from enum import Enum


class DIRECTION(Enum):
    """
    The DIRECTION class is an enumeration that defines three possible values: FORWARD, BACKWARD, and CENTRAL.

    Args:
        Enum (str): The enumeration class.
    """

    FORWARD = "forward"
    BACKWARD = "backward"
    CENTRAL = "central"


class ORDER(Enum):
    """
    The ORDER class is an enumeration that defines two possible values: FIRST and SECOND.

    Args:
        Enum (str): The enumeration class.
    """

    FIRST = "first"
    SECOND = "second"


class DIM(Enum):
    """
    The DIM class is an enumeration that defines the
    possible dimensions for the function. The possible values are:
    ONE, TWO, and THREE.
    If used in PDE's the default value is TWO. (i.e. time and space)

    Args:
        Enum (str): The enumeration class.
    """

    ONE = "one"
    TWO = "two"
    THREE = "three"


class METHOD(Enum):
    """
    The METHOD class is an enumeration that defines the possible
    methods for solving the PDE. The possible values are:
    EXPLICIT and IMPLICIT.

    Args:
        Enum (str): The enumeration class.
    """

    EXPLICIT = "explicit"
    IMPLICIT = "implicit"


class BC(Enum):
    """
    The BC class is an enumeration that defines the possible
    boundary conditions for solving the PDE. The possible values are:
    CONSTANT and INSULATED.

    Args:
        Enum (str): The enumeration class.
    """

    CONSTANT = "constant"
    INSULATED = "insulated"


class PARAMETRIC(Enum):
    """
    The PARAMETRIC class is an enumeration that defines the possible
    parametric functions for solving the PDE. The possible values are:
    "parabolic", "hyperbolic", and "elliptic".

    Args:
        Enum (str): The enumeration class.
    """

    PARABOLIC = "parabolic"
    HYPERBOLIC = "hyperbolic"
    ELLIPTIC = "elliptic"


class DIRS(Enum):
    """
    The DIRS class is an enumeration that defines the possible
    directions for applying boundary conditions. The possible values are:
    "left", "right", "top", and "bottom".

    Args:
        Enum (str): The enumeration class.
    """

    LEFT = "left"
    RIGHT = "right"
    TOP = "top"
    BOTTOM = "bottom"
