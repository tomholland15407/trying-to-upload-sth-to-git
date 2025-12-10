def sth(t, i=1):
    if i == t:
        return str(t)
    else:

        return str(i) + str(sth(t, i+1))
def sthmore(t):
    if t == 1:
        return str(t)
    if t == 0:
        return ''
    else:
        return str(t) + str(sthmore(t-1))
t = int(input('enter t: '))
for i in range(1,t+1):
    print(' '*(t-i)+sth(i)+sthmore(i-1))