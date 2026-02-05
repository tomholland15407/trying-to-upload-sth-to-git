import numpy as np
y_real = np.array([1, 2])
y_predict = np.array([2, 3])

print(np.mean((y_real - y_predict) ** 2))