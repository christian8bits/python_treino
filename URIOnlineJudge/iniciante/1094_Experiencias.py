N=int(input())
i=1
C=0
R=0
S=0
total=0
while i<=N:
     x=input().split()
     Quantia=int(x[0])
     Tipo=str(x[1])
     if Tipo=="C":
          C=Quantia+C
     elif Tipo=="R":
          R=Quantia+R
     elif Tipo=="S":
          S=Quantia+S
     i=i+1
total=C+R+S
pC=(C/total)*100
pR=(R/total)*100
pS=(S/total)*100
print("Total: %d cobaias" %total)
print("Total de coelhos: %d" %C)
print("Total de ratos: %d" %R)
print("Total de sapos: %d" %S)
print("Percentual de coelhos: %.2f %%" %pC)
print("Percentual de ratos: %.2f %%" %pR)
print("Percentual de sapos: %.2f %%" %pS)
