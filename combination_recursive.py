def c(m,n):
    if n == 0 or n == m:
        return 1
    else:
        return c(m-1,n-1) + c(m-1,n)
print(c(10,3))