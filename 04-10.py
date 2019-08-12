consumo = float(input("Digite o consumo em kWh: "))
instalacao = input("Diga a instalação: (I) Industrial, (R)Residencial e (C)Comércio: ")

if (instalacao == 'R' or instalacao == 'r'):
    if (consumo <= 500):
        valor = consumo * 0.40
    else:
        valor = consumo * 0.65
elif (instalacao == 'C' or instalacao == 'c'):
    if (consumo <= 1000):
        valor = consumo * 0.55
    else:
        valor = consumo * 0.60
elif (instalacao == 'I' or instalacao == 'i'):
    if (consumo <= 5000):
        valor = consumo * 0.55
    else: 
        valor = consumo * 0.60