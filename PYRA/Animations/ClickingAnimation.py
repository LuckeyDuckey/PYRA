import pygame
from pygame.locals import *

from .AbstractAnimation import Animation

class ClickingAnimation(Animation):
    """
    Represents an animation that alters an element's color when clicked

    This animation smoothly transitions the color of the element from its original color to a specified
    clicking color based on an easing function

    Attributes:
        OriginalColor (list[int]): The initial color of the element before the click
        ClickingColor (list[int]): The color of the element when clicked
    """

    def __init__(self, AnimationParameters, OriginalColor, ClickingColor):
        super().__init__(AnimationParameters)

        self.OriginalColor = OriginalColor
        self.ClickingColor = ClickingColor

    def GetUpdatedValue(self, AnimationProgress):
        return [self.Lerp(Original, Clicking, AnimationProgress) for Original, Clicking in zip(self.OriginalColor, self.ClickingColor)]
