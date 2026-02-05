from trig import *
import math
n = int(input())
result = 0
math_result = 0
for i in range(n+1,n+21):
    if (i-n) % 2 == 1:
        result += sin(i)
    else:
        result += cos(i)
print('Your own implementation:    ', round(result,6))
for i in range(n+1,n+21):
    if (i-n) % 2 == 1:
        math_result += math.sin(i)
    else:
        math_result += math.cos(i)
print('Math module implementation: ', round(math_result,6))
