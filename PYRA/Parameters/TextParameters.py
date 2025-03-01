import pygame

from .AbstractParameters import *

class TextParameters(Parameters):
    """
    Encapsulates the configuration parameters for a text element
    
    Attributes:
        Text (str): The string content of the text element, this attribute is required
        Font (pygame.Font):  The font used to render the text, this attribute is required
        Color (list[int]): A list representing the text color in RGBA format, where each value should be in the range 0-255
        WrapLength (int): The maximum width in pixels before text wraps to a new line, the default value of 0 disables wrapping
        Anchor (PYRA.Vec2): A Vec2 instance indicating the anchor point for the text in its container, the default value (0.5, 0.5) centers the text

    Raises:
        ValueError: If required initialization arguments are missing
        AttributeError: If an invalid parameter name is provided
        TypeError: If a parameter is supplied with an incorrect data type
    """

    Parameters = {
        "Text": Parameter(Type=str, Required=True),
        "Font": Parameter(Type=pygame.Font, Required=True),
        "Color": Parameter([0, 0, 0, 0], Type=list),
        "WrapLength": Parameter(0, Type=int),
        "Anchor": Parameter(PYRA.Vec2([0.5, 0.5]), Type=PYRA.Vec2),
    }
