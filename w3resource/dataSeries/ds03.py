import pandas as pd
ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 9])
print(f'Adiciona duas Series:\n{ds1 + ds2}')
print(f'Subtrai duas series:\n{ds1 - ds2}')
print(f'Multiplica duas Series:\n{ds1 * ds2}')
print(f'Divide Series1 pela Series2:\n{ds1 / ds2}')
