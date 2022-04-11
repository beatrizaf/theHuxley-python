temperatura = float(input())
s_t_d = input()
if (temperatura >= 35) and (temperatura <= 41):
     if (s_t_d == "S") or (s_t_d == "N"):
         if (temperatura >= 37) and (s_t_d == "S"):
             print("Exames Especiais")
         elif (temperatura >= 37) and (s_t_d == "N"):
             print("Exames Basicos")
         elif (temperatura < 37) and (s_t_d == "N"):
             print("Liberado")
         elif (temperatura < 37) and (s_t_d == "S"):
             print("Exames Basicos")
     else:
         print("Erro")
