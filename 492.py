q_total = 0
xicaras = 0 
for i in range(7):
     quantidade = int(input())
     tamanho = input()
     if (tamanho == "p") or (tamanho == "P"):
         q_total += quantidade *10
         xicaras += (quantidade *20)/7
     elif (tamanho == "g") or (tamanho == "G"):
         q_total += quantidade *16
         xicaras += (quantidade *32)/7
 
print(q_total)    
print("%0.0f" %xicaras)
