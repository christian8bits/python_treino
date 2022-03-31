ld=input().split()
A=float(ld[0])
B=float(ld[1])
C=float(ld[2])

if A+B>C and A+C>B and B+C>A:
     p=A+B+C
     print("Perimetro = %.1f" %p)
else:
     a=((A+B)*C)/2
     print("Area = %.1f" %a)
