import unittest

from design_patterns.prototype import Circle


class TestCircle(unittest.TestCase):

    def test_clone(self):
        circle = Circle(radius=3)

        referenced_circle = circle

        referenced_circle.radius = 14

        self.assertEqual(referenced_circle.radius, circle.radius)

        cloned_circle = circle.clone()

        cloned_circle.width = 10

        self.assertEquals(cloned_circle.width, 10)

        self.assertEquals(circle.radius, 14)
