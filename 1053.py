altura = float(input())
raio = float(input())
area_b = 3.14 * (raio**2)
volume = area_b * altura
area_s = (altura * (2 * 3.14 * raio)) + (2 * 3.14 * raio**2)
print("%.2f" %volume)
print("%.2f" %area_s)
