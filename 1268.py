n = int(input())
a = '*'
contador = 0
for i in range(n,0,-1):
     print(i * ".",end="")
     print(a)
     a+='**'
for i in range(1,n+1):
     print(i * ".",end="")
     print((((n-contador)*2)-1)*"*")
     contador += 1
