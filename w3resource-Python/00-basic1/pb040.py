'''
40. Escreva um programa em Python para calcular a 
distância entre os pontos (x1, y1) e (x2, y2).
'''
import math
p1 = [4, 0]
p2 = [6, 6]
distancia = math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))
print(distancia)
