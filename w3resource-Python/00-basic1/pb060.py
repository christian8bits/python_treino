# 60. Escreva um programa em Python para calcular a hipotenusa de um triângulo retângulo.
from math import sqrt
print("Entre com os lados de um triângulo retângulo:")
a = float(input("lado a: "))
b = float(input("lado b: "))
c = sqrt(a**2 + b**2)
print("A hipotenusa é:", c )

