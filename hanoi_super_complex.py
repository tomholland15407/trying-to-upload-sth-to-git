def hanoi(n,a,b,c):
    if n == 1:
        print(f'move 1 from {a} to {b}')
    else:
        hanoi(n - 1, a, c, b)
        print(f'move {n} from {a} to {b}')
        hanoi(n - 1, c, b, a)
n = int(input('enter the number of discs: '))
hanoi(n, 'a', 'b', 'c')