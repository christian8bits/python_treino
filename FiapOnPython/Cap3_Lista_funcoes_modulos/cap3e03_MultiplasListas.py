equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = 'S'
#ADICIONA ELEMENTOS NA LISTA
while resposta == 'S':
  equipamentos.append(input('Equipamento: '))
  valores.append(float(input('Valor: ')))
  seriais.append(int(input('Numero serial: ')))
  departamentos.append(input('Departamentos: '))
  resposta = input('\nDigite "S" para continuar: ').upper()
#EXIBE A LISTA  
for indice in range(0, len(equipamentos)):
  print('\nEquipamento...: ', (indice + 1))
  print('Nome..........: ', equipamentos[indice])
  print('Valor.........: ', valores[indice])
  print('Serial........: ', seriais[indice])
  print('Departamento..: ', departamentos[indice])
#BUSCA ELEMENTO NA LISTA
busca = input('\nDigite o nome do equipamento que deseja buscar: ')
for indice in range(0, len(equipamentos)):
  if busca == equipamentos[indice]:
    print('Valor...: ', valores[indice])
    print('Serial..: ', seriais[indice])
    
    
