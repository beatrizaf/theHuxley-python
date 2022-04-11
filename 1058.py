import math
temperatura = float(input())
massa = float(input())

if (temperatura >= 0.0) and (temperatura <= 200.0) and (massa >= 1.0) and (massa <= 200.0):
     velocidade = math.sqrt((3* 8.31 * temperatura) / massa)
     print(round(velocidade,2))
