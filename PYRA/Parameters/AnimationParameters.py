from .AbstractParameters import *

class AnimationParameters(Parameters):
    """
    Encapsulates the configuration parameters for an animation
    
    Attributes:
        Duration (float): The length of the animation in seconds, this attribute is required
        EasingFunction (function): A function that takes a time value and returns a modified value, typically used for
            easing the animation's progress (e.g. making it accelerate or decelerate)

    Raises:
        ValueError: If required initialization arguments are missing
        AttributeError: If an invalid parameter name is provided
        TypeError: If a parameter is supplied with an incorrect data type
    """

    Parameters = {
        "Duration": Parameter(Type=float, Required=True),
        "EasingFunction": Parameter(lambda Time : Time),
    }
