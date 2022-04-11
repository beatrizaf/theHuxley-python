numero1 = int(input())
numero2 = int(input())
if numero1 > numero2:
  numero1 = numero2
  numero2 = numero1
for x in range(numero1,numero2+1):
  if x%2 == 1:
    print(x)
