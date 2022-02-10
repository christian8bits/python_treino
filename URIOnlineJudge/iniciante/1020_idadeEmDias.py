# Leia a idade em anos e expresse a idade em ano, meses e dias.

ida=int(input())

if ida<31:
     ano=0
     mes=ida/30
     dia=ida%30

elif ((ida>30) and (ida<360)):
     ano=0
     mes=ida/30
     dia=ida%30

elif ((ida>=360) and (ida<365)):
     ano=0
     mes=(ida/30)-1
     dia=30-(365-ida)

elif ida>=365:
     ano=ida/365
     mes=(ida%365)/30
     dia=((ida%365)%30)

print("%d ano(s)" %ano)
print("%d mes(es)" %mes)
print("%d dia(s)" %dia)
