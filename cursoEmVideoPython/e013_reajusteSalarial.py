# Leia salario e mostre aumento de 15% 
salario = float(input('Digite o seu salario: \nR$:'))
aumento = salario * 0.15
print('O Salario de R${:.2f} com aumento de 15% vai subir para R${:.2f}'.format(salario, salario + aumento))
