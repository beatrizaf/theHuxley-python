print("Informe a primeira nota:")
print("Informe a segunda nota:")
print("Informe a terceira nota:")

n1 = float(input())
n2 = float(input())
n3 = float(input())

media = (n1 + n2 + n3)/3

if media >= 7.0:     
     print("Aprovado com media", "%.1f" % round(media,1))
     
elif (media >= 5.0) and (media < 7.0):
     print("Recuperacao com media", "%.1f" % round(media,1))
     
elif (media < 5.0):
     print("Reprovado com media", "%.1f" % round(media,1))
