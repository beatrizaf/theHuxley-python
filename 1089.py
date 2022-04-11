termos = int(input())
soma = 0
string = " "
for i in range(1,termos+1):
     s = (i)/(i*3)
     string += str(i)+ "/"+ str(i*3)+ " "+ "+"+ " "
     soma += s
print(string.rstrip("+ "))
print("%.2f"%soma)
