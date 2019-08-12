import math

a = float(input("Digite o valor de a: "))
if (a == 0 ):
    print("A equação não é do 2 grau.")
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    delta = (b ** 2) - 4 * a * c 
    if delta < 0:
        print("Não tem raizes")
    elif delta == 0 :
        print("A equação possui 1 raiz real")
        print(f"O valor de delta é {delta}")
        raiz = -b / 2 * a
        print(f"A raiz é {raiz}")
    else:
        print("A equação possui 2 raizes reais.")
        print(f"O valor de delta é {delta}")
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Raiz 1 é {raiz1} e raiz 2 é {raiz2}")
        