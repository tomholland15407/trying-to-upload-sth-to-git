import math
class Figure:
    def perimeter(self):
        pass
    def area(self):
        pass

class Rectangle(Figure):
    def __init__(self, width, height):
        try:
            if width > 0 and height > 0:
                self.width = width
                self.height = height
            else:
                raise LengthException
        except LengthException as e:
            print(str(type(e)) + ' was raised')
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
        try:
            if radius > 0:
                self.radius = radius
            else:
                raise LengthException
        except LengthException as e:
            print(str(type(e)) + ' was raised')
    def perimeter(self):
        return 2 * math.pi * self.radius
    def area(self):
        return math.pi * self.radius ** 2
class Triangle(Figure):
    def __init__(self, a, b, c):
        try:
            if a <= 0 or b <= 0 or c <= 0:
                raise LengthException
            elif a + b <= c or a + c <= b or b + c <= a:
                raise InvalidTriangleException
            else:
                self.a = a
                self.b = b
                self.c = c
        except LengthException as e:
            print(str(type(e)) + ' was raised')
        except InvalidTriangleException as e:
            print(str(type(e)) + ' was raised')
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
    rec = Rectangle(-1, 2)
    tri = Triangle(3, 4,7)



