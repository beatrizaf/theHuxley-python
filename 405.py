def ContaDigitosPares(num,cont):
     if len(num) == 0:
         return cont
     else:
         if int(num[0]) % 2 == 0:
             cont+=1
         return(ContaDigitosPares(num[1:],cont))
num = input()
cont = 0
print(ContaDigitosPares(num,cont))
