import numpy as np
def system_solver(a):
    r,c = a.shape
    A = a[:, :r]
    b = a[:, r]
    x = np.linalg.solve(A,b)
    return x.reshape(-1,1)
a = np.array([[1, 3, -2, 5],
	      [3, 5, 6, 7],
	      [2, 4, 3, 8]])
print(system_solver(a))