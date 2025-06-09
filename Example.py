import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Create sample data
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 4, 5])

# Create a LinearRegression model
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Make predictions
y_pred = model.predict(X)

print(model.coef_)

# Plot the data and the regression line
plt.scatter(X, y, color='blue')
plt.plot(X, y_pred, color='red')
plt.title('Linear Regression Example')
plt.xlabel('X')
plt.ylabel('y')
plt.show()