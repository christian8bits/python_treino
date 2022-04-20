'''
31. Escreva um programa em Python para calcular o máximo divisor 
comum (GCD) de dois inteiros positivos.
'''
def gcd(x, y):
  gcd = 1
  if x % y == 0:
    return y
  for k in range(int(y / 2), 0, -1):
    if x % k == 0 and y % k == 0:
      gcd = k
      break
  return gcd

print(f'GCD de 12 e 17 = {gcd(12, 17)}')
print(f'GCD de 4 e 6 = {gcd(4, 6)}')
print(f'GCD de 336 e 360 = {gcd(336, 360)}')
