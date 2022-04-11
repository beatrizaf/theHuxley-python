n = int(input())
lista = []
stringl = "[ "
for i in range(n):
     elemento = int(input())
     lista.append(elemento)
     stringl += str(elemento) + " "
     
stringl+= "]"
posicao = int(input())
adicionar = int(input())
print(stringl)
if n == 0 and posicao >0:
     print("A posicao",posicao,"estah fora do intervalo")
elif n == 0 and lista == []:
     stringl2 = "[ "
     stringl2 += str(adicionar) + " "
     stringl2 += "]"
     print(stringl2)
else:
     stringl3 = "[ "
     if posicao == 0:
         stringl3 += str(adicionar) + " "
     for i in range(0, posicao):
         stringl3 += str(lista[i]) + " "
         if i == (posicao-1):
             stringl3 += str(adicionar) + " "
     for x in range(posicao, len(lista)):    
         stringl3 += str(lista[x]) + " "   
     stringl3 += "]"
     print(stringl3)
