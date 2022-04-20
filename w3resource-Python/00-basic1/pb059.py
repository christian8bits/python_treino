'''
59. Escreva um programa Python para converter altura (em pés e polegadas) 
em centímetros.
'''
print("Entre com sua altura: ")
h_ft = int(input("Digite o tamanho em pés: "))
h_inch = int(input("Digite o tamanho em polegadas: "))

h_inch += h_ft * 12
h_cm = round(h_inch * 2.54, 1)

print("Sua altura é : %d cm." % h_cm)

