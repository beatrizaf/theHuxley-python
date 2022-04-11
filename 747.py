n = int(input())
for i in range(n):
     string = input()
     s = ""
     for j in range(0, len(string)-1):
         if string[j] != string[j+1]:
             s += string[j]
     s += string[len(string) -1]
     print(s)
    
