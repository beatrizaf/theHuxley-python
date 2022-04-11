maior_soma = 0
num_maior = 0
for i in range(5):
     n = int(input())
     soma = 0
     for x in range(1,n+1):
         if (n % x) == 0:
             soma += x
     if soma > maior_soma:
         maior_soma = soma
         num_maior = n
print(num_maior)
