def maior (a,b,c):
     a = int(a)
     b = int(b)
     c = int(c)
     if a > b and a > c:
       return(a)
     elif b > a and b > c:
       return(b)
     else:
       return(c)
a,b,c = input().split(" ")
print(maior(a,b,c),"eh o maior")
