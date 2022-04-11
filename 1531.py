time = input()
if (time == "GSW") or (time == "HOU") or (time == "CLE") or (time == "BOS"):
     jogador = input()
     tentado2 = int(input())
     convertidos2 = int(input())
     tentado3 = int(input())
     convertidos3 = int(input())
     pontos = (convertidos2 * 2) + (convertidos3 * 3)
     percentual2 = (convertidos2/ tentado2) * 100 
     percentual3 = (convertidos3/ tentado3) * 100 
     if pontos > 30:
         print("O time",time,"estah jogando, e",jogador,"estah indo bem.")
     elif (percentual2 > 50) and (tentado2 > 10):
         print("O time",time,"estah jogando, e",jogador,"estah indo bem.")
     elif (percentual3 > 40) and (tentado3 > 7):
         print("O time",time,"estah jogando, e",jogador,"estah indo bem.")
     else:
         print("O time",time, "estah jogando, mas",jogador,"nao estah indo bem.")
else:
     print("Nenhum time de interesse jogando.")
