import unittest

from design_patterns.builder import HouseBuilder


class TestHouseBuilder(unittest.TestCase):

    def test_house_builder_color(self):
        color = "RED"
        house = HouseBuilder().color(color).build()
        self.assertEqual(house.color, color)

    def test_house_builder_height(self):
        height = 12.134
        house = HouseBuilder().height(height).build()
        self.assertEqual(house.height, height)

    def test_house_builder_doors(self):
        doors = 1
        house = HouseBuilder().doors(doors).build()
        self.assertEqual(house.doors, doors)

    def test_house_builder_windows(self):
        windows = 10
        house = HouseBuilder().windows(windows).build()
        self.assertEqual(house.windows, windows)

    def test_house_builder_all(self):
        color = "RED"
        height = 12.134
        doors = 3
        windows = 10
        house = HouseBuilder().windows(windows).height(height).doors(doors).color(color).build()
        self.assertEqual(house.windows, windows)
        self.assertEqual(house.height, height)
        self.assertEqual(house.doors, doors)
        self.assertEqual(house.color, color)
