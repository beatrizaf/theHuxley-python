n = int(input())
menor = 10000
index = 0 
lista = input().split(' ')
for i in range(n):
     elemento = int(lista[i])
for i in range(len(lista)):
     if int(lista[i]) < menor:
         menor = int(lista[i])
         index = i
print("Menor valor:",menor)
print("Posicao:",index)
