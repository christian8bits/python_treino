listaCor1 = set(['Branco', 'Preto', 'Vermelho'])
listaCor2 = set(['Vermelho', 'Verde' ])
print(f'Elementos Originais\n{listaCor1}\n{listaCor2}')

print('\nDiferença entre lista 1 e lista 2:')
print(listaCor1.difference(listaCor2))

print('\nDiferença entre lista 2 e lista 1:')
print(listaCor2.difference(listaCor1))
