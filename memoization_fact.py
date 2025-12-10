def fact(n, memo={0:1,1:1}):
    if n in memo:
        return memo[n]
    memo[n] = n * fact(n-1, memo)
    return memo[n]
print(fact(2))
print(fact(3))
print(fact(4))
print(fact(5))
print(fact(6))


