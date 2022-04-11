def Media(a,b,c,d):
     media = ((a*1) + (b*2) + (c*3) + (d*4))/ 10
     if media >= 9.0:
         return("aprovado com louvor")
     elif media >= 7.0:
         return("aprovado")
     elif (media >= 3.0) and (media < 7.0):
         return("prova final")
     else:
         return("reprovado")
notas = input().split()
aluno = Media(float(notas[0]),float(notas[1]),float(notas[2]),float(notas[3]))
print(aluno)
