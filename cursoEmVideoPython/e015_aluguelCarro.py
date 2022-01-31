'''
Pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado
Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado
Dias  8 dias
km 720km 
tem que dar R$ 588.00
'''
dias = int(input("Por quantos dias o carro foi alugado: \n"))  
km = float(input("Quantos km o carro rodou: \n")) 
custo_dias = (dias * 60)
custo_km = (km * 0.15)

print("Você andou {}km por {} dias, então o preço a pagar é R${:.2f}.".format(km, dias, (custo_km + custo_dias)))


