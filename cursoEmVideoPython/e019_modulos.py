import random
pergunta = 'leia quatro nomes e escolhe um aleatoriamente'
print(pergunta)
n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto nome: ')
lista_pessoas = (n1, n2, n3, n4)
escolhido = random.choice(lista_pessoas)
print(f'A pessoa escolhida foi {escolhido}')
