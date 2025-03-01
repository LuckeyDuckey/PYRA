import PYRA.Parameters.OutlineParameters
import PYRA.Parameters.ShadowParameters

from .AbstractParameters import *

class ContainerParameters(Parameters):
    """
    Encapsulates the configuration parameters for a container element

    Attributes:
        Resolution (PYRA.Vec2): A Vec2 instance specifying the container's pixel dimensions, this attribute is required
        Color (list[int]): A list representing the background color in RGBA format, where each value should be in the range 0-255
        CornerRadius (int): An integer that defines the radius used to round the container's corners
        OutlineParameters (PYRA.OutlineParameters): An instance of OutlineParameters that defines the appearance of the container's outline
        ShadowParameters (PYRA.ShadowParameters): An instance of ShadowParameters that defines the properties of the shadow cast by the container

    Raises:
        ValueError: If required initialization arguments are missing
        AttributeError: If an invalid parameter name is provided
        TypeError: If a parameter is supplied with an incorrect data type
    """

    Parameters = {
        "Resolution": Parameter(Type=PYRA.Vec2, Required=True),
        "Color": Parameter([0, 0, 0, 0], Type=list),
        "CornerRadius": Parameter(0, Type=int),
        "OutlineParameters": Parameter(None, Type=PYRA.OutlineParameters),
        "ShadowParameters": Parameter(None, Type=PYRA.ShadowParameters),
    }
