import pandas as pd
s1 = pd.Series(['100', '200', 'python', '300.12', '400'])
print('Data Serie original: ')
print(s1)
print('Mudar para tipo numerico e filtrar erros')
s2 = pd.to_numeric(s1, errors='coerce')
print(s2)
