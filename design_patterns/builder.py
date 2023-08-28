class House:
    _windows = 4
    _doors = 1
    _height = 3.5
    _color = "WHITE"

    @property
    def windows(self) -> int:
        return self._windows

    @property
    def doors(self) -> int:
        return self._doors

    @property
    def height(self) -> float:
        return self._height

    @property
    def color(self) -> str:
        return self._color


class HouseBuilder:

    def __init__(self):
        self._house = House()

    def doors(self, doors: int) -> 'HouseBuilder':
        self._house._doors = doors
        return self

    def windows(self, windows: int) -> 'HouseBuilder':
        self._house._windows = windows
        return self

    def height(self, height: float) -> 'HouseBuilder':
        self._house._height = height
        return self

    def color(self, color: str) -> 'HouseBuilder':
        self._house._color = color
        return self

    def build(self) -> House:
        return self._house
