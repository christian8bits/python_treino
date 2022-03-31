med=0
c=0
while c!=2:
     n=float(input())
     if n>=0 and n<=10:
          med=med+n
          c=c+1
     else:
          print("nota invalida")

med=med/2
print("media = %.2f" %med)
