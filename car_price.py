t = 0
r = True
def price(n):
    match n:
        case 'd':
            return 10
        case 'm':
            return 100
        case 'l':
            return 1000
        case _:
            return 0
while r:
    n = input().lower()
    p = price(n)
    if p == 0:
        r = False
    else:
        t = t + p
        print(t)
print(t)
