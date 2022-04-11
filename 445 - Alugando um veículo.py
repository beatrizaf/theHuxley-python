dias = int(input())
km = int(input())


if (km <= dias * 100):
    custo = dias * 90
    
else:
    km_extra = km - (dias * 100)
    custo = (dias * 90) + (km_extra * 12) 
     
print("%.2f" %custo)
