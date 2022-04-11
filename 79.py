while True:
    num = int(input())
    aux = ""
    if num == 0:
        break
    m = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    for j in range(4):
        i = 0
        while i < 4:
          elemento = int(input())
          m[i][j] = elemento
          i+=1
    for i in range(4):
        for j in range(4):
            if i == j:
              m[i][j] = m[i][j]*num
            aux += str(m[i][j]) + " "
        print(aux)
        aux = ""
