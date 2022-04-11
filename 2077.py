numero = int(input())
a = 1
b = 0
multiplo1 = 0
multiplo2 = 0 
multiplo3 = 0
while b < numero:
     b = a*(a+1)*(a+2)    
     multiplo1 = a
     multiplo2 = a+1
     multiplo3 = a+2
     a += 1
if (b != numero) or numero == 0:
     print ("Falso")    
else: 
     print(multiplo1,"*", multiplo2,"*",multiplo3,"=",numero)
     print("Verdadeiro")
