def par(n):
     if n == 0:
         return n
     else:
         print(n)
         return (par(n-2))
n = int(input())
if n%2 == 0:
     print(par(n))
else:
     print(par(n-1))
