def pascal(r,c):
    if c == 1 or c == r:
        return 1
    else:
        return pascal(r-1,c-1) + pascal(r-1,c)
def display_pascal_triangle(n):
    for i in range(1,n+1):
        print(' '*(n-i), end='')
        for j in range(1,i+1):
            print(pascal(i,j), end=' ')
        print()