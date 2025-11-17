names = []
for i in range(10):
    n = input('enter a name: ')
    names.append(n)
names.sort()
n = 1
for name in names:
    print(name + '-' + f'student {n}')
    n += 1