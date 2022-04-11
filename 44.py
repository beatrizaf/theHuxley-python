listan = []
for i in range(3):
  listan.append(int(input()))
 
interm = 0
for j in range(len(listan)):
  if (listan[0] > listan[1] and listan[0]<listan[2]) or (listan[0] < listan[1] and listan[0] > listan[2]):
    interm = listan[0]
  elif (listan[1] > listan[0] and listan[1] < listan[2]) or (listan[1] < listan[0] and listan[1] > listan[2]):
    interm = listan[1]
  else:
    interm = listan[2]

print(interm)
       
