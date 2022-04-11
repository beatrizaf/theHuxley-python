n1 = int(input())
n2 = int(input())
n3 = int(input())
p1 = int(input())
p2 = int(input())
p3 = int(input())

if (n1 >= 1) and (n2 >= 1) and (n3 >= 1) and (n1 <= 100) and (n2 <= 100) and (n3 <= 100):
     if (p1 >= 1) and (p2 >= 1) and (p3 >= 1) and (p1 <= 10) and (p2 <= 10) and (p3 <= 10):
         media_a = (n1 + n2 + n3) / 3
         media_p = (n1*p1 + n2*p2 + n3*p3) / (p1 + p2 + p3)
         media_h = 3 / (1/n1 + 1/n2 + 1/n3)
         print("a:",round(media_a,1))
         print("p:",round(media_p,1))
         print("h:",round(media_h,1))
