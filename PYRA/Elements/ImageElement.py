import pygame
from pygame.locals import *

import PYRA.Rendering.RenderImage

from .AbstractElement import Element

class ImageElement(Element):
    """
    Represents an image element within the UI

    Attributes:
        PositionParameters (PYRA.PositionParameters): Defines the position and layout of the image
        ContainerParameters (PYRA.ContainerParameters): Defines the container for the image element
        ImageParameters (PYRA.ImageParameters): Defines the image source and appearance
    """

    def __init__(self, PositionParameters, ContainerParameters, ImageParameters):
        super().__init__(PositionParameters, ContainerParameters)

        self.ImageParameters = ImageParameters

        # Render image onto container
        PYRA.RenderImage(self.Surface, self.ImageParameters)

    def Render(self, Display, MousePosition, Events, DeltaTime):
        Display.blit(self.Surface, self.PositionParameters.Position)
