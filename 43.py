numero1=int(input())
numero2=int(input())
numero3=int(input())
if (numero1==numero2==numero3): 
   print ("1")
elif (numero1!=numero2!=numero3):
     print ("2")
elif (numero1==numero2!=numero3) or (numero1!=numero2==numero3):
   print("3")
