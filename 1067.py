caracter = input()
if len(caracter) == 1:
     if (caracter == "a") or (caracter == "e") or (caracter == "i") or (caracter == "o") or (caracter == "u") or (caracter ==  "A") or (caracter == "E") or (caracter == "I") or (caracter == "O") or (caracter == "U"):
         print("Eh vogal")
     else:
         print("Nao eh vogal")
else:
     print("1 caractere, por favor!")
