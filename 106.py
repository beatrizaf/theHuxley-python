while True:
    numero = int(input())
    if (numero == 0 or numero < 0 or numero > 47):
        break
    sequencia = ""
    t1 = 0
    t2 = 1
    sequencia += str(t1)
    for i in range (1 , numero):
        c = t1
        t1 = t2
        t2 = t1 + c
        sequencia += " "+ str(t1) 
    print (sequencia)
