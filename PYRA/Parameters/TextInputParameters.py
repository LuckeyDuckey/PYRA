import pygame

from .AbstractParameters import *

class TextInputParameters(Parameters):
    """
    Encapsulates the configuration parameters for a text input element
    
    Attributes:
        Callback (function): A required function that is triggered when the text input is submitted
        CharacterLength (int): The maximum number of characters allowed in the text input
        PreviewText (str): The placeholder text displayed when no input has been provided
        Font (pygame.Font): The font used to render the input text, should be monospaced
        TextColor (list[int]): A list representing the RGBA color of the entered text, with values in the range 0-255
        PreviewTextColor (list[int]): A list representing the RGBA color of the preview (placeholder) text, with values in the range 0-255

    Raises:
        ValueError: If required initialization arguments are missing
        AttributeError: If an invalid parameter name is provided
        TypeError: If a parameter is supplied with an incorrect data type
    """

    Parameters = {
        "Callback": Parameter(Required=True),
        "CharacterLength": Parameter(Type=int, Required=True),
        "PreviewText": Parameter(Type=str, Required=True),
        "Font": Parameter(Type=pygame.Font, Required=True),
        "TextColor": Parameter([0, 0, 0], Type=list),
        "PreviewTextColor": Parameter([127, 127, 127], Type=list),
    }
