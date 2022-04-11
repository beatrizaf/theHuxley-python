bandejas = int(input())
bandeja = []
contador = 0
if (bandejas >= 1) and (bandejas <= 100):
     for i in range(bandejas):
         LC = input().split(" ")
         bandeja.append(LC)
     for i in range(len(bandeja)):
         if int(bandeja[i][0]) > int(bandeja[i][1]):
             contador += int(bandeja[i][1])
     print(contador)
