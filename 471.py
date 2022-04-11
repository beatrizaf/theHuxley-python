def ppt(R,M):
     contm = 0
     contr = 0
     if M == "papel" and R == "pedra":
         contm += 1
     elif M == "pedra" and R == "papel":
         contr += 1
     elif M == "pedra" and R == "tesoura":
         contm += 1
     elif M == "tesoura" and R == "pedra":
         contr += 1
     elif M == "tesoura" and R == "papel":
         contm += 1
     elif M == "papel" and R == "tesoura":
         contr += 1
     if contm > contr:
         return("MIGUEL")
     else:
         return("MARIA")

for i in range(5):
     R = input()
     M = input()
     f = ppt(R,M)
print(f)
