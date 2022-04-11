menor_cre = 100000
acumulador_cre= 0
contador_cre = 0
matricula_menor = ""
while True:
     matricula = input()
     if matricula == "999":
         break
     cre = float(input())
     acumulador_cre += cre
     contador_cre += 1
     if cre < menor_cre:
         menor_cre = cre
         matricula_menor = matricula
     media = acumulador_cre/contador_cre
print(matricula_menor)
print("%0.2f" %media)

