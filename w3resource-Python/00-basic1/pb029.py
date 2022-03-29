'''
29. Escreva um programa Python para imprimir um conjunto contendo todas as cores de color_list_1 que não estão presentes em color_list_2.
Dados de teste :
color_list_1 = set(["Branco", "Preto", "Vermelho"])
color_list_2 = set(["Vermelho", "Verde"])
Saída esperada:
{'Preto branco'}
'''
listaCor1 = set(['Branco', 'Preto', 'Vermelho'])
listaCor2 = set(['Vermelho', 'Verde' ])
print(f'Elementos Originais\n{listaCor1}\n{listaCor2}')

print('\nDiferença entre lista 1 e lista 2:')
print(listaCor1.difference(listaCor2))

print('\nDiferença entre lista 2 e lista 1:')
print(listaCor2.difference(listaCor1))
