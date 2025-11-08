from .AbstractParameters import *

class PositionParameters(Parameters):
    """
    Encapsulates the configuration parameters for an elements position
    
    Attributes:
        Position (PYRA.Vec2 or None): Represents the absolute position of the element, if left blank automatic positioning will be applied
        Anchor (PYRA.Vec2): A vector indicating the anchor point used to align the element to its position
        Margin (list[int]): A list specifying the pixel margins around the element in the order [Top, Bottom, Left, Right]


    Raises:
        ValueError: If required initialization arguments are missing
        AttributeError: If an invalid parameter name is provided
        TypeError: If a parameter is supplied with an incorrect data type
    """

    Parameters = {
        "Position": Parameter(None),
        "Anchor": Parameter(PYRA.Vec2([0, 0]), Type=PYRA.Vec2),
        "Margin": Parameter([0, 0, 0, 0], Type=list), # Top, Bottom, Left, Right
    }
