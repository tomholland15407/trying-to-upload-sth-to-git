from class_geometry import Rectangle
class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side
    def set_width(self, width):
        self.width = width
        self.height = width
    def set_height(self, height):
        self.width = height
        self.height = height

if __name__ == '__main__':
    s = Square(4)
    s.set_height(5)
    print(s.area())