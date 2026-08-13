class Rectangle:
    def __init__(self, width, height):
        if width < 0 or height < 0:
            raise ValueError(
                "Existe un valor negativo, los valores deben ser positivos")

        self.width = width
        self.height = height

    def get_area(self):
        rectangle_area = self.width * self.height
        return rectangle_area

    def get_perimeter(self):
        rectangle_perimeter = 2 * (self.width + self.height)
        return rectangle_perimeter


height = int(input("Ingrese la altura: "))
width = int(input("Ingrese el ancho: "))

try:
    rectangle = Rectangle(width, height)
    print(rectangle.get_area())
    print(rectangle.get_perimeter())
except ValueError as error:
    print(error)
