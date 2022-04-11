num = int(input())
matriz1 = []
matriz2 = []
soma = [[0 for i in range(num)] for j in range(num)]
for i in range(num):
     elementos = input().split()
     matriz1.append(elementos)
for i in range(num):
     elementos = input().split()
     matriz2.append(elementos)
for i in range(num):
   aux = ""
   for j in range(num):
     soma[i][j] = int(matriz1[i][j]) + int(matriz2[i][j])
     aux += str(soma[i][j]) + " "
   print(aux)
