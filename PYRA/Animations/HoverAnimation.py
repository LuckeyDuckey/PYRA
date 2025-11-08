import pygame
from pygame.locals import *

from .AbstractAnimation import Animation

class HoverAnimation(Animation):
    """
    Represents an animation that changes an element's color when hovered over

    This animation smoothly transitions the color of the element from its original color to a specified
    hover color based on an easing function

    Attributes:
        OriginalColor (list[int]): The initial color of the element before hover
        HoverColor (list[int]): The color of the element when hovered over
    """

    def __init__(self, AnimationParameters, OriginalColor, HoverColor):
        super().__init__(AnimationParameters)

        self.OriginalColor = OriginalColor
        self.HoverColor = HoverColor

    def GetUpdatedValue(self, AnimationProgress):
        return [self.Lerp(Original, Hover, AnimationProgress) for Original, Hover in zip(self.OriginalColor, self.HoverColor)]
