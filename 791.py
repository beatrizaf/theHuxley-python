def SuperDigito(aux):
     soma = 0
     if len(aux) == 1:
         return aux
     else:
         for i in range(len(aux)):
             soma += int(aux[i])
         aux = str(soma)
         return(SuperDigito(aux))
soma = 0
n,k = input().split()
aux = ""
for i in range(int(k)):
     aux += n
print(SuperDigito(aux))
