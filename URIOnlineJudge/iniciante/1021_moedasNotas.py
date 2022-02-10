N=float(input())
#Notas
n100=N/100
n50=(N%100)/50
n20=((N%100)%50)/20
n10=(((N%100)%50)%20)/10
n5=((((N%100)%50)%20)%10)/5
n2=(((((N%100)%50)%20)%10)%5)/2

#Moedas
N2=int(N)
x=((N-N2)*100) #moeda é inteiro

m1=((((((N%100)%50)%20)%10)%5)%2)/1
m50=(x/50)
m25=(x%50)/25
m10=((x%50)%25)/10
m5=(((x%50)%25)%10)/5
m01=((((x%50)%25)%10)%5)/1


print("NOTAS:")
print("%d nota(s) de R$ 100.00" %n100)
print("%d nota(s) de R$ 50.00" %n50)
print("%d nota(s) de R$ 20.00" %n20)
print("%d nota(s) de R$ 10.00" %n10)
print("%d nota(s) de R$ 5.00" %n5)
print("%d nota(s) de R$ 2.00" %n2)
print("MOEDAS:")
print("%d moeda(s) de R$ 1.00" %m1)
print("%d moeda(s) de R$ 0.50" %m50)
print("%d moeda(s) de R$ 0.25" %m25)
print("%d moeda(s) de R$ 0.10" %m10)
print("%d moeda(s) de R$ 0.05" %m5)
print("%d moeda(s) de R$ 0.01" %m01)
