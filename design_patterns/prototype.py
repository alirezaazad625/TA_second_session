class Circle:

    def __init__(self, radius: int):
        self.radius = radius

    def clone(self) -> 'Circle':
        return Circle(radius=self.radius)
