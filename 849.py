def VolumeEsfera(raio):
     volume =  ((12.5664*(raio**3))/3)
     return("%.2f" %round(volume,2))
    
raio1 = float(input())
raio2 = float(input())
raio3 = float(input())

print(VolumeEsfera(raio1))
print(VolumeEsfera(raio2))
print(VolumeEsfera(raio3))
