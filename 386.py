valor_anterior = 0
vezes = -1
acumulador = 0
for i in range(7):
     valor = float(input())
     if valor > valor_anterior:
         vezes += 1
     valor_anterior = valor
     acumulador += valor
print("R$","%.2f"%acumulador)
print(vezes)
