nome = input('Digite o nome: ')
idade = int(input('Digite a idade: '))
doenca_infectocontagiosa = input('Suspeita de doença infecto-contagiosa? (Sim/Não)').upper()
if idade >= 65:
  print(f'O paciente {nome} POSSUI atendimento prioritário!')
elif doenca_infectocontagiosa == 'SIM':
  print(f'O paciente {nome} deve ser direcionado para sala de espera reserva') 
else:
  print(f'O paciente {nome} NÃO possui atendimento prioritario!') 

