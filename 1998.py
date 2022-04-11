n1 = 0 
n2 = 0
while True:
     n1=int(input())
     if (n1 < 1) or (n1 >9):
         print("Insira um n�mero inicial entre 1 e 9")
     elif (n1>=1) and (n1<=9):
         n1 = n1
         break
while True:
     n2=int(input())
     if (n2 < 1) or (n2 >9):
         print("Insira um n�mero final entre 1 e 9")
     elif (n2>=1) and (n2<=9):
         n2 = n2
         break
if (n2>n1):
     for y in range(n1,n2+1):  
         for x in range(1,9+1):
             mult=x*y
             print('%.0f x %.0f = %.0f'%(y,x,mult))
         print('')
elif (n1==n2):
     for x in range(1,9+1):
         mult=n1*x
         print('%.0f x %.0f = %.0f'%(n1,x,mult))   
elif (n2<n1):
     print('Nenhuma tabuada nesse intervalo')                  
