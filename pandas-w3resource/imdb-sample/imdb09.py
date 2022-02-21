import pandas as pd
df = pd.read_csv('movies_metadata.csv')
# Mostrar as 10 primeiras linhas
result = df.head(10)
print("As primeiras 10 linhas do dataframe")
print(result)
