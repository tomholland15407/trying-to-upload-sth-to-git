t = list(map(str, input().split()))
k = len(t)

def sublist(t,k):
    if k == 0:
        return []
    else:
        a = t[(k-1):]
        print(a)
        return str(a) + ' ' + str(sublist(t,k-1))

for i in range(k,0,-1):
    sublist(t,i)
    t.pop(i-1)

print([])