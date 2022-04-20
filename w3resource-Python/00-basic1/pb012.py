'''
12. Escreva um programa em Python para imprimir o 
calendário de um determinado mês e ano.
Nota: Use o módulo 'calendário'.
'''
import calendar
a = int(input('Entre com o ano: '))
m = int(input('Entre com o mês: '))
print('\n')
print(calendar.month(a,m))
