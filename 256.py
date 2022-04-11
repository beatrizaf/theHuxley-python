a1=[]
a2=[]
a_int=[]
n=int(input())
c1=0
c2=0
while(c1 <n):
  c1+=1
  y=int(input())
  a1.append(y)
while(c2 <n):
  c2+=1
  y=int(input())
  a2.append(y)
for i,f in zip(a1,a2):
  a_int.append(i)
  a_int.append(f)
for a in a_int:
  print(a)
