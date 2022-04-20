'''
42. Escreva um programa Python para determinar se um 
shell Python está sendo executado no modo de 32 bits ou 64 bits no SO.
'''
import platform, struct
print(platform.architecture()[0])
print(struct.calcsize("P") * 8)
