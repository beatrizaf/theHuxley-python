termos = int(input())
soma = 0
string = " "
denominador = 0
for i in range(1,termos+1,2):
     s = (i/(denominador+4)) + 1 
     string += str(i) +"/"+ str(denominador+4) +" "+"+"+" " + "1" +" "+ "+" +" "
     soma += s
     denominador += 4
if termos %2 != 0:
     soma = soma-1
     print("%.2f"%soma)
     print(string.rstrip("+ 1").lstrip("+ "))
else:
     print("%.2f"%soma)
     print(string.rstrip("+ ").lstrip(" "))
