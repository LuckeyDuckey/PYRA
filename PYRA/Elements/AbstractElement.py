import pygame
from pygame.locals import *

import PYRA.VectorMathClass
import PYRA.Rendering.RenderContainer

class Element:
    def __init__(self, PositionParameters, ContainerParameters):
        self.PositionParameters = PositionParameters
        self.ContainerParameters = ContainerParameters

        # Calculate position if needed
        if self.PositionParameters.Position:
            self.CalculatePosition()

    def RenderSurfaceCache(self):
        self.Surface = PYRA.RenderContainer(self.ContainerParameters)

    def CalculatePosition(self):
        ShadowOffset = PYRA.Vec2(getattr(self.ContainerParameters.ShadowParameters or 0, "Size", 0))
        PositionOffsetByShadow = self.PositionParameters.Position - ShadowOffset

        AnchorOffset = self.ContainerParameters.Resolution * self.PositionParameters.Anchor
        PositionOffsetByAnchor = PositionOffsetByShadow - AnchorOffset

        self.PositionParameters.Position = PositionOffsetByAnchor

    def Render(self, Display, MousePosition, Events, DeltaTime):
        raise NotImplementedError("Child classes must implement Render()")
