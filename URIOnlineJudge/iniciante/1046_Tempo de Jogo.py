t=input().split()
hi=int(t[0])
hf=int(t[1])

if hi==hf:
     ht=24

elif hi>hf:
     ht=(24-hi)+hf

elif hi<hf:
     ht=hf-hi

print("O JOGO DUROU %d HORA(S)" %ht)
             
