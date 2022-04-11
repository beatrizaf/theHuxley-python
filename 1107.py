def permutacao(matriz):
     cont  = 0
     for i in range(ordem):
         cont_linha = 0
         cont_coluna = 0
         for j in range(ordem):
             if matriz[i][j] == "1" or matriz[i][j] == "0":
                 if matriz[i][j] == "1":
                     cont_linha +=1
                 if matriz[j][i] == "1":
                     cont_coluna +=1
             else:
                 return False
         if cont_linha == 1 and cont_coluna == 1:
             cont += 1
     if cont == ordem:
         return True
     else:
         return False

ordem = int(input())
elementos = input().split()
cont = 0
matriz = []
l = []
for x in range(len(elementos)):
      cont += 1
      l.append(elementos[x])
      if cont == ordem:
          matriz.append(l)
          l =[]
          cont = 0
for i in range(ordem):
     aux = ''
     for j in range(ordem):
         aux += str(matriz[i][j]) + ' '
     print(aux)
print(permutacao(matriz))
