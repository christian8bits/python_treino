# Escreva um programa Python para converter dados JSON em objeto Python. 
import json
json_obj = '{ "Nome": "David", "Class":"I", "Idade":19}'
python_obj = json.loads(json_obj)
print('\nJSON data:')
print(python_obj)
print('\nName: ',python_obj['Nome'])
print('Class: ',python_obj['Class'])
print('Idade:', python_obj['Idade'])
