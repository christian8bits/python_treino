import pandas as pd
sr1 = pd.Series([1, 2, 3, 4, 5])
sr2 = pd.Series([2, 4, 6, 8, 10])
print('Serie Original')
print(f'Serie 1:\n{sr1}')
print(f'Serie 2:\n{sr2}')
print('\n Items da Serie 1 que não estão na Serie 2:')
result = sr1[~sr1.isin(sr2)]
print(result)
