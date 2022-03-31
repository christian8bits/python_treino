X=int(input())
Y=int(input())
soma=0
c=1
if Y>X:
     c=X+1
     while c<Y:
          if (c%5==2 or c%5==3):
               print("%d" %c)
          c=c+1
                 
if X>Y:
     c=Y+1
     while c<X:
          if (c%5==2 or c%5==3):
               print("%d" %c)
          c=c+1
