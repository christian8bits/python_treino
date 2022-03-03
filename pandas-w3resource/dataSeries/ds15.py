import pandas as pd
s = pd.Series(data = [1,2,3,4,5,6,7,8,9,5,3])
print('Data Series Original:')
print(s)
print('Média da Série de Dados:')
print(s.mean())
print('Desvio padrão da Série de Dados:')
print(s.std())
