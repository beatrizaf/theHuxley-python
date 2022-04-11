nota1 = int(input())
nota2 = int(input())
nota3 = int(input())
if (nota1 >= 0) and (nota2 >= 0) and (nota3 >= 0) and (nota1 <= 100) and (nota2 <= 100) and (nota3 <= 100):
     media = (nota1 + nota2 + nota3) / 3
     if (media >= 70) and (media <= 100):
         print("A media do aluno foi","%.2f" %media,"e ele foi APROVADO")
     elif (media >= 0) and (media < 40):
         print("A media do aluno foi","%.2f" %media,"e ele foi REPROVADO")
     elif (media >= 40) and (media < 70):
         print("A media do aluno foi","%.2f" %media,"e ele foi FINAL")
else:
     print("Media invalida")
