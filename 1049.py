massa = float(input())
altura = float(input())
if (massa > 1) and (massa < 500) and (altura > 1) and (altura < 2.8):
    imc = massa / (altura**2)
    print("%.2f" %imc)
