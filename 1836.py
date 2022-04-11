lista = ["0","1","2","3","4","5","6","7","8","9"]
while True:
     string = input()
     if string == "FIM":
         break
     string2 = ""
     for i in range(len(string)):
         if string[i] == "o":
             string2 += "0"
         elif string[i] == "O":
             string2 += "0"
         elif string[i] == "l":
             string2 += "1"
         elif string[i] in lista:
             string2 +=  string[i]
         else:
             string2 = "ERRO"
             break
     print(string2.lstrip("0"))  
