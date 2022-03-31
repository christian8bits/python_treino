c=1
p=0
n=0
ev=0
od=0
while c<=5:
     X=int(input())
     if X%2==0:
          ev=ev+1
          if X>0:
               p=p+1
          elif X<0:
               n=n+1
     if X%2!=0:
          od=od+1
          if X>0:
               p=p+1
          elif X<0:
               n=n+1
     c=c+1

print("%d valor(es) par(es)",end="" %ev)
print("%d valor(es) impar(es)"%od)
print("%d valor(es) positivo(s)"%p)
print("%d valor(es) negativo(s)"%n)
          
