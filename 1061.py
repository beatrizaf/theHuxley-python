raio_circulo1 = float(input())
raio_circulo2 = float(input())
area_circulo1 = 3.14 * (raio_circulo1 ** 2)
area_circulo2 = 3.14 * (raio_circulo2 ** 2)

if (area_circulo1 > area_circulo2):
     print("Primeiro circulo")
elif (area_circulo1 < area_circulo2):
     print("Segundo circulo")
else:
     print("Iguais")
