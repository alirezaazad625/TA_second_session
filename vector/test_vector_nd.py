import unittest

import pytest

from vector.vector_nd import Vector2d, VectorNd


@pytest.fixture
def first_vector():
    return Vector2d(x=10, y=-5)


@pytest.fixture
def first_vector_again():
    return Vector2d(x=10, y=-5)


@pytest.fixture
def second_vector():
    return Vector2d(x=5, y=8)


class TestStringMethods(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def prepare_fixtures(self, first_vector, second_vector, first_vector_again):
        self.first_vector = first_vector
        self.second_vector = second_vector
        self.first_vector_again = first_vector_again

    def test_equal(self):
        self.assertEqual(self.first_vector, self.first_vector_again)
        self.assertNotEqual(self.first_vector, self.second_vector)

    def test_multiply(self):
        self.assertEqual(
            self.first_vector * self.second_vector,
            Vector2d(50, -40)
        )

    def test_add(self):
        self.assertEqual(
            self.first_vector + self.second_vector,
            Vector2d(15, 3)
        )

    def test_subtract(self):
        self.assertEqual(
            self.first_vector - self.second_vector,
            Vector2d(5, -13)
        )

    def test_true_div(self):
        self.assertRaises(
            ValueError,
            lambda: VectorNd(1, 2) / VectorNd(2, 4)
        )
