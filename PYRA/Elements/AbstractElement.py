import pygame
from pygame.locals import *

import PYRA.VectorMathClass
import PYRA.Rendering.RenderContainer

class Element:
    def __init__(self, PositionParameters, ContainerParameters):
        self.PositionParameters = PositionParameters
        self.ContainerParameters = ContainerParameters

        # Render container
        self.Surface = PYRA.RenderContainer(self.ContainerParameters)

        # Calculate position if needed
        if PositionParameters.Position:
            self.CalculatePosition()

    def CalculatePosition(self):
        ShadowOffset = PYRA.Vec2(self.Surface.get_size()) - self.ContainerParameters.Resolution
        PositionOffsetByShadow = self.PositionParameters.Position - ShadowOffset * 0.5

        AnchorOffset = self.ContainerParameters.Resolution * self.PositionParameters.Anchor
        PositionOffsetByAnchor = PositionOffsetByShadow - AnchorOffset

        self.PositionParameters.Position = PositionOffsetByAnchor

    def Render(self, Display, MousePosition, Events, DeltaTime):
        raise NotImplementedError("Child classes must implement Render()")
