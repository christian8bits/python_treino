x=1
mai=0
pos=0
while x<=10:
     n=int(input())
     if n>mai:
          mai=n
          pos=x
     x=x+1
print("%d" %mai)
print("%d" %pos)
