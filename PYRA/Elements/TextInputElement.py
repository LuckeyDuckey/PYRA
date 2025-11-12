import PYRA, pygame, time
from pygame.locals import *

from PYRA import CursorState
import PYRA.Rendering.RenderTextInput

from .AbstractElement import Element

class TextInputElement(Element):
    """
    Represents a text input field where users can type input

    Attributes:
        PositionParameters (PYRA.PositionParameters): Defines the position and layout of the text input
        ContainerParameters (PYRA.ContainerParameters): Defines the container for the text input element
        TextInputParameters (PYRA.TextInputParameters): Defines the behavior and appearance of the input field
    """

    def __init__(self, PositionParameters, ContainerParameters, TextInputParameters):
        super().__init__(PositionParameters, ContainerParameters)

        self.TextInputParameters = TextInputParameters

        self.LetterSize = PYRA.Vec2(self.TextInputParameters.Font.size(" "))
        self.UserInputText = ""

        self.IsFocused = False
        self.MouseSelectingText = False
        
        self.TextScrollOffset = 0
        self.InsertionIndex = 0
        self.SelectionIndex = 0

        self.RenderSurfaceCache()
    
    def ProcessMouseButtonDown(self, Event, MousePosition, MouseHovering, PositionTextInput):
        if Event.button == 1:
            # If clicking this box then change its state
            if MouseHovering:
                self.IsFocused = self.MouseSelectingText = True

                # Change insertion index to clicked index
                SelectedInsertionIndex = round((MousePosition.x - PositionTextInput.x) / self.LetterSize.x)
                MaxInsertionIndex = len(self.UserInputText) - self.TextScrollOffset
                self.InsertionIndex = self.SelectionIndex = min(MaxInsertionIndex, SelectedInsertionIndex) + self.TextScrollOffset

            else:
                self.IsFocused = False
                self.SelectionIndex = self.InsertionIndex

    def ProcessMouseButtonUp(self, Event):
        if Event.button == 1:
            self.MouseSelectingText = False

    def ProcessTextInput(self, Event):
        # Remove selected text
        self.UserInputText = self.UserInputText[:min(self.SelectionIndex, self.InsertionIndex)] + self.UserInputText[max(self.SelectionIndex, self.InsertionIndex):]
        self.InsertionIndex = max(self.InsertionIndex, self.SelectionIndex) - abs(self.InsertionIndex - self.SelectionIndex)

        # Add key to text
        self.UserInputText = self.UserInputText[:self.InsertionIndex] + Event.text + self.UserInputText[self.InsertionIndex:]
        self.InsertionIndex = self.SelectionIndex = self.InsertionIndex + 1

        # If going outside of text box increase offset to keep it in
        if self.InsertionIndex > self.TextScrollOffset + self.TextInputParameters.CharacterLength or self.InsertionIndex < self.TextScrollOffset:
            self.TextScrollOffset = max(0, self.InsertionIndex - self.TextInputParameters.CharacterLength)

    def ProcessKeyDown(self, Event):
        # If backspace remove char at end of string
        if Event.key == pygame.K_BACKSPACE:

            if self.InsertionIndex - self.SelectionIndex:
                # Remove selected text
                self.UserInputText = self.UserInputText[:min(self.SelectionIndex, self.InsertionIndex)] + self.UserInputText[max(self.SelectionIndex, self.InsertionIndex):]
                self.InsertionIndex = self.SelectionIndex = max(self.InsertionIndex, self.SelectionIndex) - abs(self.InsertionIndex - self.SelectionIndex)

            else:
                # Remove one letter
                self.UserInputText = self.UserInputText[:max(0, self.InsertionIndex - 1)] + self.UserInputText[self.InsertionIndex:]
                self.InsertionIndex = self.SelectionIndex = max(0, self.InsertionIndex - 1)

            # If going outside of text box decrease offset to keep it in
            if self.TextScrollOffset > len(self.UserInputText) - self.TextInputParameters.CharacterLength:
                self.TextScrollOffset = max(0, len(self.UserInputText) - self.TextInputParameters.CharacterLength)

        # If enter set value
        elif Event.key == pygame.K_RETURN:
            self.IsFocused = False
            self.TextInputParameters.Callback(self.UserInputText)

        # If left arrow move insertion point
        if Event.key == pygame.K_LEFT:
            self.InsertionIndex = max(0, self.InsertionIndex - 1)

            if self.InsertionIndex < self.TextScrollOffset:
                self.TextScrollOffset = self.InsertionIndex

            # If not selecting text
            if not Event.mod & pygame.KMOD_SHIFT:
                self.SelectionIndex = self.InsertionIndex

        # If right arrow move insertion point
        elif Event.key == pygame.K_RIGHT:
            self.InsertionIndex = min(len(self.UserInputText), self.InsertionIndex + 1)
            InsertionScrollOffset = max(0, self.InsertionIndex - self.TextInputParameters.CharacterLength)

            if InsertionScrollOffset > self.TextScrollOffset:
                self.TextScrollOffset = InsertionScrollOffset

            # If not selecting text
            if not Event.mod & pygame.KMOD_SHIFT:
                self.SelectionIndex = self.InsertionIndex

    def ProcessKeyDownCtrl(self, Event):
        # Check for all select events
        if Event.key == pygame.K_a:

            # Set selection
            self.InsertionIndex = len(self.UserInputText)
            self.SelectionIndex = 0

            # Update offset
            self.TextScrollOffset = max(0, len(self.UserInputText) - self.TextInputParameters.CharacterLength)

        # Check for copy events
        if Event.key == pygame.K_c:
            pygame.scrap.put_text(self.UserInputText[min(self.InsertionIndex, self.SelectionIndex):max(self.InsertionIndex, self.SelectionIndex)])

        # Check for paste events
        if Event.key == pygame.K_v:
            PastedText = pygame.scrap.get_text().strip().strip("\x00")

            # If returned data and it isnt to long add to text
            if not PastedText or len(PastedText) > 50:
                return

            # Remove selected text
            self.UserInputText = self.UserInputText[:min(self.SelectionIndex, self.InsertionIndex)] + self.UserInputText[max(self.SelectionIndex, self.InsertionIndex):]
            self.InsertionIndex = max(self.InsertionIndex, self.SelectionIndex) - abs(self.InsertionIndex - self.SelectionIndex)

            # Add key to text
            self.UserInputText = self.UserInputText[:self.InsertionIndex] + PastedText + self.UserInputText[self.InsertionIndex:]
            self.InsertionIndex = self.SelectionIndex = self.InsertionIndex + len(PastedText)

            # If going outside of text box increase offset to keep it in
            if self.InsertionIndex > self.TextScrollOffset + self.TextInputParameters.CharacterLength or self.InsertionIndex < self.TextScrollOffset:
                self.TextScrollOffset = max(0, self.InsertionIndex - self.TextInputParameters.CharacterLength)

    def ProcessEvents(self, Events, MousePosition, MouseHovering, Position):
        for Event in Events:
            if Event.type == MOUSEBUTTONDOWN:
                self.ProcessMouseButtonDown(Event, MousePosition, MouseHovering, Position)

            elif Event.type == MOUSEBUTTONUP:
                self.ProcessMouseButtonUp(Event)

            elif Event.type == pygame.TEXTINPUT and self.IsFocused:
                self.ProcessTextInput(Event)

            elif Event.type == KEYDOWN and self.IsFocused:
                self.ProcessKeyDown(Event)

                if Event.mod & pygame.KMOD_CTRL:
                    self.ProcessKeyDownCtrl(Event)

    def Render(self, Display, MousePosition, Events, DeltaTime):
        ShadowOffset = self.ContainerParameters.ShadowParameters.Size if self.ContainerParameters.ShadowParameters else PYRA.Vec2(0)
        PositionOffsetByShadow = self.PositionParameters.Position + ShadowOffset

        MouseHovering = pygame.Rect(PositionOffsetByShadow, self.ContainerParameters.Resolution).collidepoint(MousePosition)
        if MouseHovering:
            PYRA.CursorState = pygame.SYSTEM_CURSOR_HAND

        # Render container
        Display.blit(self.Surface, self.PositionParameters.Position)

        # Render text input
        SurfaceTextInput = PYRA.RenderTextInput(self.TextInputParameters, self)
        PositionTextInput = PositionOffsetByShadow + (self.ContainerParameters.Resolution - PYRA.Vec2(SurfaceTextInput.get_size())) * 0.5
        Display.blit(SurfaceTextInput, PositionTextInput)

        # Handle all events and updates for the text input
        self.ProcessEvents(Events, MousePosition, MouseHovering, PositionTextInput)

        # Update selected text based on mouse position
        if self.MouseSelectingText:
            SelectedIndex = round((MousePosition.x - PositionTextInput.x) / self.LetterSize.x)
            ClampedSelectedIndex = max(0, min(len(self.UserInputText) - self.TextScrollOffset, SelectedIndex))
            self.InsertionIndex = ClampedSelectedIndex + self.TextScrollOffset
