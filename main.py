import pandas as pd

df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=[0, 1])
df2 = pd.DataFrame({'A': [5, 6], 'C': [7, 8]}, index=[1, 2])

aligned_df1, aligned_df2 = df1.align(df2, join='left')

print(aligned_df1)
print(aligned_df2)

print(df1.merge(df2, how = 'left'))