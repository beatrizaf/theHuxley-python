escala = input()
temperatura = float(input())

if (escala == "C"):
     if (temperatura >= -273.0):
         F = (1.8 * temperatura) + 32 
         K = temperatura + 273.15
         print("%.2f" %F,"F")
         print("%.2f" %K,"K")
     else:
         print("Valor de temperatura abaixo do minimo")
         
elif (escala == "F"):
     if (temperatura >= -459.67):
         C = (temperatura - 32) / 1.8
         K = (temperatura + 459.67) * (5/9) 
         print("%.2f" %C,"C")
         print("%.2f" %K,"K")
     else:
         print("Valor de temperatura abaixo do minimo")
         
elif (escala == "K"):
     if (temperatura >= 0.0):
         C = temperatura - 273.15
         F = 1.8 * (temperatura - 273.15) + 32
         print("%.2f" %C,"C")
         print("%.2f" %F,"F")
     else:
         print("Valor de temperatura abaixo do minimo")
