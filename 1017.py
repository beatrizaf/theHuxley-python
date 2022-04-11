fib = 0
def Fibonacci(num):
     if num <= 1:
         return num
     else:
         return Fibonacci(num-1) + Fibonacci(num-2)
num = int(input())
for i in range(num):
     fib = Fibonacci(i)
print(fib)

     
