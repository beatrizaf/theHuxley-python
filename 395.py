def mdc(n,m):
     if n % m == 0:
         return m
     else:
         return mdc(m, n%m)
n = int(input())
m = int(input())
print(mdc(n,m))
