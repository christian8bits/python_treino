import pandas as pd
df = pd.read_csv('movies_metadata.csv')
small_df = df[['title', 'runtime']]
result = small_df[(small_df['runtime'] >= 30) & (small_df['runtime'] <= 360)]
print("List of movies longer than 30 minutes and shorter than 360 minutes:")
print(result)
