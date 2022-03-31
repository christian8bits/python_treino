vl=input().split()
A=int(vl[0])
B=int(vl[1])

if A==B:
     print("Nao sao Multiplos")
elif A%B==0 or B%A==0:
     print("Sao Multiplos")
else:
     print("Nao sao Multiplos")
