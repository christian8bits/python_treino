#Faça um Programa que leia três números e mostre o maior deles.
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
if a >= b and a >= c:
    print ('Maior: %d' %a)
elif b >= c:
    print ('Maior: %d' %b)
else:
    print ('Maior: %d' %c)

