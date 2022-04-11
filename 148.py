buracos = {'a':1,'b':2,'d':1,'o':1,'p':1,'q':1,'r':1}

T = int(input())

for i in range(T):

    texto = input()
    quant_buracos = 0

    for l in texto:
        if l.lower() in buracos.keys():
            quant_buracos += buracos[l.lower()]
    
    print(quant_buracos)
