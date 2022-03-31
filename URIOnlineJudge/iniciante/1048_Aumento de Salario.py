sal=float(input())

if sal>0 and sal<=400:
     perc=0.15
     saln=(sal*perc)+sal
if sal>400 and sal<=800:
     perc= 0.12
     saln=(sal*perc)+sal
if sal>800 and sal<=1200:
     perc=0.10
     saln=(sal*perc)+sal
if sal>1200 and sal<=2000:
     perc=0.07
     saln=(sal*perc)+sal
if sal>2000:
     perc=0.04
     saln=(sal*perc)+sal

re=sal*perc
cento=perc*100

print("Novo salario: %.2f" %saln)
print("Reajuste ganho: %.2f" %re)
print("Em percentual: %d %%" %cento)
