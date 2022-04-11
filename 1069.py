forma = input()
if (forma == "Q") or (forma == "R") or (forma == "C"):  
     if (forma == "Q"):
         lado = float(input())
         areaq = lado * lado
         perimetroq = lado * 4
         print("%.2f" %areaq)
         print("%.2f" %perimetroq)
         
     elif (forma == "R"):
         altura = float(input())
         largura = float(input())
         arear = altura * largura
         perimetror = (altura * 2) + (largura * 2)
         print("%.2f" %arear)
         print("%.2f" %perimetror)
         
     elif (forma == "C"):
         raio = float(input())
         areac = 3.14 * (raio**2)
         comprimento = 2 * 3.14 * raio
         print("%.2f" %areac)
         print("%.2f" %comprimento)
else:
     print("Nenhuma figura selecionada")
