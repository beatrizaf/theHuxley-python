TVideo = float(input())
TAudio = float(input())
TDados = float(input())
Capacidade = float(input())
if (Capacidade > 0):
     QDmax = (TVideo*5.2 + TAudio*3.4 + TDados*1.5) / Capacidade
     print(round(QDmax, 2))
