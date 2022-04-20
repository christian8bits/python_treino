'''
21. Escreva um programa em Python para descobrir 
se um determinado número (aceito do usuário) é par ou ímpar, 
imprima uma mensagem apropriada para o usuário.
'''
num = int(input('Entre um numero: '))
mod = num % 2
if mod > 0:
  print('Numero impar')
else:
  print('Numero par')
