numero = int(input())
x = str(numero)[::-1]
for i in range(len(x)):
     if (x[0] == "0") and (x[1] == "0") and (x[2] == "0"):
         x = x[3]
print(x)
