lc = input().split(" ")
l = int(lc[0])   
c = int(lc[1])
matriz = [[0 for i in range(c)] for j in range(l)]
principal = 0
secundaria = 0
menores = 0 
maiores = 0
aux = ""
cont = 0
for i in range(l):
     for j in range(c):
         elemento = int(input())
         matriz[i][j] = elemento 
         if i == j:
           principal += matriz[i][j]
         if matriz[i][j] < 0:
           menores += 1
         else:
           maiores += 1

print("Matriz formada:")
for i in range(l):
     cont+= 1
     for j in range(c):
        aux += str(matriz[i][j]) + " "
     print(aux[:-1])
     aux = ""
matriz[-cont]
for i in range(l):
     for j in range(c):
         if i == j:
             secundaria += matriz[i][j]

if l == c:  
     if principal == secundaria:
         print("A diagonal principal e secundaria tem valor(es)",principal,"e",secundaria,"respectivamente.")
     else:
         print("A diagonal principal e secundaria tem valor(es)",principal,"e",secundaria)
else:
   print("A diagonal principal e secundaria nao pode ser obtida.")
print("A matriz possui",menores,"numero(s) menor(es) que zero.")
print("A matriz possui",maiores,"numero(s) maior(es) que zero.")
