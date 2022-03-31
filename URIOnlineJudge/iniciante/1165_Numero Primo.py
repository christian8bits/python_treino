n = int(input())
i = 1

while i <= n:
       primo = 0
       x = int(input())
       j = 1
       
       while j<=x:
              if x%j == 0:
                     primo = primo +1                     
              j = j+1
       if primo == 2:
              print("%d eh primo" %x)
       else:
              print("%d nao eh primo" %x)

       i = i+1
