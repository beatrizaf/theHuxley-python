vendas = 0
vendas_avista = 0.0
idade_menor = 111100000
maior_compra = 0
soma_avista = 0
media = 0
soma_cartao = 0
while True:
     idade = int(input())
     valor_compra = float(input())
     tipo_pagamento = input()
     resposta = input()
     vendas += 1
     if tipo_pagamento == "V":
         vendas_avista += 1
         soma_avista += valor_compra
         media = soma_avista/vendas_avista
     else: 
         soma_cartao +=valor_compra
     
     if idade < idade_menor:
         idade_menor = idade
         
     if valor_compra > maior_compra:
         maior_compra = valor_compra
         
     if resposta == "N":
         break
print(vendas)
if soma_avista == 0:
     print(soma_avista)
else:
     print("%.2f"  %soma_avista)
if soma_cartao == 0:
     print(soma_cartao)
else:
     print("%.2f"  %soma_cartao)
print(idade_menor)
print("%.2f"  %maior_compra)
if media == 0:
     print(media)
else:
     print("%.2f" %media)
