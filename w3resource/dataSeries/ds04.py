import pandas as pd
ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 10])
print(f'Series1:\n{ds1}')
print(f'Series2:\n{ds2}')
print('Comparar os elementos das duas Series:')
print(f'Igual:\n{ds1 == ds2}')
print(f'Maior:\n{ds1 > ds2}')
print(f'Menor:\n{ds1 < ds2}')
