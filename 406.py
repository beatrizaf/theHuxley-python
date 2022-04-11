numero= int(input())
numero1= int(input())
soma= 0
if numero > numero1:
     for i in range(numero,numero1-1,-1):
         if i>0:
             soma+=i
else:
     for i in range(numero,numero1+1):
         if i>0:
             soma+=i
print(soma)
