import math
class Figure:
    def perimeter(self):
        pass
    def area(self):
        pass

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        if self.width <= 0 or self.height <= 0:
            raise LengthException
    def perimeter(self):
        return 2 * (self.width + self.height)
    def area(self):
        return self.width * self.height
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height
class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
        if self.radius <= 0:
            raise LengthException
    def perimeter(self):
        return 2 * math.pi * self.radius
    def area(self):
        return math.pi * self.radius ** 2
class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            raise LengthException
        elif self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            raise InvalidTriangleException
    def perimeter(self):
        return self.a + self.b + self.c
    def area(self):
        s = (self.a + self.b + self.c) * 0.5
        return (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
    def get_height_a(self):
        return self.area() * 2 / self.a
    def get_height_b(self):
        return self.area() * 2 / self.b
    def get_height_c(self):
        return self.area() * 2 / self.c

class LengthException(Exception):
    pass
class InvalidTriangleException(Exception):
    pass


if __name__ == '__main__':
    width, height = input('Enter width and height: ').split()
    width, height = int(width), int(height)
    try:
        rect = Rectangle(width,height)
        print(rect.perimeter())
        print(rect.area())
    except LengthException as e:
        print(e.__class__.__name__, 'was raised')
