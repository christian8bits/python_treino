nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
salario = float(input('Digite seu salario: '))
#usando funcao format
print('Seu nome é {} tem {} anos e recebe {:.2f}'.format(nome, idade, salario))
