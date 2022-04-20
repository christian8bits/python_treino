'''
39. Escreva um programa em Python para calcular o valor futuro de
um valor principal especificado, taxa de juros e um número de anos.
Dados de teste: amt = 10.000, int = 3,5, anos = 7
Saída esperada: 12722,79
'''
amt = 1000
int = 3.5
anos = 7
valor_futuro = amt*((1+(0.01*int)) ** anos)
print(round(valor_futuro, 2))
