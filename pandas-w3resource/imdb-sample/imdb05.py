import pandas as pd
df = pd.read_csv('movies_metadata.csv')
result = df[['title', 'genres']]
print("Detalhes dos titulos e gêneros:")
print(result)
