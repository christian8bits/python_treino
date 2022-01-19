# leia um numero e mostre a tabuada
n = int(input('Digite um numero para exibir sua tabuada: '))

  
#  SOLUCAO SEM LOOP
print('{} x {} = {}'.format(n, 1, 1 * n))
print('{} x {} = {}'.format(n, 2, 2 * n)) 
print('{} x {} = {}'.format(n, 3, 3 * n)) 
print('{} x {} = {}'.format(n, 4, 4 * n)) 
print('{} x {} = {}'.format(n, 5, 5 * n))
print('{} x {} = {}'.format(n, 6, 6 * n)) 
print('{} x {} = {}'.format(n, 7, 7 * n)) 
print('{} x {} = {}'.format(n, 8, 8 * n)) 
print('{} x {} = {}'.format(n, 9, 9 * n))
print('{} x {} = {}'.format(n, 10, 10 * n)) 


''' 
# SOLUCAO COM LOOP
i = 1
while i <=10:
  print('{} x {} = {}'.format(n, i, i * n))
  i = i + 1
'''  
  
print('FIM')
