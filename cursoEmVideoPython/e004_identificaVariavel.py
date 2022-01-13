#Ler algo e mostrar seu tipo primitivo e todas as informações sobre
a = input('Digite algo: ')
print('Qual o tipo primitivo dessa variavel? ', type(a))
print('Tem só espaços? ', a.isspace())
print('É um numero? ', a.isnumeric())
print('É alfabetico? ', a.isalpha())
print('É alfanumerico? ', a.isalnum())
print('Está em maiúsculas? ', a.isupper())
print('Está em minúsculas:? ', a.islower())
print('Está capitalizada? ', a.istitle())

