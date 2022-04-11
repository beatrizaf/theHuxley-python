n = int(input()) 

while n != -1:
     contador=0
     for i in range(1,n+1):
         if n%i==0:
             contador=contador+1
     if n==1 or n==0:
         print(0)
     elif contador>2:
         print(0)
     elif contador==2:
         print(1)
     n = int(input())
                 
