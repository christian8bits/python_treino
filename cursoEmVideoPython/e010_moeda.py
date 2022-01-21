# leia quanto um valor em reais e converta em dolares

# Considere R$ 4.99 = US$ 1
n = float(input("Quanto dinheiro você tem? \nR$"))
dolar = 4.99
conversao = n / dolar
print("Com R${} você pode comprar US$ {:.2f}.".format(n, conversao))
