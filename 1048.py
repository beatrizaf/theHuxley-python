salario = float(input())
hora_extra = int(input())
if (salario > 1000.00) and (salario < 10000.00) and (hora_extra >= 0) and (hora_extra <= 50):
     valor_hora = salario / 44
     salario_total = salario + (valor_hora * hora_extra) + (valor_hora * hora_extra * 0.1)
     print("%.2f" %salario_total)
