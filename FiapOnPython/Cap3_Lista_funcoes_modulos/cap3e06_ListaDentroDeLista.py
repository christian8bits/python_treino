inventario=[]
resposta = 'S'
# ADICIONA LISTA DENTRO DE LISTA
while resposta == 'S':
  equipamento=[input('Equipamento: '), float(input('Valor: ')),int(input('Número Serial: ')),input('Departamento: ')]
  inventario.append(equipamento)
  resposta = input('\nDigite "S" para continuar: ').upper()
# EXIBE ELEMENTOS DE CADA LISTA
for elemento in inventario:
  print('\nNome.........: ', elemento[0])
  print('Valor........: ', elemento[1])
  print('Serial.......: ', elemento[2])
  print('Departamento.: ', elemento[3])
# BUSCA nome NAS LISTAS
busca = input('\nDigite o nome do equipamento que deseja buscar: ')
for elemento in inventario:
  if busca == elemento[0]:
    print('Valor..: ', elemento[1])
    print('Serial.:', elemento[2])
# ALTERA elemento
depreciacao = input('\nDigite o nome do equipamento que será depreciado: ')
for elemento in inventario:
  if depreciacao == elemento[0]:
    print('Valor antigo: ', elemento[1])
    elemento[1] = elemento[1] * 0.9
    print('Novo valor: ', elemento[1])
# EXCLUI elemento
serial = int(input('\nDigite o serial do equipamento que será excluído: '))
for elemento in inventario:
  if elemento[2] == serial:
    inventario.remove(elemento)
# EXIBE elemento
for elemento in inventario:
  print('\nNome.........: ', elemento[0])
  print('Valor........: ', elemento[1])
  print('Serial.......: ', elemento[2])
  print('Departamento.: ', elemento[3])
