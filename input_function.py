def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
def c(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))
a=10

for i in range(0, a):
    for t in range(0, i+1):
        print(c(a, t), end=' ')
    print("\n")