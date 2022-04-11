n,m = input().split()
n = int(n)
m = int(m)
matriz = [[0 for i in range(m)] for i in range(n)]
if (n >= 2 and n <= 1000) and (m >= 2 and m <= 1000):
  for i in range(n):
    elementos = input().split()
    for j in range(m):
       if int(elementos[j]) >= 1 and int(elementos[j]) <= 100:
         matriz[i][j] = elementos[j]
menor = 10000000
for j in range(m):
     soma = 0
     for i in range(n):
       soma += int(matriz[i][j])
     if soma < menor:
       menor = soma
print(menor)
