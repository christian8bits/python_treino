import pandas as pd
s = pd.Series([
    ['Red', 'Green', 'White'],
    ['Red', 'Black'],
    ['Yellow']])
print('Serie Original com lista')
print(s)
s = s.apply(pd.Series).stack().reset_index(drop=True)
print('Apenas uma Serie')
print(s)
