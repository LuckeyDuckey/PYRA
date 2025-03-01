import PYRA.VectorMathClass

class Parameter:
    def __init__(self, DeafultValue=None, Type=None, Required=False):
        self.DeafultValue = DeafultValue
        self.Type = Type
        self.Required = Required

class Parameters:
    Required = object()
    Parameters = {}

    def __init__(self, **Attributes):
        # Check for required parameters
        MissingParameters = [Key for Key, Value in self.Parameters.items() if Value.Required and Key not in Attributes]
        if MissingParameters:
            raise ValueError(f"Missing required parameters: {', '.join(MissingParameters)}")

        # Set parameters with default values
        for Key, Value in self.Parameters.items():
            super().__setattr__(Key, Value.DeafultValue)

        # Set parameters with provided values
        for Key, Value in Attributes.items():
            setattr(self, Key, Value)

    def __setattr__(self, Name, Value):
        if Name not in self.Parameters:
            raise AttributeError(f"Invalid attribute: {Name}")

        ExpectedType = self.Parameters[Name].Type
        if ExpectedType and not isinstance(Value, ExpectedType):
            raise TypeError(f"Expected type {ExpectedType.__name__} for '{Name}', got {type(Value).__name__}")

        super().__setattr__(Name, Value)
