import pygame
from pygame.locals import *

import PYRA.Rendering.RenderText

from .AbstractElement import Element

class TextElement(Element):
    """
    Represents a text element within the UI

    Attributes:
        PositionParameters (PYRA.PositionParameters): Defines the position and layout of the text
        ContainerParameters (PYRA.ContainerParameters): Defines the container for the text element
        TextParameters (PYRA.TextParameters): Defines the content, style, and behavior of the text
    """

    def __init__(self, PositionParameters, ContainerParameters, TextParameters):
        super().__init__(PositionParameters, ContainerParameters)

        self.TextParameters = TextParameters

        # Render text onto container
        PYRA.RenderText(self.Surface, self.TextParameters)

    def Render(self, Display, MousePosition, Events, DeltaTime):
        Display.blit(self.Surface, self.PositionParameters.Position)
