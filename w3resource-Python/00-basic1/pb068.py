num = int(input("Digite um número de quatro dígitos: "))
x = num //1000
x1 = (num - x*1000)//100
x2 = (num - x*1000 - x1*100)//10
x3 = num - x*1000 - x1*100 - x2*10
print("A soma dos dígitos do número é", x+x1+x2+x3)
