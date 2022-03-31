vl=input().split()
A=float(vl[0])
B=float(vl[1])
C=float(vl[2])
 
if B>A:
     aux=B;B=A;A=aux
if C>A:
     aux=C;C=A;A=aux
if C>B:
     aux=C;C=B;B=aux

if C>A:
     aux=C;C=A;A=aux
if B>A:
     aux=B;B=A;A=aux
if C>B:
     aux=C;C=B;B=aux
          
print("%.1f %.1f %.1f" %(A,B,C))

if A>=(B+C):
     print("NAO FORMA TRIANGULO")
elif A**2 > ((B**2) + (C**2)):
     print("TRIANGULO OBTUSANGULO")
if ((A**2)==(B**2+C**2)):
     print("TRIANGULO RETANGULO")
if A**2 < (B**2 + C**2):
     print("TRIANGULO ACUTANGULO")
if A==B and A==C:
     print("TRIANGULO EQUILATERO")
if (((A==B)and(A!=C)) or ((B==C) and (B!=A))):
     print("TRIANGULO ISOSCELES")
