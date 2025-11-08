from .AbstractParameters import *

class ButtonParameters(Parameters):
    """
    Encapsulates the configuration parameters for a button element
    
    Attributes:
        Callback (callable): A function that is invoked when the button is clicked

    Raises:
        ValueError: If required initialization arguments are missing
        AttributeError: If an invalid parameter name is provided
        TypeError: If a parameter is supplied with an incorrect data type
    """

    Parameters = {
        "Callback": Parameter(Required=True),
    }
