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
