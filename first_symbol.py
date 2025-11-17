n = list(input('enter a string: '))
t = n[0]
for i,s in enumerate(n):
    if s == t:
        n[i] = '$'
print(''.join(n))


