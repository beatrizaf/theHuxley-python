n = 0
while n != -1:
     n = int(input())
     if n >-1:
         fatorial = 1
         while (n>0) and (n<=12):
             fatorial = fatorial * n
             n -= 1
         print(fatorial)
     
