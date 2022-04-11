def contagem(num):
     cont = 0
     for i in range(num-1):
         x = num - cont
         for j in range(x-1):
             print(x,end="-")
         print(x)
         cont+=1
     return(1)
num = int(input())
print(contagem(num))
