class Fraction:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return str(self.x) + '/' + str(self.y)
    def __add__(self, other):
        return Fraction(self.x * other.y + self.y * other.x, self.y * other.y)
    def __sub__(self, other):
        return Fraction(self.x * other.y - self.y * other.x, self.y * other.y)
    def __mul__(self, other):
        return Fraction(self.x * other.x, self.y * other.y)
    def inverse(self):
        return Fraction(self.y, self.x)
    def __float__(self):
        return self.x / self.y

f1 = Fraction(1,2)
print(f1)
f2 = Fraction(2,3)
print(f2)
print(f1 + f2)
print(f1 - f2)
print(f1 * f2)
print(f1.inverse())
print(float(f1))

