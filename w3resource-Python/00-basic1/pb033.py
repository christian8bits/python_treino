def soma(x, y, z):
  if x==y or y==z or x==z:
    soma = 0
  else:
    soma = x + y + z
  return soma


  print(soma(2,1,2))
  print(soma(3, 2, 2))
  print(soma(1, 2, 4))
  print(soma(1, 2, 3))
