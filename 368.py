salario = float(input())
if salario > 500:
     aumento = salario + (salario * (10/100))
     print("%.2f" %aumento)
elif (salario > 300) and (salario < 500):
     aumento = salario + (salario * (7/100))
     print("%.2f" %aumento)
else:
     aumento = salario + (salario * (5/100))
     print("%.2f" %aumento)
