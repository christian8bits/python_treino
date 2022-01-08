"""
Faça um programa que leia um nome de usuário e a sua senha 
e não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações.
"""
usuario = input('Usuario ')
senha = input('Senha: ')
while usuario == senha:
  print ('Senha deve ser diferente do usuario')
  usuario = input('Usuario ')
  senha = input('Senha: ') 
