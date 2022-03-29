'''
17. Escreva um programa em Python para testar se um número está dentro de 100 de 1000 ou 2000.
'''
def proximo_mil(n):
  return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
  
print(proximo_mil(1000))
print(proximo_mil(900))
print(proximo_mil(800))   
print(proximo_mil(2200))
