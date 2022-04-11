n = int(input())
lista = []
stringl = "[ "
for i in range(n):
     elemento = input()
     lista.append(elemento)
     stringl += elemento + " "
     
stringl+= "]"
remover = int(input())
print(stringl)
if lista == []:
     print("A lista estah vazia - nao eh possivel remover elemento")
elif str(remover) not in lista:
     print("Nao eh possivel remover o elemento",remover)
else:
     stringl2 = "[ "
     for i in range(len(lista)):
         if lista[i] != str(remover):
             stringl2 += lista[i] + " "
     stringl2 += "]"
     print(stringl2)
