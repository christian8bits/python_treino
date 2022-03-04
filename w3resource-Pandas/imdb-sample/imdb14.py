import pandas as pd
df = pd.read_csv('movies_metadata.csv')
small_df = df[['title', 'release_date', 'budget', 'revenue', 'runtime']]
result = small_df[(small_df['revenue'] > 2000000) & (small_df['budget'] < 1000000)]
print("Movies, revenue more than 2 million and spent less than 1 million:")
print(result.head())
