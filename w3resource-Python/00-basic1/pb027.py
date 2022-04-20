'''
27. Escreva um programa Python para concatenar 
todos os elementos de uma lista em uma string e devolvê-la.
'''
def concatenar_lista(list):
  resultado = ''
  for e in list:
    resultado += str(e)
  return resultado

lista =  [1, 3, 5, 22, 6]
print(concatenar_lista(lista))
