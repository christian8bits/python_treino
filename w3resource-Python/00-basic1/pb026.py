'''
26. Escreva um programa em Python para criar um histograma a partir de uma determinada lista de inteiros.
'''
def histograma(itens):
  for n in  itens:
    saida = ''
    quantidade = n
    while(quantidade > 0 ):
      saida +='@'
      quantidade = quantidade -1
    print(saida)

lista = [3,5,7, 9, 11]
histograma(lista)
