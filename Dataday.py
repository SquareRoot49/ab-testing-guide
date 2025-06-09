import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def linear_regression(data):
    data['x_row_num'] = data['x_row_num'].apply(lambda x: x ** 2)
    X = pd.DataFrame(data['x_row_num'])
    y = pd.DataFrame(data['y_close'])

    print(X)
    print(y)
    model = LinearRegression()
    model.fit(X, y)

    #from sklearn.metrics import mean_squared_error, r2_score

    #intercept = model.intercept_

    ts = model.coef_[0]

    return ts[0]



row = []
for i in range(len(Dataday['close'])):
    row.append(i)
rows = {'x_row_num': row}
column = []
for j in Dataday['close']:
    column.append(j)
columns = {'y_close': column}
my_data = pd.concat([pd.DataFrame(rows), pd.DataFrame(columns)], axis = 1)
my_data.dropna(inplace=True)
my_data = my_data.replace([np.inf, -np.inf], np.nan).dropna()

print(linear_regression(my_data))
