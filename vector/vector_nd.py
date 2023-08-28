import math
from typing import Sized


class VectorNd(Sized):
    def __len__(self) -> int:
        return int(math.sqrt(sum([math.pow(dimension, 2) for dimension in self.dimensions])))

    @property
    def length(self) -> int:
        return len(self.dimensions)

    @property
    def dimensions_length(self) -> int:
        return len(self.dimensions)

    def _validate_type(self, other):
        if issubclass(type(other), type(VectorNd)):
            raise ValueError()

    def _validate_length(self, other: 'VectorNd'):
        if self.dimensions_length != other.dimensions_length:
            raise ValueError()

    def __eq__(self, other):
        self._validate_type(other)
        self._validate_length(other)
        for i in range(0, len(self.dimensions)):
            if self.dimensions[i] != other.dimensions[i]:
                return False

        return True

    def __add__(self, other) -> 'VectorNd':
        self._validate_type(other)
        self._validate_length(other)
        return VectorNd(*[self.dimensions[i] + other.dimensions[i] for i in range(0, len(self.dimensions))])

    def __sub__(self, other) -> 'VectorNd':
        self._validate_type(other)
        self._validate_length(other)

        return VectorNd(*[self.dimensions[i] - other.dimensions[i] for i in range(0, len(self.dimensions))])

    def __mul__(self, other) -> 'VectorNd':
        self._validate_type(other)
        self._validate_length(other)

        return VectorNd(*[self.dimensions[i] * other.dimensions[i] for i in range(0, len(self.dimensions))])

    def __truediv__(self, other):
        # raise NotImplementedError()
        pass

    def __matmul__(self, other) -> float:
        self._validate_type(other)
        self._validate_length(other)

        return sum([self.dimensions[i] * other.dimensions[i] for i in range(0, len(self.dimensions))])

    def __init__(self, *args):
        self.dimensions = []
        for arg in args:
            if not isinstance(arg, float) and not isinstance(arg, int):
                raise ValueError()
            self.dimensions.append(arg)


class Vector2d(VectorNd):
    def __init__(self, x, y):
        super().__init__(x, y)


if __name__ == '__main__':
    print(Vector2d(1, 2) == Vector2d(1, 2))
