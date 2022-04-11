ordem = int(input())
matriz = [[0 for i in range(ordem)] for j in range(ordem)]
for i in range(ordem):
     elemento = input().split(" ")
     for j in range(ordem):
         matriz[i][j] = int(elemento[j])

nova_matriz = [[0 for i in range(ordem)] for j in range(ordem)]
aux = ""
for i in range(ordem):
      for j in range(ordem):
          nova_matriz[i][j] = matriz[j][i]
          if nova_matriz[i][j] < 0:
              nova_matriz[i][j] = int(nova_matriz[i][j])*2
          aux += str(nova_matriz[i][j]) + " "
      print(aux[:-1])
      aux = ""
