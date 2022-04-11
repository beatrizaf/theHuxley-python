nome = " "
menor_ponto = 10000000
nome_domenor = " "
maior_ponto = -1
nome_domaior = " "
contador_jogador = 0
acumulador_pontos = 0
media = 0
while True:
     nome = input()
     if nome == "sair":
         break
         print("Nenhum jogador foi registrado.")
     pontuacao = int(input())
     contador_jogador += 1
     acumulador_pontos += pontuacao
     if pontuacao <= menor_ponto:
         menor_ponto = pontuacao
         nome_domenor = nome
     if pontuacao >= maior_ponto:
         maior_ponto = pontuacao
         nome_domaior = nome
if contador_jogador <=0:
     print("Nenhum jogador foi registrado.")
else:
     media = acumulador_pontos/contador_jogador
     print(nome_domenor)
     print(nome_domaior)
     print("%.2f" %media)
