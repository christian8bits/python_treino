'''
61. Escreva um programa Python para converter a distância (em pés) em polegadas, jardas e milhas.
'''
d_ft = int(input("Insira a distância em pés: "))
d_inches = d_ft * 12
d_yards = d_ft / 3,0
d_milhas = d_ft / 5280,0

print("A distância em polegadas é %i polegadas." % d_inches)
print("A distância em jardas é %.2f jardas." % d_yards)
print("A distância em milhas é %.2f milhas." % d_miles)
