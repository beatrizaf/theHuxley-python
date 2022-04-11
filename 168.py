matriz = []
for i in range(3):
     itens = input().split()
     matriz.append(itens)
precos = input().split()
for i in range(3):
  soma = 0
  for j in range(4):
    x = int(matriz[i][j]) * float(precos[j])
    soma += x
  print("%.2f"%soma)
