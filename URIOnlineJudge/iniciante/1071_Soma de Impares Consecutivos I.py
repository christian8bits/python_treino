X=int(input())
Y=int(input())
soma=0
if Y>X:
     if X%2==0:
          X=X+1
     else:
          X=X+2
     c=X
     while c<Y:
          soma=soma+c
          c=c+2
                 
if X>Y:
     if Y%2==0:
          Y=Y+1
     else:
          Y=Y+2
     c=Y
     while c<X:
          soma=soma+c
          c=c+2          
                
print("%d" %soma)
