delator = input()

if (delator == "roubo") or (delator == "tr�fico") or (delator == "homic�dio"):
     if delator == "roubo":
         valor1 = int(input())
         delatado = input()
         if (delatado == "roubo") or (delatado == "tr�fico") or (delatado == "homic�dio"):
             if delatado == "roubo":
                 valor2 = int(input())
                 if valor2 > valor1 * 5:
                     print("Dela��o concedida.")
                 else:
                     print("Dela��o rejeitada.")
                     
             elif delatado == "homic�dio":
                 print("Dela��o concedida.")
                 
             elif delatado == "tr�fico":
                 valor2 = int(input())
                 if valor2 > valor1 * 3:
                     print("Dela��o concedida.")
                 else:
                     print("Dela��o rejeitada.")
             else:
                 print("Dela��o rejeitada.") 
                     
         else:
             print("Crime inv�lido.")
     if delator == "tr�fico":
         valor1 = int(input())
         delatado = input()
         if (delatado == "roubo") or (delatado == "tr�fico") or (delatado == "homic�dio"):
             if delatado == "homic�dio":
                 print("Dela��o concedida.")
            
             elif delatado == "tr�fico":
                 valor2 = int(input())
                 if valor2 > valor1 * 5:
                     print("Dela��o concedida.")
                 else:
                     print("Dela��o rejeitada.")
             else:
                 print("Dela��o rejeitada.")
             
         else:
             print("Crime inv�lido.")
             
     if delator == "homic�dio":
         delatado = input()
         if (delatado == "roubo") or (delatado == "tr�fico") or (delatado == "homic�dio"):
             if delatado == "homic�dio":
                 print("Dela��o concedida.")
             else:
                 print("Dela��o rejeitada.")
         else:
             print("Crime inv�lido.")
else:
     print("Crime inv�lido.")
