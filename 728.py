def velkmh(velocidadei,aceleracao,tempo):
     velocidadef = (velocidadei + aceleracao * tempo) * 3.6
     return velocidadef

l = []
for i in range(3):
     velocidadei = float(input())
     aceleracao = float(input())
     tempo = float(input())
     v = velkmh(velocidadei,aceleracao,tempo)
     l.append(v)
if l[0] < l[1] and l[0] < l[2]:
     print(l[0])
elif l[1] < l[0] and l[1] < l[2]:
     print(l[1])
else:
     print(l[2])
