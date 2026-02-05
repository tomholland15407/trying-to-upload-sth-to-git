def fact(n, memo=None):
    if memo is None:
        memo = {0:1, 1:1}
    if n in memo:
        return memo[n]
    memo[n] = n*fact(n-1, memo)
    return memo[n]
def exp(x):
    total = 0
    for i in range(50):
        total += (x**i)/fact(i)
    return round(total, 6)
def sin(x):
    total = 0
    for i in range(50):
        total += (-1)**i*(x**(2*i+1))/fact(2*i+1)
    return round(total, 6)
def cos(x):
    total = 0
    for i in range(50):
        total += (-1)**i*(x**(2*i))/fact(2*i)
    return round(total, 6)

pi = 0
for i in range(5000):
    pi += (-1)**i / (2*i+1)
pi = round(pi*4, 6)

