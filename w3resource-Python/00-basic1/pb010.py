'''
10. Escreva um programa Python que aceite um inteiro (n) e calcule o valor de n+nn+nnn.
O valor da amostra de n é 5
(Exemplo: 5 + 55 + 555 = 615 )
Resultado esperado: 615
'''
a = int(input('Entre com um numero inteiro: '))
# exemplo: 5 + 55 + 555 = 615
n1 = int('%s' % a)
n2 = int('%s%s' % (a,a))
n3 = int('%s%s%s' % (a,a,a))
print('A Soma n+nn+nnn:')
print(n1+n2+n3)
