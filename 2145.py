nacionalidade = input()
ocupacao = input()
q_armas = int(input())
calibre = int(input())

if (q_armas == 0) and (calibre == 0):
     print("Liberado")
elif (nacionalidade == "E") and (q_armas == 0):
     print("Liberado")
elif nacionalidade == "B":
     if ocupacao == "M":
         print("Liberado")
     elif ((ocupacao == "T") or (ocupacao == "O")) and (q_armas <= 1) and (calibre <= 22):
         print("Liberado")
     elif (ocupacao == "C") and (q_armas <= 2) and (calibre <= 38):
         print("Liberado")
     else:
         print("Barrado")
else:
     print("Barrado")
   
