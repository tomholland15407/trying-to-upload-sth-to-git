import numpy as np
from sklearn.linear_model import LinearRegression

class BaseClassRegressionAnalysis():
    def __init__(self):
        # Initialize a regressor, which will handle the LinearRegression model
        self.regressor = LinearRegression()

    def fit(self, X, y):
        # The regressor learn from the training data with input X and output y
        self.regressor.fit(X, y)

    def predict(self, X):
        # The regressor predict the result with input X (after being trained)
        # The output has the same size as output y
        return self.regressor.predict(X)

    def mean_square_error(self, y_real, y_predict):
        # Compare the 2 output vectors: real output and prediction, using mean square error
        return np.mean((y_real - y_predict) ** 2)

model = BaseClassRegressionAnalysis()
y_real = np.array([1, 0, 1, 0, 1])
y_pred = np.array([2, 1, 0, 1, 2])
print(model.mean_square_error(y_real, y_pred))