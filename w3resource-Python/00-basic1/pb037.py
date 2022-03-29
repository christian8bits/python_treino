'''
37. Escreva um programa Python para exibir seus detalhes como nome, idade, endereço em três linhas diferentes.
'''
def detalhes_pessoais():
  nome, idade = "Chris", 29
  endereco = "Brasil, SP, São Paulo"
  print("Nome: {}\nIdade: {}\nEndereço: {}".format(nome, idade, endereco))

detalhes_pessoais()
