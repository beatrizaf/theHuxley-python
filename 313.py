linha = int(input())
cont = 0
soma = 0
if linha >= 0 and linha <= 11:
     operacao = input()
     matriz = [[0 for i in range(12)] for j in range(12)]
     for i in range(12):
         elemento = input().split(" ")
         for j in range(12):
             matriz[i][j] = float(elemento[j])
             if i == linha:
                 soma += matriz[i][j]
                 cont += 1
if cont > 0:
     media = soma/cont
if operacao == "S":
     print("%.1f"%soma,"\n")
else:
     print("%.1f"%media,"\n")
