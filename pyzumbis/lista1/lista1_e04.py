"""
Faça um programa que calcule o aumento de um salário. 
Ele deve solicitar o valor do salário e a
porcentagem do aumento. Exiba o valor do aumento e do novo salário.
"""
s = float(input('Salario: '))
p = float(input('Porcentagem de aumento: '))
aumento = s * p / 100
novo = s + aumento
print('Aumento: %.2f' %aumento)
print('Novo salario: R$ %.2f' %novo)
