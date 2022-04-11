n, m, o = input().split()
matrizA = []
matrizB = []
matrizTransposta = []
for i in range(int(n)):
    elementosA = input().split()
    matrizA.append(elementosA)
for i in range(int(m)):
    elementosB = input().split()
    matrizB.append(elementosB)
for i in range(int(o)):
     l = [] 
     for j in range(int(m)):
       l.append(matrizB[j][i])
     matrizTransposta.append(l)

for i in range(int(n)):
     aux = ""
     for x in range(int(n)):
         soma = 0
         for j in range(int(m)):
           soma += int(matrizA[i][j]) * int(matrizTransposta[x][j])
         aux += str(soma) + " "
     print(aux.rstrip(" "))
