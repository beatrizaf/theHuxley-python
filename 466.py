destino = 'SEM DESTINO'
distanciaDestino = 0
while True:
    cidade = input()
    cidade = cidade.upper()
    if (cidade) == 'FIM':
        break

    distancia = int(input())
    valor  = int(input())
    valor *=2

    if distanciaDestino < distancia and valor <= 300:
        distanciaDestino = distancia
        destino = cidade
print (destino)
