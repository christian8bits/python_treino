n=0
al=0
gas=0
die=0

while n!=4:
     n=int(input())
     if n==1:
          al=al+1
     elif n==2:
          gas=gas+1
     elif n==3:
          die=die+1
     elif n==4:
          print("MUITO OBRIGADO")
print("Alcool: %d" %al)
print("Gasolina: %d" %gas)
print("Diesel: %d" %die)
