import pygame
from pygame.locals import *

import PYRA.Parameters.ChildElementsParameters

from .AbstractElement import Element

class ContainerElement(Element):
    """
    Represents a container element that can hold and organize child elements

    Attributes:
        PositionParameters (PYRA.PositionParameters): Defines the position and layout of the container
        ContainerParameters (PYRA.ContainerParameters): Defines the container's appearance and behavior
        ChildElementsParameters (PYRA.ChildElementsParameters): Parameters for the child elements inside the container
    """

    def __init__(self, PositionParameters, ContainerParameters, ChildElementsParameters=PYRA.ChildElementsParameters()):
        super().__init__(PositionParameters, ContainerParameters)

        self.ChildElementsParameters = ChildElementsParameters
        self.ChildElementsToArrange = list(filter(
            lambda ChildElement: ChildElement.PositionParameters.Position == None,
            self.ChildElementsParameters.ChildElements
        ))

        self.ResolutionMinusPadding = self.ContainerParameters.Resolution - PYRA.Vec2(
            self.ChildElementsParameters.Padding[0] + self.ChildElementsParameters.Padding[1],
            self.ChildElementsParameters.Padding[2] + self.ChildElementsParameters.Padding[3]
        )

        # Vars for scrolling
        self.CurrentScrollOffset = 0
        self.TargetScrollOffset = 0
        self.MaxScrollOffset = self.CalculateMaxScrollOffset()

    def CalculateChildPositions(self):
        """
        Calculates the positions of child elements with automatic positioning enabled,
        based on the parameters defined in ChildElementsParameters.
        """

        if self.ChildElementsParameters.Direction == "Horizontal":
            TotalSpaceMainAxis = 0

            for ChildElement in self.ChildElementsToArrange:
                TotalSpaceMainAxis += ChildElement.PositionParameters.Margin[2] + ChildElement.ContainerParameters.Resolution.x + ChildElement.PositionParameters.Margin[3]

            # Determine starting offset based on justify_content
            if self.ChildElementsParameters.JustifyContent == "Center":
                CurrentPositionX = (self.ResolutionMinusPadding.x - TotalSpaceMainAxis) // 2
            elif self.ChildElementsParameters.JustifyContent == "End":
                CurrentPositionX = self.ResolutionMinusPadding.x - TotalSpaceMainAxis
            elif self.ChildElementsParameters.JustifyContent == "Start":
                CurrentPositionX = 0

            for ChildElement in self.ChildElementsToArrange:
                # Position child along main axis
                CurrentPositionX += ChildElement.PositionParameters.Margin[2]
                ChildPosition = PYRA.Vec2([CurrentPositionX, 0])

                # Update CurrentPositionX for next element
                CurrentPositionX += ChildElement.ContainerParameters.Resolution.x + ChildElement.PositionParameters.Margin[3]

                # Position child along cross axis using align_content
                if self.ChildElementsParameters.AlignContent == "Center":
                    ChildPosition.y = (self.ResolutionMinusPadding.y - ChildElement.ContainerParameters.Resolution.y) // 2
                elif self.ChildElementsParameters.AlignContent == "End":
                    ChildPosition.y = self.ResolutionMinusPadding.y - ChildElement.ContainerParameters.Resolution.y - ChildElement.PositionParameters.Margin[1]
                elif self.ChildElementsParameters.AlignContent == "Start":
                    ChildPosition.y = ChildElement.PositionParameters.Margin[0]

                ChildElement.PositionParameters.Position = ChildPosition - PYRA.Vec2([0, round(self.CurrentScrollOffset)])
                ChildElement.CalculatePosition()

        elif self.ChildElementsParameters.Direction == "Vertical":
            TotalSpaceMainAxis = 0

            for ChildElement in self.ChildElementsToArrange:
                TotalSpaceMainAxis += ChildElement.PositionParameters.Margin[0] + ChildElement.ContainerParameters.Resolution.y + ChildElement.PositionParameters.Margin[1]

            # Determine starting offset based on justify_content
            if self.ChildElementsParameters.JustifyContent == "Center":
                CurrentPositionY = (self.ResolutionMinusPadding.y - TotalSpaceMainAxis) // 2
            elif self.ChildElementsParameters.JustifyContent == "End":
                CurrentPositionY = self.ResolutionMinusPadding.y - TotalSpaceMainAxis
            elif self.ChildElementsParameters.JustifyContent == "Start":
                CurrentPositionY = 0

            for ChildElement in self.ChildElementsToArrange:
                # Position child along main axis
                CurrentPositionY += ChildElement.PositionParameters.Margin[0]
                ChildPosition = PYRA.Vec2([0, CurrentPositionY])

                # Update CurrentPositionY for next element
                CurrentPositionY += ChildElement.ContainerParameters.Resolution.y + ChildElement.PositionParameters.Margin[1]

                # Position child along cross axis using align_content
                if self.ChildElementsParameters.AlignContent == "Center":
                    ChildPosition.x = (self.ResolutionMinusPadding.x - ChildElement.ContainerParameters.Resolution.x) // 2
                elif self.ChildElementsParameters.AlignContent == "End":
                    ChildPosition.x = self.ResolutionMinusPadding.x - ChildElement.ContainerParameters.Resolution.x - ChildElement.PositionParameters.Margin[3]
                elif self.ChildElementsParameters.AlignContent == "Start":
                    ChildPosition.x = ChildElement.PositionParameters.Margin[2]

                ChildElement.PositionParameters.Position = ChildPosition - PYRA.Vec2([0, round(self.CurrentScrollOffset)])
                ChildElement.CalculatePosition()

        # Call child containers to arrange their children too
        for ChildElement in self.ChildElementsParameters.ChildElements:
            if type(ChildElement) == ContainerElement:
                ChildElement.CalculateChildPositions()

    def CalculateMaxScrollOffset(self):
        MaxScrollOffset = -self.ResolutionMinusPadding.y

        for ChildElement in self.ChildElementsToArrange:
            MaxScrollOffset += ChildElement.PositionParameters.Margin[0] + ChildElement.ContainerParameters.Resolution.y + ChildElement.PositionParameters.Margin[1]

        return max(0, MaxScrollOffset)
    
    def UpdateScrollOffest(self, Events, DeltaTime):
        ScrollDifference = self.TargetScrollOffset - self.CurrentScrollOffset
        ScrollDifferenceSmoothed = ScrollDifference * DeltaTime * 25

        ScrollSpeedThreshold = 0.1
        if abs(ScrollDifferenceSmoothed) > ScrollSpeedThreshold:
            self.CurrentScrollOffset += ScrollDifferenceSmoothed
        elif ScrollDifference:
            self.CurrentScrollOffset += min(ScrollSpeedThreshold, ScrollDifference)

        if ScrollDifference:
            self.CalculateChildPositions()

        for Event in Events:
            if Event.type == pygame.MOUSEWHEEL:
                self.TargetScrollOffset = max(min(self.TargetScrollOffset - Event.y * 50, self.MaxScrollOffset), 0)

    def Render(self, Display, MousePosition, Events, DeltaTime):
        # Render container
        Display.blit(self.Surface, self.PositionParameters.Position)

        if (
            self.ChildElementsParameters.Scrollable and
            self.ChildElementsParameters.JustifyContent == "Start" and
            self.ChildElementsParameters.Direction == "Vertical"
        ):
            self.UpdateScrollOffest(Events, DeltaTime)

        # Render children
        RenderSurfaceChildren = pygame.Surface(self.ResolutionMinusPadding).convert_alpha()
        RenderSurfaceChildren.fill([0, 0, 0, 0])

        ShadowAndPaddingOffset = (PYRA.Vec2(self.Surface.get_size()) - self.ResolutionMinusPadding) * 0.5
        PositionOffsetByShadowAndPadding = self.PositionParameters.Position + ShadowAndPaddingOffset

        for ChildElement in self.ChildElementsParameters.ChildElements:
            ChildElement.Render(RenderSurfaceChildren, MousePosition - PositionOffsetByShadowAndPadding, Events, DeltaTime)

        Display.blit(RenderSurfaceChildren, PositionOffsetByShadowAndPadding)
