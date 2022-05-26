'''
Escreva um programa Python para criar um novo arquivo JSON
a partir de um arquivo JSON existente.
'''

import json

with open('estados.json') as f:
  state_data = json.load(f)

for state in state_data['UF']:
  del state['sigla']

with open('estadosResumo.json', 'w') as f:
  json.dump(state_data, f, indent=2)
