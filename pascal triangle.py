def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
def combination(a,b):
    return fact(a)//(fact(a-b)*fact(b))
n = int(input('enter a number: '))
for i in range(n):
    print('  '*(n-i), end='')
    for j in range(i+1):
        t = combination(i,j)
        print(f'{t:3}', end=' ')
    print()