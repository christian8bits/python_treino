'''
5. Escreva um programa Python que aceite o nome e sobrenome 
do usuário e imprima-os na ordem inversa com um espaço entre eles.
'''
pnome = input('Entre com o seu primeiro nome: ')
unome = input('Entre com o seu ultimo nome: ')
# Formas diferentes de imprimir uma variavel
print(f'Olá {pnome} {unome}')
print('Seu ultimo nome: ' + unome + ' e seu primeiro nome é ' +pnome)
print('Tchau {} um abraço pra familia {}'.format(pnome, unome))
