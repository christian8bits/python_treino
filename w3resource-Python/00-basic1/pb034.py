'''
34. Escreva um programa Python para a soma de dois inteiros dados. 
No entanto, se a soma estiver entre 15 e 20, retornará 20.
'''
def soma(x,y):
  resposta = x + y
  if resposta in range(15, 20):
    return 20
  else:
    return resposta


print(soma(12, 88))
print(soma(5, 13))
