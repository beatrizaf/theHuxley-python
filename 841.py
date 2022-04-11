n1 = float(input())
n2 = float(input())
n3 = float(input())

if (n1 <= 10.0) and (n2 <= 10.0) and (n3 <= 10.0):
     media = (n1 + n2 + n3)/3
     if (n1 > media) and (n2 > media) and (n3 > media):
         print("3")
     elif ((n1 > media) or (n2 > media)) and (n3 > media):
         print("2")
     elif (n1 > media) and ((n2 > media) or (n3 > media)):
         print("2")
     elif (n2 > media) and ((n1 > media) or (n3 > media)):
         print("2")
     elif (n1 > media) and (n2 < media) and (n3 < media):
         print("1")
     elif (n1 < media) and (n2 > media) and (n3 < media):
         print("1")
     elif (n1 < media) and (n2 < media) and (n3 > media):
         print("1")
     else:
         print("0")
