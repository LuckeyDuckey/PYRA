from .AbstractParameters import *

class ShadowParameters(Parameters):
    """
    Encapsulates the configuration parameters that define the appearance of a containers shadow
    
    Attributes:
        Size (int): An integer specifying the size or spread of the shadow effect in pixels
        Color (list[int]): A list representing the RGB color of the shadow, with each component in the range 0-255
        Intensity (int): An integer indicating the opacity or strength of the shadow

    Raises:
        ValueError: If required initialization arguments are missing
        AttributeError: If an invalid parameter name is provided
        TypeError: If a parameter is supplied with an incorrect data type
    """

    Parameters = {
        "Size": Parameter(Type=int, Required=True),
        "Color": Parameter([0, 0, 0], Type=list),
        "Intensity": Parameter(0, Type=int),
    }
