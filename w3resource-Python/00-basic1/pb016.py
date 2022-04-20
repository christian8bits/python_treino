'''
16. Escreva um programa em Python para obter a diferença 
entre um determinado número e 17, se o número for maior que 17, 
retorne o dobro da diferença absoluta.
'''
def diferente(n):
  if n <= 17:
    return 17 - n
  else:
    return (n - 17) * 2 

print(diferente(22))
print(diferente(14))
