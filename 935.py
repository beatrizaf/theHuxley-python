n1 = float(input())
n2 = float(input())
n3 = float(input())

media = (n1 + n2 + n3)/3
if media >= 7.0:     
     print("Informe a primeira nota:")
     print("Informe a segunda nota:")
     print("Informe a terceira nota:")
     print("Aprovado com media",media)
elif (media >= 5.0) and (media < 7.0):
     print("Informe a primeira nota:")
     print("Informe a segunda nota:")
     print("Informe a terceira nota:")
     print("Recuperacao com media",media)
elif (media < 5.0):
     print("Informe a primeira nota:")
     print("Informe a segunda nota:")
     print("Informe a terceira nota:")
     print("Reprovado com media",media)
