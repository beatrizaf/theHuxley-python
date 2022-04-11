quantidade = int(input())
strings = []
for i in range(quantidade):
     strings.append(input())
for i in range(len(strings)):
     if str(strings[i].lower().replace(" ","")) == str(strings[i][::-1].lower().replace(" ","")):
         print("SIM")
     else: 
         print("NAO")
     
