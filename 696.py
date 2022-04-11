numeros = []
cont = 0
for i in range(10):
     numeros.append(int(input()))
x = int(input())
for num in range(len(numeros)):
     if numeros[num] == x:
         cont+= 1
print(cont)
