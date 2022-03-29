'''
23. Escreva um programa em Python para obter as n (inteiros não negativos) cópias dos 2 primeiros caracteres de uma determinada string. Retorne as n cópias de toda a string se o comprimento for menor que 2.
'''
def substring_copia(str, n):
  trecho = 2
  if  trecho > len(str):
    trecho = len(str)
  subtexto = str[:trecho]

  resultado = "" 
  for i in range(n):
    resultado = resultado + subtexto
  return resultado

print(substring_copia('abcdefgh', 2))
print(substring_copia('H', 3))
