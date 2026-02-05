import numpy as np
def convert(a):
    row_sum = a.sum(axis=1, keepdims=True)
    return a / row_sum
print(convert(np.arange(0,9).reshape(3,3)))
# [[0, 1, 2], [3, 4, 5],[6, 7, 8]]
