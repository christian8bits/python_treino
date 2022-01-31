# Leia preço de um produto e aplique desconto de 5%

n = float(input('Digite o preço de um produto: '))
desconto  = n * 5 / 100
print('Produto de R${:.2f} com desconto de 5% custa R${:.2f}'.format(n, n - desconto))
