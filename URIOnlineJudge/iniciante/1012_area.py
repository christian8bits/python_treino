'''
Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
    a) a área do triângulo retângulo que tem A por base e C por altura.
    b) a área do círculo de raio C. (pi = 3.14159)
    c) a área do trapézio que tem A e B por bases e C por altura.
    d) a área do quadrado que tem lado B.
    e) a área do retângulo que tem lados A e B. .
'''

val=input().split()

A=float(val[0])
B=float(val[1])
C=float(val[2])

tri=(A*C)/2
circ=3.14159*C**2
trap=((A+B)*C)/2
quad=B*B
ret=A*B

print("TRIANGULO: %.3f" %tri)
print("CIRCULO: %.3f" %circ)
print("TRAPEZIO: %.3f" %trap)
print("QUADRADO: %.3f" %quad)
print("RETANGULO: %.3f" %ret)
