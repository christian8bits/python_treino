N=int(input())
i=1
while i<=N:
     num=input().split()
     X=int(num[0])
     Y=int(num[1])
     soma=0
     
     if Y>X:
          if X%2==0:
               X=X+1
          c=X
          while c<Y:
               soma=soma+c
               print("%d" %soma)
               c=c+2
     elif X>Y:
          if Y%2==0:
               Y=Y+1
          c=Y
          while c<X:
               soma=soma+c
               print("%d" %soma)
               c=c+2
     if X==Y:
          print("%d" %soma)
     
     i=i+1
