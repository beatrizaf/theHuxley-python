opcao = input()
if (opcao == "C") or (opcao == "BF") or (opcao == "BS"):
     pao = input() 
     bebidaa = input()
     bebidac = input()
     quantidadec = int(input())
     quantidadea = int(input())
     if opcao == "C":
         conta = (quantidadea * 6.4) + (quantidadea * 1.8) + (quantidadea * 1.5) + (quantidadec * 6.4)
     elif opcao == "BF":
         conta = (quantidadea * 8) + (quantidadea * 2.7) + (quantidadec * 6.4)
     elif opcao == "BS":
         conta = (quantidadea * 8) + (quantidadea * 2.25) + (quantidadec * 6.4)
     if bebidaa == "S":
         conta = conta + (quantidadea * 16)
     else:
         conta = conta
     if bebidac == "S":
         conta = conta + (quantidadec * 3)
     else:
         conta = conta
     if pao == "N":
         conta = conta - (conta * 0.02)
     else:
         conta = conta
     print("R$:","%.2f" %conta)
else:
     print("Op��o inv�lida.")
