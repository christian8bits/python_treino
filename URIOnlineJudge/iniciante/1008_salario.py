'''
Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.
'''
fun = int(input('Digite o numero do funcionario: '))
horas = int(input('Digite o numero de horas trabalhadas: '))
valor = float(input('Digite o valor por hora: '))
print(f'NUMBER = {fun}')
print(f'SALARY = U$ {horas * valor}')

'''
fun = int(input())
horas = int(input())
valor = float(input())
salario = horas * valor
print("NUMBER = %d" %fun)
print("SALARY = U$ %0.2f" %salario)
'''
