t = list(str(input()))
r = True
k = 1
while r:
    while len(t) < 4:
        t.append("0")
    t1 = ''.join(sorted(t))
    t2 = ''.join(sorted(t, reverse=True))
    e = int(t2) - int(t1)
    if e == 6174:
        print('6174, ok', k)
        r = False
    elif e == 0:
        print('not ok')
        r = False
    else:
        print(e)
        k = k + 1
        t = list(str(e))