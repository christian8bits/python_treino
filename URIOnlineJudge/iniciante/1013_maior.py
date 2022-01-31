'''Faça um programa que leia três valores e apresente o maior dos valores seguido da mensagem “eh o maior”.
Utilize a fórmula: MaiorAB=(a+b+abs(a-b))/2.
'''

val=input().split()

a=int(val[0])
b=int(val[1])
c=int(val[2])

MaiorAB=(a+b+abs(a-b))/2
MaiorABC = (MaiorAB + c + abs(MaiorAB - c)) / 2

print("%d eh o maior" %MaiorABC)
