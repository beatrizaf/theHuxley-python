def Digitos(num,result):
     if len(num) == 0:
         return result
     else:
         if int(num[0]) % 2 == 0:
             result += int(num[0]) * 2 * len(num)
         else:
             result += int(num[0]) * 3 * len(num)
         return Digitos(num[1:],result)
while True:
     num = int(input())
     if num == 0:
         break
     result = 0
     num = str(num)
     if len(num) <= 9: 
         print(Digitos(num,result))
