import pandas as pd
df = pd.read_csv('movies_metadata.csv')
result = df.shape
print("Numero de linhas e colunas do dataframe:")
print(result)

