import pandas as pd
s = pd.Series([0, 1,2,3,4,5,6,7,8,9,10])
print("Data Series Original:")
print(s)
print("\nSubconjunto da Série de Dados:")
n = 6
new_s = s[s < n]
print(new_s)
