import pandas as pd
df = pd.read_csv('movies_metadata.csv')
# Criando um dataframe small
small_df = df[['title', 'release_date', 'budget', 'revenue', 'runtime']]
result = small_df.sort_values('release_date')
print("DataFrame pela data de lançamento.")
print(result)
