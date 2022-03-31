# -*- coding: utf-8 -*-
m = 1
n = 1
while m >0 and n >0:
        num = input().split()
        m = int(num[0])
        n = int(num[1])
        if m>0 and n>0:
            if n>m:
                i = m
                Sum = 0
                while i<=n:
                    Sum = Sum+i
                    print(i, end=" ")
                    i= i+1
                print("Sum=%d" %Sum)
            else:
                i = n
                Sum = 0
                while i<=m:
                    Sum = Sum+i
                    print(i, end=" ")
                    i= i+1
                print("Sum=%d" %Sum)