fat = 0
def Fatorial(num):
     if num == 1 or num == 0: 
         return 1
     else: 
         return num * Fatorial(num - 1)
for i in range(5):
     num = int(input())
     if num % 3 == 0:
         fat += Fatorial(num)
print(fat)
