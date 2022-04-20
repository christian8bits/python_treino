'''
51. Escreva um programa Python para determinar o perfil de programas Python.
Nota: Um perfil é um conjunto de estatísticas que descreve 
com que frequência e por quanto tempo várias partes do programa são executadas. Essas estatísticas podem ser formatadas em relatórios por meio do módulo pstats.
'''
import cProfile
def sum():
    print(1+2)
    
cProfile.run('sum()')
