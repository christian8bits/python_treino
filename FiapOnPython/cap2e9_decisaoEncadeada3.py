nivel = input('Digite o nivel de acesso ADM/USER/GUEST: ').upper()
if nivel == 'ADM' or nivel == 'USER':
  genero = input('Digite o seu gênero FEMININO/MASCULINO: ').upper()
  if nivel == 'ADM':
    if genero == 'FEMININO':
      print('Olá adminsitradora')
    else:
      print('Olá adminstrador')
  else:
    if genero == 'FEMININO':
      print('Olá Usuária')
    else: 
      print('Olá Usuário')
elif nivel == 'GUEST':
  print('Olá Visitante')
else:
  print('Olá desconhecido(a)')
