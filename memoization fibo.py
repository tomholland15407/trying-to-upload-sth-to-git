def fib_fast(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_fast(n-1, d) + fib_fast(n-2, d)
        d[n] = ans
        print(n, ans)
    return ans
d = {1:1, 2:2}
print(fib_fast(4, d))