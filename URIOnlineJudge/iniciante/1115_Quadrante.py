X=1
Y=1
while X!=0 or Y!=0:
     pnt=input().split()
     X=float(pnt[0])
     Y=float(pnt[1])
     
     if((X>0)and(Y>0)):
          print("primeiro")
     elif((X<0)and(Y>0)):
          print("segundo")
     elif((X<0)and(Y<0)):
          print("terceiro")
     elif((X>0)and(Y<0)):
          print("quarto")
     elif X==0 or Y==0:
          break
