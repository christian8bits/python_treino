import pandas as pd
df = pd.read_csv('movies_metadata.csv')
result = df.info()
print('Detalhes do dataframe')
print(result)
