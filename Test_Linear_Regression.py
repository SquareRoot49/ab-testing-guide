import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

row = []
for i in range(len(Dataday['close'])):
    row.append(i)
rows = {'x_row_num': row}
column = []
for j in Dataday['close']:
    column.append(j)
columns = {'y_clos': column}
my_data = pd.concat([pd.DataFrame(rows), pd.DataFrame(columns)], axis = 1)
my_data.dropna(inplace=True)
my_data = my_data.replace([np.inf, -np.inf], np.nan).dropna()

def linear_regression(data):
    data['x_row_num'] = data['x_row_num'].apply(lambda x: x ** 2)
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

df = pd.DataFrame({'x_row_num': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                   'y_close': [76, 78, 85, 88, 72, 69, 94, 94, 88, 92, 90]})


model = LinearRegression()
X = pd.DataFrame(df['x_row_num'])
y = pd.DataFrame(df['y_close'])
model.fit(X, y)

df = pd.DataFrame({'x_row_num': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
                   'y_close': [76, 78, 85, 88, 72, 69, 94, 94, 88, 92, 90]})

print(df)

model = LinearRegression()
X = pd.DataFrame(df['x_row_num'])
y = pd.DataFrame(df['y_close'])
model.fit(X, y)

coefficients = pd.DataFrame(zip(X.columns, model.coef_))
print(coefficients)
print(coefficients.iloc[0][1][0])

print(linear_regression(df))
