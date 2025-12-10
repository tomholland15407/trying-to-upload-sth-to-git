def fibfast(n, d = {1:0, 2:1}):
    if n in d:
        return d[n]
    d[n] = fibfast(n-1, d) + fibfast(n-2, d)
    return d[n]

print(fibfast(5))
