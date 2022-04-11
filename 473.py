aprovador = 0
while True:
     p_certas = int(input())
     if p_certas < 0:
         break
     m_certas = int(input())
     redacao = float(input())
     
     if (p_certas >= 40) and (m_certas >= 21) and (redacao>= 7):
        aprovador += 1
print(aprovador)

