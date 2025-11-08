from .AbstractParameters import *

class OutlineParameters(Parameters):
    """
    Encapsulates the configuration parameters that define the appearance of an outline
    
    Attributes:
        Thickness (int): The thickness of the outline in pixels, this is required
        Color (list[int]): A list representing the color of the outline in RGB format, where each value should be in the range 0-255

    Raises:
        ValueError: If required initialization arguments are missing
        AttributeError: If an invalid parameter name is provided
        TypeError: If a parameter is supplied with an incorrect data type
    """

    Parameters = {
        "Thickness": Parameter(Type=int, Required=True),
        "Color": Parameter([0, 0, 0], Type=list),
    }
