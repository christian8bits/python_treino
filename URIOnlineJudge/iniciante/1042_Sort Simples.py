n=input().split()
a=int(n[0])
b=int(n[1])
c=int(n[2])

if a<b and a<c:
     if b<c:
          print("%d\n%d\n%d\n" %(a,b,c))
     else:
          print("%d\n%d\n%d\n" %(a,c,b))
elif b<a and b<c:
     if a<c:
          print("%d\n%d\n%d\n" %(b,a,c))
     else:
          print("%d\n%d\n%d\n" %(b,c,a))
elif c<a and c<b:
     if a<b:
          print("%d\n%d\n%d\n" %(c,a,b))
     else:
          print("%d\n%d\n%d\n" %(c,b,a))

print("%d\n%d\n%d" %(a,b,c))
