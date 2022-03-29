'''
18. Escreva um programa em Python para calcular a soma de três números dados, se os valores forem iguais, então retorne três vezes a soma.
'''
def soma_tres(x, y, z):
  soma = x + y + z
  if x == y == z:
    soma = soma * 3
  return soma

print(soma_tres(1, 2, 3))
print(soma_tres(3, 3, 3))
