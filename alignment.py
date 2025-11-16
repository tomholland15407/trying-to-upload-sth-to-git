c = 'H'
thickness = int(input('enter a number: '))
for i in range(thickness):
    print((c*i).rjust(thickness-1) + c + (c*i).ljust(thickness-1))

x,y = map(int, input('enter x,y: ').split(' '))
def print_line(x,y):
    return [('.|.' * (2*i + 1)).center(y, '-') for i in range(x)]
list = print_line(x,y)
print('\n'.join(list))