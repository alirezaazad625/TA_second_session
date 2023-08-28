from vector.vector_2d import Vector2d


class TestStringMethods:
    def test_equal(self):
        # self.x == other.x and self.y == other.y
        first_vector = Vector2d(x=10, y=-5)
        second_vector = Vector2d(x=10, y=-5)
        third_vector = Vector2d(x=10, y=-4)

        assert first_vector == second_vector
        assert (first_vector == third_vector) is False

    def test_add(self):
        first_vector = Vector2d(x=10, y=-5)
        second_vector = Vector2d(x=1, y=8)
        result_vector = first_vector + second_vector

        assert result_vector.x == 11
        assert result_vector.y == 3

    def test_multiply(self):
        first_vector = Vector2d(x=10, y=-5)
        second_vector = Vector2d(x=2, y=8)
        result_vector = first_vector * second_vector

        assert result_vector.x == 20
        assert result_vector.y == -40

    def test_math_multiply(self):
        first_vector = Vector2d(x=10, y=-5)
        second_vector = Vector2d(x=2, y=8)
        result = first_vector @ second_vector

        assert result == -20

    def test_subtract(self):
        first_vector = Vector2d(x=10, y=-5)
        second_vector = Vector2d(x=2, y=8)
        result = first_vector - second_vector

        assert result.x == 8
        assert result.y == -13

    def test_true_div(self):
        first_vector = Vector2d(x=10, y=-5)
        second_vector = Vector2d(x=2, y=8)

        try:
            first_vector / second_vector
        except Exception as e:
            assert isinstance(e, NotImplementedError)
