def digitos(string):
     cont = 0
     for i in range(len(string)):
        if string[i] in "0123456789":
             cont += 1
     return(cont)
         
string = input()
print(digitos(string))
