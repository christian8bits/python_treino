# CODIGO MultiplasListas.py COM DELETE DE UM ELEMENTO PELO SERIAL
equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = 'S'
# ADICIONA ELEMENTOS NAS LISTAS
while resposta == 'S':
  equipamentos.append(input('Equipamento: '))
  valores.append(float(input('Valor: ')))
  seriais.append(int(input('Numero serial: ')))
  departamentos.append(input('Departamentos: '))
  resposta = input('\nDigite "S" para continuar: ').upper()
# EXIBE AS LISTAS  
for indice in range(0, len(equipamentos)):
  print('\nEquipamento...: ', (indice + 1))
  print('Nome..........: ', equipamentos[indice])
  print('Valor.........: ', valores[indice])
  print('Serial........: ', seriais[indice])
  print('Departamento..: ', departamentos[indice])
# DELETA TODOS OS ELEMENTOS COM O MESMO INDICE NAS LISTAS
serial=int(input('\nDigite o serial do equipamento que será excluido: '))
for indice in range(0, len(departamentos)):
  if seriais[indice]==serial:
    del departamentos[indice]
    del equipamentos[indice]
    del seriais[indice]
    del valores[indice]
    break
# EXIBE AS LISTAS  
for indice in range(0, len(equipamentos)):
  print('\nEquipamento...: ', (indice + 1))
  print('Nome..........: ', equipamentos[indice])
  print('Valor.........: ', valores[indice])
  print('Serial........: ', seriais[indice])
  print('Departamento..: ', departamentos[indice])
    
    
