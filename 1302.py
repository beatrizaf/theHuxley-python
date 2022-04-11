m = [[0,0,0],[0,0,0],[0,0,0]]
aux = 0
cont = 0
menor = 100000
soma = 0
for i in range(3):
     for j in range(3):
         elemento = int(input())
         m[i][j] = elemento
         if m[i][j] > 0:
             aux += m[i][j]
             cont += 1
         if m[i][j] < menor:
             menor = m[i][j]
         if i != j:
             soma += m[i][j]
if menor%2 == 0:
     delta = 1
else:
     delta = 0
if cont > 0:
     media = aux/cont
print("%.2f" %media, menor,delta,soma)
