import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

#Data = pd.DataFrame({'close': [1, 2, 3, 4, 5]})

def get_target(items):
    row = []
    for i in range(len(items)):
        if i < (len(items) - 1):
            gap = items.iloc[i + 1] - items.iloc[i]
            ts = gap / items.iloc[i]
            row.append(ts)
    return row

#demo = pd.DataFrame({'dm': [1, 2, 3, 4, 5]})
#print(demo)
#get_target(demo['dm'])
#print(get_target(demo['dm']))

columns = {'y_close': get_target(Data['close'])}
row = []
for i in range(len(get_target(Data['close']))):
    row.append(i)
rows = {'x_row_num': row}

my_data = pd.concat([pd.DataFrame(rows), pd.DataFrame(columns)], axis = 1)
my_data.dropna(inplace=True)
my_data = my_data.replace([np.inf, -np.inf], np.nan).dropna()
#print(my_data)


def linear_regression(data):
    X = pd.DataFrame(data['x_row_num'])
    y = pd.DataFrame(data['y_close'])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X, y)

    prediction = model.predict(X_test)

    from sklearn.metrics import mean_squared_error, r2_score
    mse = mean_squared_error(y_test, prediction)
    r2 = r2_score(y_test, prediction)

    coefficients = pd.DataFrame(zip(X.columns, model.coef_))
    intercept = model.intercept_

    ts = coefficients.iloc[0][1][0]

    return ts

#print(linear_regression(my_data))


