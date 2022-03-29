'''
1. Escreva um programa Python para imprimir a seguinte string em um formato específico (veja a saída).
Sequência de Amostra: "Brilha, brilha, estrelinha, Como eu me pergunto o que você é! Acima do mundo tão alto, Como um diamante no céu. Brilha, brilha, estrelinha, Como eu me pergunto o que você é" Saída:

Brilha Brilha Estrelinha,
  	Como eu me pergunto o que você é!
    		Acima do mundo tão alto,
    		Como um diamante no céu.
Brilha Brilha Estrelinha,
  	Como eu me pergunto o que você é!
'''

# Usando quebra de linha e tabulação
print("Brilha Brilha Estrelinha, \n\tComo eu me pergunto o que você é! \n\t\tAcima do mundo tão alto, \n\t\tComo um diamante no céu. \nBrilha Brilha Estrelinha, \n\tComo eu me pergunto o que você é!")
 
# Usando aspas triplas 
texto = '''
Brilha Brilha Estrelinha,
  	Como eu me pergunto o que você é!
    		Acima do mundo tão alto,
    		Como um diamante no céu.
Brilha Brilha Estrelinha,
  	Como eu me pergunto o que você é!
'''    
print(texto)
