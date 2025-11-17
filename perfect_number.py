n = int(input('enter: '))
sum = 0
l = []
for i in range(1, n):
    if n % i == 0:
        sum += i
        l.append(i)
if n == sum:
    print('perfect number')
    print('list is : ', *l)
else:
    print('not perfect number')