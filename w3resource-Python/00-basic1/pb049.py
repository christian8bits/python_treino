'''
49. Escreva um programa Python para listar todos os arquivos 
em um diretório em Python.
'''
from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('/home/Documentos') if isfile(join('/home/Documentos', f))]
print(files_list);
