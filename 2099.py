situacao_medio = input()
encceja = input()
nota_encceja = int(input())
tipo_escola = input()
renda = float(input())

if (nota_encceja >= -1) and (nota_encceja <= 800):
     if (situacao_medio == "CLD") or (situacao_medio == "CVC") or (situacao_medio == "CSC") or (situacao_medio == "NCC"):
         if (encceja == "S") and (nota_encceja >= 400):
             print("Voce terah direito a isencao")
         elif (situacao_medio == "CVC") and (tipo_escola == "PUB"):
             print("Voce terah direito a isencao")
         elif (tipo_escola == "PUB") or (tipo_escola == "PCB") and (renda <= 1431):
             print("Voce terah direito a isencao")
         else:
             print("Infelizmente voce nao tem direito a isencao")
     else:
         print("Informacao sobre ensino medio invalida")
