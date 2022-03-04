import pandas as pd
df = pd.read_csv('movies_metadata.csv')
small_df = df[['title', 'release_date', 'budget', 'revenue', 'runtime']]
# Ordernar por lançamento em ordem decrescente
result = small_df.sort_values('runtime', ascending=False)
print("DataFrame  Ordem de lançamento.")
print(result.head())
