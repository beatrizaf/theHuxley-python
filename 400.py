def CalculaMulta(km):
    if km <= 50:
        return(0.00)
    if km > 50 and km <= 55:
         return(230.00)
    elif km > 55 and km <= 60:
         return(340.00)
    else:
         return((km - 50) * 19.28)

km = int(input())
print("%.2f" %CalculaMulta(km))
