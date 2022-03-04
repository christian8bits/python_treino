import pandas as pd
df = pd.read_csv('movies_metadata.csv')
#Set the index to the title
df = df.set_index('title')
#Details of the movie 'Grumpier Old Men'
result = df.loc['Grumpier Old Men']
print("Details of the movie 'Grumpier Old Men:")
print(result)
