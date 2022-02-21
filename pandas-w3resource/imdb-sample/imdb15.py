import pandas as pd
df = pd.read_csv('movies_metadata.csv')
result = df['vote_count'].quantile(0.70)
print(result)
