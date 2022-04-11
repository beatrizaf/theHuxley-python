T = int(input())
cont = 0
if (T>= 1) and T<=4:
     lista = input().split(' ')
     a = int(lista[0])
     b = int(lista[1])
     c = int(lista[2])
     d = int(lista[3])
     e = int(lista[4])
     for i in range(len(lista)):
         if lista[i] == str(T):
             cont += 1
     print(cont)
