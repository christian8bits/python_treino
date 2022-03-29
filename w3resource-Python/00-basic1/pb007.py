'''
7. Escreva um programa Python para aceitar um nome de arquivo do usuário e imprima a extensão dele.
Nome do arquivo de exemplo: abc.java
Saída: java
'''
nomearquivo = input('Entre com o nome completo do arquivo: ')
extensao = nomearquivo.split('.')
print('A extensão do arquivo {} é:  {}'.format(repr(extensao[0]),repr(extensao[-1])))
