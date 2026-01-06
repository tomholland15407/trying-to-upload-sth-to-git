import numpy as np
# Exercise 1
# Generate the numpy matrix in the fastest way possible, using np.arange(). Note: do not manually write down each element, and the solution should not exceed two lines
#
# [[ 1  6 11 16  2]
#  [ 7 12 17  3  8]
#  [13 18  4  9 14]
#  [19  5 10 15 20]]


print(np.transpose(np.arange(1,21).reshape(4, 5)).flatten().reshape(4,5))

