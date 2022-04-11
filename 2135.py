n1 = int(input())
l1 = []
if n1 >0:
  for i in range(n1):
    l1.append(int(input()))
  n2 = int(input())
  l2 = []
  if n2 > 0:
    for i in range(n2):
     l2.append(int(input()))
     l3 = l1 + l2
     acumulador = ''
    for i in range(len(l3)):
     acumulador += str(l3[i]) + " "
    acumulador.rstrip(" ")
    print(acumulador)
  else: 
    print("Erro - A lista deve ter pelo menos 1 elemento.")
else: 
  print("Erro - A lista deve ter pelo menos 1 elemento.")
