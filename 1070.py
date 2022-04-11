dia = input()
preco = float(input())
opcao = input()
nome = input()
if (dia == "seg") or (dia == "ter") or (dia == "qua"): 
     if (opcao == "ouro"):
         preco1 = preco / 2
         print("O preco do produto",nome,"no dia",dia,"eh",round(preco1,2))
     else:
         preco4 = preco * 2
         print("O preco do produto",nome,"no dia",dia,"eh","%.2f" %preco4)
if (dia == "qui") or (dia == "sex"):
     if (preco > 10) and (preco < 100):
         preco2 = preco /3
         print("O preco do produto",nome,"no dia",dia,"eh","%.2f" %preco2)
     else:
         preco4 = preco * 2
         print("O preco do produto",nome,"no dia",dia,"eh","%.2f" %preco4)
if (dia == "sab"):
     if (opcao == "prata"):
         preco3 = preco * 3
         print("O preco do produto",nome,"no dia",dia,"eh","%.2f" %preco3)
     else:
         preco4 = preco * 2
         print("O preco do produto",nome,"no dia",dia,"eh","%.2f" %preco4)
if (dia == "dom"):
     preco4 = preco * 2
     print("O preco do produto",nome,"no dia",dia,"eh","%.2f" %preco4)
