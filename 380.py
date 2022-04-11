contB = 0
contC = 0
for i in range(7):
     passeio = input().upper()
     if passeio == "BOLICHE":
         contB += 1 
     elif passeio == "CINEMA":
         contC += 1
if contC > contB:
     print("CINEMA")
else:
     print("BOLICHE")
         
