import numpy as np

sample_size = 100
X = np.random.rand(sample_size, 1)
print(X)

measurement_error = np.random.normal(
    size=sample_size, scale=0.3).reshape(-1, 1)

print(measurement_error)
# Slope is 1, intercept is 0
Y = X + measurement_error
print(Y)
def ols_obj(beta, X, Y):
    interc, coeffs = beta[0], np.array(beta[1:])
    error = Y - interc - X.dot(coeffs.reshape(-1, 1))
    return np.sum(np.power(error, 2))