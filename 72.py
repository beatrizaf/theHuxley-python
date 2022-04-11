x=int(input())
y=input()
y=y.split()
z=""
for i in range( x-1, -1 ,-1):
  if(i!=0):
    z+=y[i]+" "
  else:
    z+=y[i]
print(z)
