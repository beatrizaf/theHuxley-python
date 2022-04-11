def mdc(n,m):
     if n % m == 0:
         return m
     else:
         return mdc(m, n%m)
num = int(input())
for i in range(num):
     n,m = input().split()
     n = int(n)
     m = int(m)
     print("MDC("+str(n)+","+str(m)+") =",mdc(n,m))
