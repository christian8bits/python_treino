c=1
p=0
med=0
while c<=6:
     X=float(input())
     if X>0:
          p=p+1
          med=X+med
     c=c+1

media=med/p     
print("%d valores pares" %p)
print("%.1f" %media)

          
