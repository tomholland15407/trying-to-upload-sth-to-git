import numpy as np
# Write a function to convert the numpy matrix into percentage matrix: each element in a line is converted into its percentage of the sum of elements in that line (no need for rounding)
#
# Example:
#
# Input
#
# [[0, 1, 2],
#  [3, 4, 5],
#  [6, 7, 8]]
t = [[0, 1, 2],[3, 4, 5],[6, 7, 8]]
# Output
#
# [[0.        , 0.33333333, 0.66666667],
#  [0.25      , 0.33333333, 0.41666667],
#  [0.28571429, 0.33333333, 0.38095238]]
def convert(a):
    for i in range(a.shape[0]):
        m = a[i].sum()
        for j in range(a.shape[1]):
            a[i, j] = a[i, j] / m

    return a

a = np.array(eval(input()), dtype=float)
print(convert(a))