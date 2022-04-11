n = int(input())
lista = []
stringl = "[ "
for i in range(n):
     elemento = input()
     lista.append(elemento)
     stringl += elemento + " "
     
stringl+= "]"
pop = int(input())
print(stringl)
if n == 0:
     print("A lista estah vazia - nao eh possivel remover elementos")
elif pop > len(lista):
     print("Nao eh possivel remover o elemento")
else:
     print("O item %s serah removido da lista" %(lista[pop]))
     stringl2 = "[ "
     for i in range(len(lista)):
         if i != pop:
             stringl2 += lista[i] + " "
     stringl2 += "]"
     print(stringl2)
