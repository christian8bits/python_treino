x= 0
cont= 0
media= 0
while x!=2:
    nota = float(input())
    if nota<0 or nota>10:
        print("nota invalida")
    else:
        media = media + nota
        cont = cont+1
    if cont==2:
        media = media/cont
        print("media = %.2f" %media)
        cont=0
        media=0
        x=0
        while x<1 or x>2:
            x = int(input("novo calculo (1-sim 2-nao)\n"))
