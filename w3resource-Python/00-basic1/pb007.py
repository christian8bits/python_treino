nomearquivo = input('Entre com o nome completo do arquivo: ')
extensao = nomearquivo.split('.')
print('A extensão do arquivo {} é:  {}'.format(repr(extensao[0]),repr(extensao[-1])))
