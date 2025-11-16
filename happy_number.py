t = str(input())
c = 0
e = 0
d = []
r = True
while r:
    for i in range(len(t)):
        e += int(t[i])**2

    if e == 1:
        print('happy')
        r = False
    elif e in d:
        print('unhappy')
        r = False
    else:
        d.append(e)
        t = str(e)
        e = 0
