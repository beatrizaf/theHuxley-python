def par(n):
     if n == 0:
         return(n)
     else:
         l.append(n)
         return (par(n-2))
n = int(input())
l = []
if n%2 == 0:
     print(par(n))
else:
     print(par(n-1))
x = l[::-1]
for i in range(len(x)):
     print(x[i])
