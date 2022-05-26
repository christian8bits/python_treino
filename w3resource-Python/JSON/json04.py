'''
Escreva um programa Python para converter o objeto de dicionário Python 
(classificar por chave) em dados JSON. 
Imprima os membros do objeto com nível de recuo 4. 
'''

import json
j_str = {'4':5, '6':7, '1':3, '2':4}
print('String original:')
print(j_str)
print('\nJSON:')
print(json.dumps(j_str, sort_keys=True, indent=4))
