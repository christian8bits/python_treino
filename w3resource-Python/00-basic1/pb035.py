'''
35. Escreva um programa Python que retornará true se os dois valores inteiros fornecidos forem iguais ou sua soma ou diferença for 5.
'''
def igual_diferenca5(x, y):
  if x==y or abs(x-y)==5 or (x+y)==5:
    return True
  else:
    return False

print(igual_diferenca5(7, 2))
print(igual_diferenca5(3, 2))
print(igual_diferenca5(2, 2))
print(igual_diferenca5(7, 3))
print(igual_diferenca5(27, 53))
