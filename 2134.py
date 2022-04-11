notas = []
n = int(input())
acumulador = 0
if n > 0  and (n<=5):
     for i in range(n):
         notas.append(float(input()))
         print("Nota",str(i+1)+":",notas[i])
         acumulador += notas[i]
     media = acumulador/n
     print("Media:","%.2f"%media)
else:
     print("Numero de notas invalido.")

     
