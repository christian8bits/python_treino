'''
Leia os quatro valores correspondentes a
p1(x1,y1) e p2(x2,y2).
Calcule a distância entre eles, mostrando 
14 casas decimais após a vírgula.
'''

val1=input().split()
x1=float(val1[0])
y1=float(val1[1])

val2=input().split()
x2=float(val2[0])
y2=float(val2[1])

Distancia=((x2-x1)**2 + (y2-y1)**2)**(0.5)
print("%.4f" %Distancia)
