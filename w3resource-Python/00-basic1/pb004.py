'''
4. Escreva um programa Python que aceite o raio de um círculo do usuário e calcule a área.
Saída de amostra:
r = 1,1
Área = 3,8013271108436504
'''
from math import pi
r = float(input('Entre com o raio do circulo: '))
print(f'Com o raio {r} a area do circulo é {pi * r**2}')
