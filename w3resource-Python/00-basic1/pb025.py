'''
25. Escreva um programa Python para verificar se um valor especificado está contido em um grupo de valores.
Dados de teste :
3 -> [1, 5, 8, 3] : Verdadeiro
-1 -> [1, 5, 8, 3] : Falso
'''
def membro_grupo(grupo, n):
  for valor in grupo:
    if n == valor:
      return True
  return False

lista1 = [1, 2, 54, 6, 2, 3, 5, 8]
lista2 = [7, 3, 1, 4, 32]
print(membro_grupo(lista1, 3))
print(membro_grupo(lista2, -2))
