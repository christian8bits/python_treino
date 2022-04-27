'''
64. Escreva um programa Python para obter as datas/horas 
de criação e modificação do arquivo.
'''
import os.path, time
print("Ultima modificação: %s" % time.ctime(os.path.getmtime("00PytthonBasic.txt")))
print("Criado em: %s" % time.ctime(os.path.getctime("00PytthonBasic.txt")))
