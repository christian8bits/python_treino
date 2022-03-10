a = int(input('Entre com um numero inteiro: '))
# exemplo: 5 + 55 + 555 = 615
n1 = int('%s' % a)
n2 = int('%s%s' % (a,a))
n3 = int('%s%s%s' % (a,a,a))
print('A Soma n+nn+nnn:')
print(n1+n2+n3)
