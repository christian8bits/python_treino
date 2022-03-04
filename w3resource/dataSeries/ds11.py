import pandas as pd
s = pd.Series(['100', '200', 'python', '300.12', '400'])
print(f'Data Serie Original\n{s}')
new_s = pd.Series(s).sort_values()
print(f'Data Serie Ordenada\n{new_s}')
