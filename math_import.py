import math
t = list(map(int,input("Enter some numbers: ").split()))

def f(x):
    if x < 0:
        a = x**2*4.5
        b = x**3-1
        return math.cos(a) + 5*math.sin(b)
    if x == 0:
        return 7
    if x > 0:
        return math.log(x, 2) + (x**2+5)**(1/2)

print(f'{'x':>10} {'f(x)':>10}')
print('-'*30)

for x in t:
    y = f(x)
    print(f'{x:>10} {y:>10.2f}')