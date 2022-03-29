'''
14. Escreva um programa Python para calcular o número de dias entre duas datas.
Datas de amostra: (2014, 7, 2), (2014, 7, 11)
Produção esperada: 9 dias
'''
from datetime import date
f_date = date(2022, 7, 2)
l_date = date(2022, 7, 11)
delta = l_date - f_date
print(delta.days)
