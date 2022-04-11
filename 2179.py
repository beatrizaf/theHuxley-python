def titulares(l):
     cont = 0 
     indice = 0 
     for i in range(len(l)):
         if l[i] == 0:
             cont+=1
     if cont < 2:
         indice = l[0]*2 + l[1]*3.5 + l[2]*1.5 + l[3]*2
     return indice 
l = []
t = []
for i in range(5):
     nome = input()
     for i in range(4):
         l.append(int(input()))
     t.append(titulares(l))
     t.sort()
     l = []
print(t[4])
print(t[3])
print(t[2])
