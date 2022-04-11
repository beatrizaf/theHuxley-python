numero1 = int(input())
numero2 = int(input())
if numero1 > numero2:
     for i in range(numero1,numero2-1,-1):
         contador=0
         for j in range(1,i+1):
             if i%j==0:
                 contador=contador+1
         if contador==2:
             print(i)
else:
     for i in range(numero2,numero1-1,-1):
         contador=0
         for j in range(1,i+1):
             if i%j==0:
                 contador=contador+1
         if contador==2:
             print(i)
