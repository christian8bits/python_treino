# Declarando e inicializando uma variável
a = 0 
print(a)

# declarando a mesma variável novamente
a = 'Ola mundo A'
print(a)
b = 'Ola mundo B'
print(b)

# Concatenando String
print ('isto é uma string ' + str(123))


# Variavel Local dentro da funcao não altera Variavel Global fora
def funcaoLocal():
  b = 'Ola mundo B, dentro da funcao local'
  print(b)


# Variável Global X Variável local 
def funcaoAlteraEscopo():
  global a
  a = 'Ola Mundo A, funcao altera variavel global'
  print(a)




funcaoAlteraEscopo()
print(a)

funcaoLocal()
print(b)
