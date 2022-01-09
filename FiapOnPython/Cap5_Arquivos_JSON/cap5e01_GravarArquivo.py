with open('teste.txt', 'w') as arquivo:
  arquivo.write('Nunca foi tao facil criar um arquivo')

# Para abrir o arquivo novamente e escrever no final 
# é necessario mudar o segundo parametro para a
with open('teste.txt', 'a') as arquivo:
  arquivo.write(' Continuacao do texto')


