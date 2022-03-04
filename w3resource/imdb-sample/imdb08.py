import pandas as pd
df = pd.read_csv('movies_metadata.csv')
# Criand oum smaller dataframe
small_df = df[['title', 'release_date', 'budget', 'revenue', 'runtime']]
print("Smaller DataFrame:")
print(small_df.head())
