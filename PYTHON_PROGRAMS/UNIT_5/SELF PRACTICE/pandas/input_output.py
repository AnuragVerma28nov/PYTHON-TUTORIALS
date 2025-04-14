# input-output

import pandas as pd

df_csv = pd.read_csv('sample.csv') #Reading data from a CSV file
print(df_csv)

df_excel = pd.read_excel('sample.xlsx') #Reading data from an Excel file
print(df_excel)

df = pd.DataFrame({
'Name': ['Alice', 'Bob', 'Carol'],
'Age': [24, 30, 28],
'City': ['New York', 'Los Angeles', 'Chicago']
}) #Creating a DataFrame

df.to_csv('output.csv', index=False) # Writing data to a CSV file
