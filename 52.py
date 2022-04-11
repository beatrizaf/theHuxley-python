n = int(input())
for i in range(1,n):
     soma = 0
     for x in range(1,i+1):
         if (i % x) == 0:
             soma += x
     if soma == (2*i):
         print(x)
