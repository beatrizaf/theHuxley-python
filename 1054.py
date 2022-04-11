raio = float(input())
angulo = float(input())
if (raio > 1.0) and (raio < 50.0) and (angulo > 0.0) and (angulo < 359.0):
     comprimento_arco = (angulo * 3.14 * raio) / 180
     area_setor = (angulo * 3.14 * raio**2) / 360
     print(round(comprimento_arco,2))
     print(round(area_setor,2))
