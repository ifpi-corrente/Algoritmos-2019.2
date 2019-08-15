dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))

if (dia > 0 and dia < 32):
    validadedia = True
else:
    validadedia = False

if (mes > 0 and mes < 13):
    validademes = True
else:
    validademes = False
    
if (ano> 1000 and ano < 9999):
    validadeano = True
else:
    validadeano = False
    
if (validadedia == True and validademes == True and validadeano == True):
    print("Data válida!!")
else:
    print("Data inválida!")