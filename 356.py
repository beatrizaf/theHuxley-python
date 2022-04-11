def Decimal(num):
     if num == 0:
         return 0
     elif num == 1:
         return 1
     else:
         if num % 2 == 0:
             l.append(0)
         else:
             l.append(1)
         return(Decimal(num// 2 ))
num = int(input())
l = []
print(Decimal(num))
x = l[::-1]
for i in range(len(x)):
     print(x[i])
