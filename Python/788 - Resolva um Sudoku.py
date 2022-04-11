def pos_valida(sud, linha, coluna, elemento):

    if elemento in sud[linha]:
        return False 

    col = []
    for lin in range(9):
        col.append(sud[lin][coluna])
    if elemento in col:
        return False

    lin_ini = (linha // 3) * 3 
    col_ini = (coluna // 3) * 3
    for l in range(lin_ini, lin_ini + 3):
        for c in range(col_ini, col_ini + 3):
            if sud[l][c] == elemento:
                return False 

    return True  

def preenche(sud):
    
    linha = -1
    for i in range(9):
        for j in range(9):
            if sud[i][j] == 0:
                linha = i
                coluna = j
                
    if linha == -1:
        return True

    for elemento in range(1, 10):
        if pos_valida(sud, linha, coluna, elemento):
            sud[linha][coluna] = elemento
            if preenche(sud):
                return True 
        sud[linha][coluna] = 0
        
    return False

n = int(input())
for i in range(n):
    sud = []
    for j in range(9):
        linha = input()
        sud.append(list(map(int,linha)))
        
    preenche(sud)
    
    for i in sud:
        for j in i:
            print(j, end="")
        print()

