N=int(input())
c=1
while c<=N:
     n=input().split()
     N1=float(n[0])
     N2=float(n[1])
     N3=float(n[2])
     med1=(N1*2+N2*3+N3*5)/10
     print("%.1f" %med1)
     c=c+1
