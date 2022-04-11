ordem = int(input())
principal = ""
cont = 0
matriz = [[0 for i in range(ordem)] for j in range(ordem)]
for i in range(ordem):
     elemento = input().split(" ")
     for j in range(ordem):
         matriz[i][j] = float(elemento[i])
         if i == j:
             cont += matriz[i][j]
             principal += "("+str("%.2f"%matriz[i][j])+")" + " + "
print("tr(A) =",principal[:-3],"=","%.2f"%cont)
