N=int(input())
c=1
while c<=N:
     X=int(input())
     if X==0:
          print("NULL")
     elif X%2==0:
          if X>0:
               print("EVEN POSITIVE")
          else:
               print("EVEN NEGATIVE")
     if (X%2)!=0:
          if X>0:
               print("ODD POSITIVE")
          else:
               print("ODD NEGATIVE")
     c=c+1


     
