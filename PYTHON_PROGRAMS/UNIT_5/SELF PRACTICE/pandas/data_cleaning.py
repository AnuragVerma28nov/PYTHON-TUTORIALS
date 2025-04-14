# data cleaning

import pandas as pd
import numpy as np

df = pd.DataFrame({
'A': [1, 2,np.nan, 4],
'B': [np.nan, 'b', 'c', 'd'],
'C': [4.5, np.nan, 6.5, 7.5]
})#Creating a DataFrame with missing values

missing_values = df.isna() #Detecting missing values
print(missing_values)

filled_df = df.fillna(0.2) # Filling missing values with a specific value
print(filled_df)

tranformed_df=df.apply(lambda x:x*2)
print(tranformed_df)