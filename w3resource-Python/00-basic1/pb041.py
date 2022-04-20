# 41. Escreva um programa Python para verificar se existe um arquivo.
import os.path
# Solucao 1
print(os.path.isfile('main.txt'))
print(os.path.isfile('main.py'))

# Solucao 2
print(os.path.exists('main.txt'))
print(os.path.exists('main.py'))
