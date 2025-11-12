import pygame, copy
from pygame.locals import *

from PYRA import CursorState
import PYRA.Rendering.RenderText
import PYRA.Rendering.RenderImage

from .AbstractElement import Element

class ButtonElement(Element):
    """
    Represents a button element in the UI with customizable position, appearance, and animations

    Attributes:
        PositionParameters (PYRA.PositionParameters): Defines the position and layout of the button
        ButtonParameters (PYRA.ButtonParameters): Defines the button's appearance and behavior
        ContainerParameters (PYRA.ContainerParameters): Parameters for the container element that holds the button
        TextParameters (PYRA.TextParameters, optional): Parameters for text displayed on the button
        ImageParameters (PYRA.ImageParameters, optional): Parameters for an image displayed on the button
        HoverAnimation (optional): Parameters defining the hover animation when the button is interacted with
        ClickingAnimation (optional): Parameters defining the animation when the button is clicked
    """

    def __init__(self, PositionParameters, ButtonParameters, ContainerParameters, TextParameters=None, ImageParameters=None, HoverAnimation=None, ClickingAnimation=None):
        super().__init__(PositionParameters, ContainerParameters)

        self.ButtonParameters = ButtonParameters
        self.TextParameters = TextParameters
        self.ImageParameters = ImageParameters

        self.HoverAnimation = HoverAnimation
        self.ClickingAnimation = ClickingAnimation

        self.RenderSurfaceCache()

    def RenderSurfaceCache(self):
        super().RenderSurfaceCache()

        if self.TextParameters:
            PYRA.RenderText(self.Surface, self.TextParameters)
        if self.ImageParameters:
            PYRA.RenderImage(self.Surface, self.ImageParameters)

    def RenderAnimation(self, MouseHovering, MouseClicking, DeltaTime):
        AnimatedColor = self.ContainerParameters.Color

        if self.HoverAnimation:
            AnimatedColor = self.HoverAnimation.Update(MouseHovering, DeltaTime)
        
        if self.ClickingAnimation:
            self.ClickingAnimation.OriginalColor = AnimatedColor
            AnimatedColor = self.ClickingAnimation.Update(MouseClicking and MouseHovering, DeltaTime)

        if AnimatedColor == self.ContainerParameters.Color:
            return self.Surface
        
        # Apply animation to surface
        AnimatedContainerParameters = copy.deepcopy(self.ContainerParameters)
        AnimatedContainerParameters.Color = AnimatedColor

        AnimatedSurface = PYRA.RenderContainer(AnimatedContainerParameters)
        if self.TextParameters:
            PYRA.RenderText(AnimatedSurface, self.TextParameters)
        if self.ImageParameters:
            PYRA.RenderImage(AnimatedSurface, self.ImageParameters)

        return AnimatedSurface

    def Render(self, Display, MousePosition, Events, DeltaTime):
        ShadowOffset = self.ContainerParameters.ShadowParameters.Size if self.ContainerParameters.ShadowParameters else PYRA.Vec2(0)
        MouseHovering = pygame.Rect(self.PositionParameters.Position + ShadowOffset, self.ContainerParameters.Resolution).collidepoint(MousePosition)
        MouseClicking = pygame.mouse.get_pressed()[0]

        Display.blit(self.RenderAnimation(MouseHovering, MouseClicking, DeltaTime), self.PositionParameters.Position)

        if not MouseHovering:
            return

        PYRA.CursorState = pygame.SYSTEM_CURSOR_HAND

        for Event in Events:
            if Event.type == MOUSEBUTTONUP:
                if Event.button == 1:
                    self.ButtonParameters.Callback()
