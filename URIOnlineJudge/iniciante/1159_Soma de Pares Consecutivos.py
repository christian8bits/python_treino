x = 1
while x != 0:
       x = int (input())
       soma = 0       
       i = 1
       if x==0:
              break  
       if x%2 == 0:
              while i<=5:
                     soma = soma+x
                     x = x+2
                     i = i+1
              print("%d" %soma)

       else:
              x = x+1
              while i<=5:
                     soma = soma+x
                     x = x+2
                     i = i+1
              print("%d" %soma)      
   
   
