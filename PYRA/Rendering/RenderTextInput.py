import pygame, time

import PYRA.VectorMathClass

def RenderTextInput(Parameters, Element):
    # Create surface to render too (plus make it transparent)
    RenderSurface = pygame.Surface(Element.LetterSize * PYRA.Vec2(Parameters.CharacterLength, 1)).convert_alpha()
    RenderSurface.fill([0, 0, 0, 0])

    # Render selection region
    SelectionPosition = PYRA.Vec2(min(Element.InsertionIndex, Element.SelectionIndex) - Element.TextScrollOffset, 0) * Element.LetterSize
    SelectionSize = PYRA.Vec2(abs(Element.InsertionIndex - Element.SelectionIndex), 1) * Element.LetterSize
    SelectionRect = pygame.Rect(SelectionPosition, SelectionSize)
    pygame.draw.rect(RenderSurface, [25, 75, 200], SelectionRect)

    # Render current text input / preview text inside
    if Element.UserInputText:
        RenderedTextInsideBox = Parameters.Font.render(Element.UserInputText[Element.TextScrollOffset:], True, Parameters.TextColor)
    else:
        RenderedTextInsideBox = Parameters.Font.render(Parameters.PreviewText, True, Parameters.PreviewTextColor)
    RenderSurface.blit(RenderedTextInsideBox, [0, 0])

    # Render insertion point with period 0.5 seconds
    if not Element.IsFocused or time.time() % 1 > 0.5:
        return RenderSurface
    
    TextCursorPosition = PYRA.Vec2(Element.LetterSize.x * (Element.InsertionIndex - Element.TextScrollOffset), 0)
    TextCursorSize = PYRA.Vec2(1, Element.LetterSize.y)
    TextCursorRect = pygame.Rect(TextCursorPosition, TextCursorSize)
    pygame.draw.rect(RenderSurface, Parameters.TextColor, TextCursorRect)
    
    return RenderSurface
