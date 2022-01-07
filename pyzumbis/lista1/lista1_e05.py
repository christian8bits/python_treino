"""
Solicite o preço de uma mercadoria e o percentual de desconto. 
Exiba o valor do desconto e o preço a pagar.
"""
m = float(input('Preço da mercadoria: '))
p = float(input('Porcentagem de desconto: '))
desconto = m * p / 100
novo = m - desconto
print('Desconto: R$ %.2f' %desconto)
print('Preço a pagar: R$ %.2f' %novo)
