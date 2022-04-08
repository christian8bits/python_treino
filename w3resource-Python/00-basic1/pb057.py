'''
57. Escreva um programa Python para obter o tempo de execução de um método Python.
'''
import time
def soma_n_numeros(n):
    inicio = time.time()
    s = 0
    for i in range(1,n+1):
        s = s + i
    fim = time.time()
    return s,inicio-fim

n = 5
print("\nTempo de execução somado 1 a",n," e o tempo necessario para somar isso é :",soma_n_numeros(n))
