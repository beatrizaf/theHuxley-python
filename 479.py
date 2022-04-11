linha = int(input())
coluna = int(input())
matriz = [[0 for i in range(coluna)] for j in range(linha)]

for i in range(linha):
     elementos = input().split()
     for j in range(coluna):
         matriz[i][j] = elementos[j]

sequencia = int(input())
direcoes = []
for i in range(sequencia):
     direcao = input()
     direcoes.append(direcao)

posicao_linha = int(input())
posicao_coluna = int(input())

for i in range(len(direcoes)):
     if direcoes[i] == 'C': 
         if posicao_linha - 1 > 0: 
             if matriz[posicao_linha - 1][posicao_coluna] == "1":
                 posicao_linha = posicao_linha - 1
     elif direcoes[i] == 'B':
         if posicao_linha + 1 < len(matriz):
             if matriz[posicao_linha + 1][posicao_coluna] == "1":
                 posicao_linha += 1
     elif direcoes[i] == 'D':
          if posicao_coluna + 1 < len(matriz[0]):
             if matriz[posicao_linha][posicao_coluna + 1] == "1":
                 posicao_coluna += 1
     elif direcoes[i] == 'E':
         if posicao_coluna - 1 >= 0:
             if matriz[posicao_linha][posicao_coluna - 1] == "1":
                 posicao_coluna -= 1
print("("+str(posicao_linha)+","+str(posicao_coluna)+")")
         
