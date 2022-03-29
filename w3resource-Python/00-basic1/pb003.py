'''
3. Escreva um programa Python para exibir a data e hora atuais.
Saída de amostra:
Data e hora atuais:
2014-07-05 14:34:14
'''
import datetime
now = datetime.datetime.now()
print('Data e hora atual:')
print(now.strftime('%Y-%m-%d %H:%M:%S'))
