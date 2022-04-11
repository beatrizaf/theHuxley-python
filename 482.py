meta = 0
acumulador = 0 
for i in range(7):
     correspondencias = int(input())
     if correspondencias >= 100:
         meta += 1
     acumulador += correspondencias  
media = acumulador/7
print(meta)
print("%.0f"%media)
     
