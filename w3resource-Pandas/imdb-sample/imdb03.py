import pandas as pd
df = pd.read_csv('movies_metadata.csv')
terceiro_filme = df.iloc[2]
print('Detalhes do Terceiro filme:')
print(terceiro_filme)

