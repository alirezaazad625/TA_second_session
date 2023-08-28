import math

from collections.abc import Sized
from typing import Callable


class Vector2d(Sized):
    def __len__(self) -> int:
        return int(math.sqrt(math.pow(self.x, 2) + math.pow(self.y, 2)))

    @property
    def length(self) -> int:
        return 2

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other) -> 'Vector2d':
        self._validate_type(other)
        return Vector2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other) -> 'Vector2d':
        self._validate_type(other)
        return Vector2d(self.x - other.x, self.y - other.y)

    def __mul__(self, other) -> 'Vector2d':
        self._validate_type(other)
        return Vector2d(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        # raise ValueError()
        raise NotImplementedError()

    def __matmul__(self, other) -> float:
        self._validate_type(other)
        return self.x * other.x + self.y * other.y

    def __eq__(self, other) -> bool:
        return self._match_type_and_execute(
            other=other,
            function=lambda: self.x == other.x and self.y == other.y
        )

    def _validate_type(self, other):
        if not isinstance(other, Vector2d):
            raise ValueError()

    def _match_type_and_execute(self, other, function: Callable):
        match other:
            case Vector2d():
                return function()
            case _:
                raise ValueError()

