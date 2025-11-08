import pygame

from .AbstractParameters import *

class ImageParameters(Parameters):
    """
    Encapsulates the configuration parameters for an image element
    
    Attributes:
        Image (pygame.Surface): A required pygame Surface object that specifies the image to be rendered
        CornerRadius (int): An integer that defines the radius used to round the corners of the image
        Anchor (PYRA.Vec2): A Vec2 instance indicating the anchor point for the image in its container, the default value (0.5, 0.5) centers the image

    Raises:
        ValueError: If required initialization arguments are missing
        AttributeError: If an invalid parameter name is provided
        TypeError: If a parameter is supplied with an incorrect data type
    """

    Parameters = {
        "Image": Parameter(Type=pygame.Surface, Required=True),
        "CornerRadius": Parameter(0, Type=int),
        "Anchor": Parameter(PYRA.Vec2([0.5, 0.5]), Type=PYRA.Vec2),
    }
