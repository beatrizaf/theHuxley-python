def MesCorrespondente(mes):
     if mes == 1:
         return("janeiro")
     elif mes == 2:
         return("fevereiro")
     elif mes == 3:
         return("marco")
     elif mes == 4:
         return("abril")
     elif mes == 5:
         return("maio")
     elif mes == 6:
         return("junho")
     elif mes == 7:
         return("julho")
     elif mes == 8:
         return("agosto")
     elif mes == 9:
         return("setembro")
     elif mes == 10:
         return("outubro")
     elif mes == 11:
         return("novembro")
     elif mes == 12:
         return("dezembro")
     else:
         return("invalido")
         
mes = int(input())
print(MesCorrespondente(mes))
     
