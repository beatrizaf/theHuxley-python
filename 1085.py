p1 = int(input())
p2 = int(input())
p3 = int(input())
p4 = int(input())
x = int(input())
if (p1 >= -10) and (p1 <= 10) and (p2 >= -10) and (p2 <= 10) and (p3 >= -10) and (p3 <= 10) and (p4 >= -10) and (p4 <= 10) and (x >= -10) and (x <= 10):
     polinomio = (p1 * (x**3)) + (p2 * (x**2)) + (p3 * x) + p4
     print(polinomio)
