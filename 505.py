n = int(input())
numeros = []
for i in range(n):
     numero = int(input())
     numeros.append(numero)
deslocar = int(input())
for i in range(deslocar):
     x = numeros[0]
     del numeros[0]
     numeros.append(x)
for i in range(len(numeros)):
     print(numeros[i])     
