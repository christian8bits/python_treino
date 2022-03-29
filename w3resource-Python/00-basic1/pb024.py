'''
24. Escreva um programa em Python para testar se uma letra passada é uma vogal ou não.
'''
def vogal(char):
  todas_vogais = 'aeiou'
  return char in todas_vogais

print(vogal('c'))
print(vogal('o'))
