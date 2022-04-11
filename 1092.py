homens = 0
mulheres = 0 
acumulador_salariom = 0
acumulador_salariof = 0
maior_salario = 0
maior_sexo = " "
mediam = 0
for i in range(1,10+1):
     salario = float(input())
     sexo = input()
     if salario > maior_salario:
         maior_salario = salario
         maior_sexo = sexo
     if sexo == "m":
         homens += 1
         acumulador_salariom += salario
     else:
         mulheres+=1
         acumulador_salariof += salario
media = (acumulador_salariom + acumulador_salariof)/10
if homens == 0:
     print("0")
else:
     mediam = acumulador_salariom/homens
print(homens)
print(mulheres)
print("%.1f" %media)
print(maior_sexo)
print("%.1f" %mediam)
