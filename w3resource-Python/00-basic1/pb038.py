'''
38. Escreva um programa em Python para resolver (x + y) * (x + y).
Dados de teste: x = 4, y = 3
Saída Esperada: (4 + 3) ^ 2) = 49
'''
x, y = 4, 3
resultado = x * x + 2 * x * y + y * y
print('({} + {}) ^ 2) = {}'.format(x, y, resultado))
