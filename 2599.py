matriz = []
menor = 99999.0
meses = ["Janeiro","Fevereiro","Marco","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
dias = ["Primeiro","Primeiro","Segundo","Segundo","Terceiro","Terceiro","Quarto","Quarto"]
nomes_dias = ["Sabado","Domingo","Sabado","Domingo","Sabado","Domingo","Sabado","Domingo",]
for i in range(12):
     elemento = input().split()
     matriz.append(elemento)
     for j in range(8):
         if float(matriz[i][j]) <= 0.5:
             if float(matriz[i][j]) < menor:
                 menor = float(matriz[i][j])
                 mes = i
                 x = j
if menor ==  99999.0:
     print("Proximo ano eu tento denovo...")
else:
     print("O melhor dia e no",dias[x],nomes_dias[x],"de",meses[mes])
