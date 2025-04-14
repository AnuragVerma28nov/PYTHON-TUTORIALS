# data manipulation

import pandas as pd

df= pd.DataFrame({
'A': [1, 2, 3, 4],
'B': ['a', 'b', 'c', 'd'],
'C': [4.5, 5.5, 6.5, 7.5]
})

value = df. loc[0, 'A'] #Accessing a specific value
print(value)

selected_columns = df.loc[:, ['A', 'C']] # Selecting multiple columns
print(selected_columns)

selected_rows = df. loc[1:3, :] # Selecting a range of rows
print(selected_rows)

filtered_df = df [df['A'] > 2] # Filtering rows based on a condition
print(filtered_df)

filtered_df = df [(df['A'] > 1) & (df['C'] < 7)] #Filtering rows based on multiple conditions
print(filtered_df)