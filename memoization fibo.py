def fibfast(n, d = {1:0, 2:1}):
    if n in d:
        return d[n]
    d[n] = fibfast(n-1, d) + fibfast(n-2, d)
    return d[n]

list = []
for i in range(1,100):
    list.append(fibfast(i))
print(list)