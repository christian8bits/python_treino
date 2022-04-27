'''
62. Escreva um programa Python para converter todas as unidades de tempo em segundos.
'''
dias = int(input("Dias de entrada: ")) * 3600 * 24
horas = int(input("Insira horas: ")) * 3600
minutos = int(input("Insira minutos: ")) * 60
segundos = int(input("Digite segundos: "))

tempo = dias + horas + minutos + segundos

print("A quantidade de segundos", tempo)
