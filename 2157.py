def linhas_iguais(x,count):
    for i in range(len(x[0])):
        compara = x[i]
        for j in range(len(x[0])):
            if i != j:
                if compara == x[j]:
                  count += 1
    return(count)
matriz = []
matrizTransposta = []
determinante = ""
cont = 0
count = 0
while True:
     elementos = input()
     if elementos == "acabou":
         break
     x = elementos.split()
     matriz.append(x)
     cont += 1
if cont == len(matriz[0]):
    for i in range(len(matriz[0])):
        somalinha = 0
        somacoluna = 0
        l = []
        for j in range(len(matriz[0])):
            somalinha += int(matriz[i][j])
            somacoluna += int(matriz[j][i])
            l.append(matriz[j][i])
        matrizTransposta.append(l)
        if somalinha == 0 or somacoluna == 0:
            determinante = "Zero"
    if (determinante == "Zero") or (linhas_iguais(matriz,count) > 1) or (linhas_iguais(matrizTransposta,count) > 1):
        print("Determinante zero.")
    else:
        print("Determinante diferente de zero.")
else:
     print("O determinante de uma matriz s� existe para matrizes quadradas.")
