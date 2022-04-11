tamanho = int(input())
numeros = []
s = 0
for i in range(tamanho):
     numeros.append(int(input()))
if tamanho > 0:
     while len(numeros) != 0:
         if len(numeros) == 1:
             soma = (numeros[0] - 0)**2
             del numeros[0]
         else:
             soma = (numeros[0] - numeros[-1])**2
             del numeros[0]
             del numeros[-1]
         s += soma
     print("S =",s)
elif tamanho == 0:
     print("Lista vazia - O valor de S eh zero")
else:
     print("O valor informado para N foi negativo")
