import pandas as pd
d1 = {'a': 100, 'b': 200, 'c':300, 'd':400, 'e':800}
print('Dicionario:')
print(d1)
serieConvertida = pd.Series(d1)
print('Convertido para series:')
print(serieConvertida)
