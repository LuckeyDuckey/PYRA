class Vec2:
    """
    This class represents a vector with two components (x and y) that supports various
    initialization methods, common arithmetic and indexing operations

    Initialization methods:
      - With a list or tuple: Vec2([x, y])
      - With two separate values: Vec2(x, y)
      - With a single value (applied to both components): Vec2(scalar)

    Indexing methods:
      - Via indices: Vec2[0] and Vec2[1]
      - Via name: Vec2.x and Vec2.y

    Arithmetic methods:
      - Vec on Vec: Vec2(1, 2) + Vec2(3, 4) yields Vec2(4, 6)
      - Vec on Scalar: Vec2(1, 2) + 3 yields Vec2(4, 5)
      - Subtraction, multiplication and division work similarly

    Attributes:
        x (int or float): The x-component of the vector
        y (int or float): The y-component of the vector

    Raises:
        ValueError: If initialization arguments do not conform to any of the supported patterns
        IndexError: If an invalid index (other than 0 or 1) is used
    """

    def __init__(self, x, y=None):
        if isinstance(x, (list, tuple)) and len(x) == 2:  # Vec2([x, y])
            self.x, self.y = x
        elif isinstance(x, (int, float)) and y is None:  # Vec2(scalar, scalar)
            self.x = self.y = x
        elif isinstance(x, (int, float)) and isinstance(y, (int, float)):  # Vec2(x, y)
            self.x, self.y = x, y
        else:
            raise ValueError("Vec2 must be initialized with (x, y), [x, y], or (scalar)")

    def __getitem__(self, Index):
        if Index == 0:
            return self.x
        elif Index == 1:
            return self.y
        else:
            raise IndexError("Vec2 index out of range")

    def __setitem__(self, Index, Value):
        if Index == 0:
            self.x = Value
        elif Index == 1:
            self.y = Value
        else:
            raise IndexError("Vec2 index out of range")

    def __iter__(self):
        return iter([self.x, self.y])

    def __len__(self):
        return 2

    def copy(self):
        return Vec2(self.x, self.y)

    def __repr__(self):
        return f"Vec2({self.x}, {self.y})"

    # Arithmetic operators
    def __add__(self, Value):
        if isinstance(Value, (int, float)):
            return Vec2(self.x + Value, self.y + Value)
        elif isinstance(Value, Vec2):
            return Vec2(self.x + Value.x, self.y + Value.y)
        return NotImplemented

    def __sub__(self, Value):
        if isinstance(Value, (int, float)):
            return Vec2(self.x - Value, self.y - Value)
        elif isinstance(Value, Vec2):
            return Vec2(self.x - Value.x, self.y - Value.y)
        return NotImplemented

    def __mul__(self, Value):
        if isinstance(Value, (int, float)):
            return Vec2(self.x * Value, self.y * Value)
        elif isinstance(Value, Vec2):
            return Vec2(self.x * Value.x, self.y * Value.y)
        return NotImplemented

    def __truediv__(self, Value):
        if isinstance(Value, (int, float)):
            return Vec2(self.x / Value, self.y / Value)
        elif isinstance(Value, Vec2):
            return Vec2(self.x / Value.x, self.y / Value.y)
        return NotImplemented

    def __floordiv__(self, Value):
        if isinstance(Value, (int, float)):
            return Vec2(self.x // Value, self.y // Value)
        elif isinstance(Value, Vec2):
            return Vec2(self.x // Value.x, self.y // Value.y)
        return NotImplemented

    # Reverse operators to support "scalar - Vec2"
    __radd__ = __add__

    def __rsub__(self, other):
        if isinstance(other, (int, float)):  # Scalar - Vec2
            return Vec2(other - self.x, other - self.y)
        return NotImplemented

    __rmul__ = __mul__

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):  # Scalar / Vec2
            return Vec2(other / self.x, other / self.y)
        return NotImplemented

    def __rfloordiv__(self, other):
        if isinstance(other, (int, float)):  # Scalar // Vec2
            return Vec2(other // self.x, other // self.y)
        return NotImplemented
