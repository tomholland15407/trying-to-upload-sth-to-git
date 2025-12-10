t = list(map(str, input().split()))
n = int(input())
l = []
for i in range(1, n+1):
    for j in t:
        a = str(i) + j
        l.append(a)
print(l)
