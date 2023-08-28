from collections import abc
# from typing import Sequence
from typing import Self


class VectorND:
    def __init__(self, xs: abc.Sequence[float]):
        self.xs: tuple[float, ...] = tuple(xs)

    def __eq__(self, other) -> bool:
        if isinstance(other, VectorND):
            if len(self.xs) != len(other.xs):
                return False
            for x1, x2 in zip(self.xs, other.xs):
                if x1 != x2:
                    return False
            return True
        else:
            return False

    def __str__(self) -> str:
        return f"{self.xs}"

    def __repr__(self) -> str:
        return f"{type(self).__name__}{self.xs}"


class Vector2D(VectorND):
    def __init__(self, x: float, y: float):
        super().__init__([x, y])

    @property
    def x(self) -> float:
        return self.xs[0]

    @property
    def y(self) -> float:
        return self.xs[1]

    @property
    def length(self) -> float:
        return (self.x**2 + self.y**2) ** 0.5

    def __matmul__(self, other) -> float:
        if isinstance(other, Vector2D):
            return self.x * other.x + self.y * other.y
        else:
            raise ValueError(
                f"you cannot multiply a vector with {type(other)}"
            )

    def __mul__(self, other) -> Self:
        if isinstance(other, Vector2D):
            return Vector2D(self.x * other.x, self.y * other.y)
        else:
            raise ValueError(
                f"you cannot multiply a vector with {type(other)}"
            )

    def __add__(self, other) -> Self:
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        else:
            raise ValueError(f"you cannot add a vector to {type(other)}")


if __name__ == "__main__":
    v1 = Vector2D(1, 1)
    v2 = Vector2D(0, 0)

    assert v1 + v2 == Vector2D(1, 1)
    assert v1 * v2 == Vector2D(0, 0)
    print(v1 + v2)
    assert v1 @ v2 == 0

    vectors: list[Vector2D] = [Vector2D(i, i) for i in range(10)]
    print(vectors)
    print(list(filter(lambda v: v.length >= 2, vectors)))
