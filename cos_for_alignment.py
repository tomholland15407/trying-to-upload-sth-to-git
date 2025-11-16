from math import sqrt

ax, ay, bx, by, cx, cy = [float(i) for i in input().split()]
EPS = 1e-9

ab1, ab2 = bx - ax, by - ay
ac1, ac2 = cx - ax, cy - ay
bc1, bc2 = cx - bx, cy - by

ab = sqrt(ab1**2 + ab2**2)
ac = sqrt(ac1**2 + ac2**2)
bc = sqrt(bc1**2 + bc2**2)

# Check for collinearity using cross product
area = abs(ab1 * ac2 - ab2 * ac1)
if area < EPS:
    print('line')
else:
    a = (ab1 * ac1 + ab2 * ac2) / (ab * ac)
    b = ((-ab1) * bc1 + (-ab2) * bc2) / (ab * bc)
    c = (bc1 * ac1 + bc2 * ac2) / (bc * ac)

    if abs(a) < EPS or abs(b) < EPS or abs(c) < EPS:
        print('right')
    elif a < 0 or b < 0 or c < 0:
        print('obtuse')
    else:
        print('acute')