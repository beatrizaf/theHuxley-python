def leet(string):
     string_aux = ""
     cont = 0
     if len(string) == 0:
         print("numeros")
         return 0
     for i in range(len(string)):
         if string[i] in "0123456789":
             print("numeros")
             return 0
         else:
             if string[i] == "a":
                 string_aux += "@"
                 cont += 1
             elif string[i] == "e":
                 string_aux += "3"
                 cont += 1
             elif string[i] == "i":
                 string_aux += "1"
                 cont += 1
             elif string[i] == "o":
                 string_aux += "0"
                 cont += 1
             elif string[i] == "t":
                 string_aux += "7"
                 cont += 1
             elif string[i] == "s":
                 string_aux += "5"
                 cont += 1
             else:
                 string_aux += string[i]
     print(string_aux[::-1])
     return(cont)
string = input().lower()
print(leet(string))
