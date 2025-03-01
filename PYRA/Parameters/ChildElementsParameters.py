from .AbstractParameters import *

class ChildElementsParameters(Parameters):
    """
    Encapsulates the configuration parameters for managing child elements within a container
    
    Attributes:
        ChildElements (list): A list containing child elements that belong to the parent container
        Direction (str): Defines the layout direction of the child elements, options include "Vertical" or "Horizontal"
        JustifyContent (str): Determines how child elements are spaced along the main axis, values include "Start", "Center", and "End"
        AlignContent (str): Specifies how child elements are aligned along the cross axis, values include "Start", "Center", and "End"
        Scrollable (bool): A boolean indicating whether the container allows scrolling, along the vertical axis, when content exceeds its bounds
        Padding (list[int]): A list of four integers representing the padding values for the top, bottom, left, and right sides of the container

    Raises:
        ValueError: If required initialization arguments are missing
        AttributeError: If an invalid parameter name is provided
        TypeError: If a parameter is supplied with an incorrect data type
    """

    Parameters = {
        "ChildElements": Parameter([], Type=list),
        "Direction": Parameter("Vertical", Type=str),
        "JustifyContent": Parameter("Start", Type=str),
        "AlignContent": Parameter("Start", Type=str),
        "Scrollable": Parameter(False, Type=bool),
        "Padding": Parameter([0, 0, 0, 0], Type=list), # Top, Bottom, Left, Right
    }
    