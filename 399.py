def CalculaHospedagem(apartamento,dias):
     if apartamento == "individual":
         if dias >= 3:
             total = 125*dias - (125*dias* 0.15)
             return("%.2f"%total)
         total = 125*dias
         return("%.2f"%total)
     elif apartamento == "su�te dupla":
         if dias >= 3:
             total = 140*dias - (140*dias* 0.15)
             return("%.2f"%total)
         total = 140*dias
         return("%.2f"%total)
     elif apartamento == "su�te tripla":
         if dias >= 3:
             total = 180*dias - (180*dias* 0.15)
             return("%.2f"%total)
         total = 180*dias
         return("%.2f"%total)
apartamento = input().lower()
dias = int(input())
print(CalculaHospedagem(apartamento,dias))
