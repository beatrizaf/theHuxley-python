def ProdutoPrimos(a,b,c,d):
     a = int(a)
     b = int(b)
     c = int(c)
     d = int(d)
     if ((a == 1) or (a == -1) or (a == 0)) or ((b == 1) or (b == -1) or (b == 0)) or ((c == 1) or (c == -1) or (c == 0)) or ((d == 1) or (d == -1) or (d == 0)):
         return("SEM PRODUTO")
     elif (a%2==1 or a == 2) and (b%2==1 or b ==2) and (c%2==1 or c ==2) and (d%2==1 or d==2):
         return(a*b*c*d)
     else:
         return("SEM PRODUTO")
        
a,b,c,d = input().split(" ")
print(ProdutoPrimos(a,b,c,d))
