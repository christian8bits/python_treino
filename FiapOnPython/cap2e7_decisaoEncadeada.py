nome = input('Digite o nome: ')
idade = int(input('Digite a idade: '))
doenca_infectocontagiosa = input('Suspeita de doença contagiosa? (sim/nao)').upper
if idade >= 65:
  print('Paciente COM prioridade')
  if doenca_infectocontagiosa =='SIM'
    print('encaminhe o paciente para a sala AMARELA')
  elif doenca_infectocontagiosa =='NAO'
    print('Encaminhe o paciente para sala BRANCA')
  else:
    print('Responda a suspeita de doença infectocontagiosa com SIM ou NAO')
else:
  print('Paciente SEM prioridades')
  if doenca_infectocontagiosa=='SIM'
    print ('Encaminhe o paciente para sala AMARELA')
  elif doenca_infectocontagiosa == 'NAO'
    print ('Encaminhe o paciente para sala BRANCA')
  else:
    print('Responda a suspeita de doença infectocontagiosa com SIM ou NAO')
