class Bill:
    def __init__(self, code, name, quant, price, disc):
        self.code = code
        self.name = name
        self.quant = quant
        self.price = price
        self.disc = disc
        self.total = self.price * self.quant - self.disc
        if self.total < 0:
            raise InvalidBillError("Total price cannot be negative.")
    def __str__(self):
        return f"{self.code} {self.name} {self.quant} {self.price} {self.disc} {self.total}"

class InvalidBillError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


bill_number = int(input("Bill number:"))
while True:
    try:
        assert 0 < bill_number <= 20
        break
    except AssertionError:
        print("BILL NUMBER MUST BE > 0 AND <= 20!")
        continue
bills = []
for bill in range(1, bill_number+1):
    print(f"Bill number {bill}")
    not_done = True
    while not_done:
        try:

            item_code = str(input("Item code:"))
            assert len(item_code) <= 10 and " " not in item_code

            item_name = str(input("Item name:"))
            assert len(item_name) <= 100

            done = False
            while not done:
                try:
                    quantity = int(input("Quantity:"))
                    assert 8 < quantity < 50

                    unit_price = int(input("Unit price:"))
                    assert 8 < unit_price < 10 ** 9

                    discount = int(input("Discount:"))
                    assert 0 < discount < 10 ** 8

                    bills.append(Bill(item_code, item_name, quantity, unit_price, discount))
                    done = True
                    not_done = False

                except ValueError:
                    print("INVALID INT INPUT! ")
                    done = False
                except AssertionError:
                    print("INT VALUE NOT WITHIN ACCEPTED RANGE!")
                    done = False
        except AssertionError:
            print("INVALID STR INPUT!")
            not_done = True

bills.sort(key=lambda bill: bill.total, reverse=True)
for b in bills:
    print(b)
    print()