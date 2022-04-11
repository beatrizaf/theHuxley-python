def EstacaoAno(dia,mes):
     if (mes == 1) or (mes == 2) or ((mes == 3) and (dia <= 20)):
         return("VERAO")
     elif ((mes == 3) and (dia > 20)) or (mes == 4) or (mes == 5) or ((mes == 6) and (dia <= 20)):
         return("OUTONO")
     elif ((mes == 6) and (dia > 20)) or (mes == 7) or (mes == 8) or ((mes == 9) and (dia <= 20)):
         return("INVERNO")
     else:
         return("PRIMAVERA")

dia = int(input())
mes = int(input())
print(EstacaoAno(dia,mes))
