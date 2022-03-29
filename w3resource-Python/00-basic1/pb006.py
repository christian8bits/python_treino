'''
6. Escreva um programa em Python que aceite uma sequência de números separados por vírgulas do usuário e gere uma lista e uma tupla com esses números.
Dados de amostra: 3, 5, 7, 23
Saída :
Lista: ['3', '5', '7', '23']
Tupla: ('3', '5', '7', '23')
'''
valor = input('Entre com varios numeros separados por virgula (,): ')
list = valor.split(',')
tuple = tuple(list)
print(f'Lista: {list}')
print(f'Tupla: {tuple}')
