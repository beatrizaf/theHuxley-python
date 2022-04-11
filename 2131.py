princesas = int(input())
eleitores = int(input())
cont = 0
m = [[0 for i in range(princesas)] for j in range(eleitores)]
for i in range(eleitores):
     p = input().split(" ")
     for j in range(princesas):
         m[i][j] = p[j]
for j in range(princesas):
     for i in range(eleitores):
       if m[i][j] == "1":
         cont+=1
     print("Princesa",str(j+1)+":",cont,"voto(s)")
     cont = 0
