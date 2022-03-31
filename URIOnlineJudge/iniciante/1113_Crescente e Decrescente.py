X=0
Y=1

while X!=Y:
     num=input().split()
     X=int(num[0])
     Y=int(num[1])
     if X==Y:
          break
     elif X>Y:
          print("Decrescente")
     else:
          print("Crescente")
     
