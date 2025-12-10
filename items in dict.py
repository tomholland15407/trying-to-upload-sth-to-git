d = {'c':3, 'b':1, 'a':2}
t = d.items()
a = sorted(t)
b = sorted(t, reverse=True)
print(a)
print(b)
l = []
for key, value in t:
    l.append((value,key))
c = sorted(l)
print(c)
print([(k,v) for v,k in sorted([(v,k) for k,v in d.items()])])

e = dict(zip(d.keys(), d.values()))
print(e == d)