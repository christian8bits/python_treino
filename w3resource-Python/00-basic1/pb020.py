'''
20. Escreva um programa em Python para obter uma string que seja n (inteiro não negativo) cópias de uma determinada string.
'''
def larger_string(str, n):
   result = ""
   for i in range(n):
      result = result + str
   return result

print(larger_string('abc', 2))
print(larger_string('.py', 3))
