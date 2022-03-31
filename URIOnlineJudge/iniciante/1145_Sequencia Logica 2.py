num = input().split()
x = int(num[0]) # 3
y = int(num[1]) # 99
cont1 = 1
cont2 = 0
soma  = ""
while cont1 < y:
    while cont2 < x:
        soma = soma + str(cont1) + " "
        if cont1 == y:
            cont2 = x
        cont1 +=1
        cont2 +=1
    cont2 = 0
    print(soma[0:-1])
    soma = ""
