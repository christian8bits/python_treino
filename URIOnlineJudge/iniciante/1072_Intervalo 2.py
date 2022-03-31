N=int(input())
c=1

s=0
n=0

while c<=N:
     X=int(input())
     if X>=10 and X<=20:
          s=s+1
     else:
          n=n+1
     c=c+1

print("%d in" %s)
print("%d out" %n)
          
