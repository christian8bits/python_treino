import pandas as pd
df = pd.read_csv('movies_metadata.csv')
result = df.iloc[4]
print("Details of the fifth movie of the DataFrame:")
print(result)

