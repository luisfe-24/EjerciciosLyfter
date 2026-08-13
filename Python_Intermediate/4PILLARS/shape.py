import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter

    def calculate_area(self):
        area = math.pi * pow(self.radius, 2)
        return area


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def calculate_perimeter(self):
        perimeter = 4 * self.side
        return perimeter

    def calculate_area(self):
        area = pow(self.side, 2)
        return area


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_perimeter(self):
        perimeter = 2 * (self.length + self.width)
        return perimeter

    def calculate_area(self):
        area = self.length * self.width
        return area


mi_circulo = Circle(2)

print(mi_circulo.calculate_perimeter())

print(mi_circulo.calculate_area())

mi_cuadrado = Square(2)

print(mi_cuadrado.calculate_perimeter())

print(mi_cuadrado.calculate_area())

mi_rectangulo = Rectangle(2, 4)

print(mi_rectangulo.calculate_perimeter())

print(mi_rectangulo.calculate_area())
