carros = 0 
carro_novo = 0
velocidade_maior = 0 
velocidade_acumulador = 0
while True:
     resposta = input()
     if resposta == "n" or resposta == "N":
         break
     ano = int(input())
     velocidade = float(input()) 
     carros += 1
     velocidade_acumulador += velocidade
     if ano > carro_novo:
         carro_novo = ano
     if velocidade > velocidade_maior:
         velocidade_maior = velocidade
if carros == 0:
     print("zero")
else:
     velocidade_media = velocidade_acumulador/carros
     print("%.2f"%velocidade_maior)
     print(carro_novo)
     print("%.2f"%velocidade_media)
