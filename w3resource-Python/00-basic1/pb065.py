tempo = float(input("Insira o tempo em segundos: "))
dia = hora // (24 * 3600)
tempo = tempo % (24 * 3600)
hora = hora // 3600
tempo %= 3600
minutos = tempo // 60
tempo %= 60
segundos = tempo
print("d:h:m:s-> %d:%d:%d:%d"% (dia, hora, minutos, segundos))
