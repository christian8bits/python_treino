N=int(input())
c=1
while c<=N:
     l=input().split()
     X=int(l[0])
     Y=int(l[1])

     if Y==0:
          print("divisao impossivel")
     else:
          d=X/Y
          print("%.1f" %d)
     c=c+1
