# - Problem: Move n disks from peg A to peg C, using peg B as helper.
# - Base case: If n=1, move the disk directly from A to C.
# - Recursive case:
# - Move n-1 disks from A to B (using C as helper).
# - Move the largest disk from A to C.
# - Move n-1 disks from B to C (using A as helper).

def hanoi(n,a,b,c):
    if n == 1:
        print(f'move disk from {a} to {c}')
    else:
        hanoi(n-1,a,c,b)
        hanoi(1,a,b,c)
        hanoi(n-1,b,a,c)

print(hanoi(3,'A','B','C'))