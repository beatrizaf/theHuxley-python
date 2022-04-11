def calcular_leds(digito):
     cont = 0
     for i in range(len(digito)):
         if digito[i] == "1":
             cont += 2 
         elif digito[i] == "2" or digito[i] == "3" or digito[i] == "5":
             cont += 5
         elif digito[i] == "4":
             cont += 4
         elif digito[i] == "6" or digito[i] == "9" or digito[i] == "0":
             cont += 6 
         elif digito[i] == "7":
             cont += 3
         elif digito[i] == "8":
             cont += 7
     return cont
num = int(input())
l = []
for i in range(num):
     digito = input()
     l.append(digito)
for i in range(len(l)):
     print(calcular_leds(l[i]),"leds")
     
