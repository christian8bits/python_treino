'''
22. Escreva um programa em Python para contar o número 4 em uma determinada lista.
'''
def contar4_lista(lista):
  contador = 0
  for n in lista:
    if n == 4:
      contador = contador + 1
  return contador

lista1 = [1, 3, 4, 5, 6, 4]
lista2 = [4, 6, 9, 7, 4, 3, 6, 4, 8 ]
print(contar4_lista(lista1))
print(contar4_lista(lista2))
