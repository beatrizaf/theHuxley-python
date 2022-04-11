codigo = int(input())
if (codigo == 1):
     print("Nordeste")
elif (codigo == 2):
     print("Norte")
elif (codigo == 3) or (codigo == 4):
     print("Centro-Oeste")
elif (codigo >= 5) and (codigo <= 9):
     print("Sul")
elif (codigo >= 10) and (codigo <= 15):
     print("Sudeste")
