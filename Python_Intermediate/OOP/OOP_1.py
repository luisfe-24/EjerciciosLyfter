import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = math.pi * (self.radius ** 2)
        return area


circle1 = Circle(5)

circle2 = Circle(10)

print(circle2.get_area())
