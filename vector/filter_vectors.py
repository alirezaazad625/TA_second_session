from vector.vector_2d import Vector2d

vectors: list[Vector2d] = [
    Vector2d(1, 2),
    Vector2d(1, 0),
    Vector2d(1, 1),
    Vector2d(1, 4),
    Vector2d(3, 1),
    Vector2d(1, 1),
    Vector2d(0, 0)
]

vectors = list(filter(lambda x: x.length >= 2, vectors))
