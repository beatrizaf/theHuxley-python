numero_glicose = -1
contador = 0
acumulador = 0
while numero_glicose != 0:
     numero_glicose = int(input())
     acumulador += numero_glicose 
     contador += 1 
media = acumulador/(contador-1) 
if media < 110:
     print("Glicose Normal")
elif media >= 200:
     print("Glicose Muito Alta")
else:
     print("Glicose Alterada")
