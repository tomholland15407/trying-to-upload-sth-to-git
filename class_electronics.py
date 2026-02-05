class Electronics:
    def __init__(self, code, name, quant, price, disc):
        self.code = code
        self.name = name
        self.quant = quant
        self.price = price
        self.disc = disc
        self.total = self.price * self.quant - self.disc
        if len(self.name) > 100 or len(self.code) > 10:
            raise LengthException
        if self.quant > 50 or len(str(self.price)) > 10 or len(str(self.disc)) > 9:
            raise ValueException

    def __str__(self):
        return f"{self.code} {self.name} {self.quant} {self.price} {self.disc} {self.total}"
class LengthException(Exception):
    pass
class ValueException(Exception):
    pass

n = int(input())
try:
    assert n <= 20
except AssertionError:
    raise InvalidBillError("Too many items.")
class InvalidBillError(Exception):
    pass
bills = []
for i in range(n):
    code = input()
    name = input()
    quant = int(input())
    price = int(input())
    disc = int(input())
    bills.append(Electronics(code, name, quant, price, disc))
bills.sort(key=lambda bill:bill.total, reverse = True)
for bill in bills:
    print(bill)
    print()