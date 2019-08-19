import math

a=int(input("Digite o valor de a: "))
b=int(input("Digite o valor de b: "))
c=int(input("Digite o valor de c: "))
delta = b**2 - 4 * a * c
if delta < 0:
    print('Impossivel Calcular')
else:
    x1 = (-b + math.sqrt(delta))/(2 * a)
    x2 = (-b - math.sqrt(delta))/(2 * a)
    if delta == 0:
        print(x1)
    else:
        print(x1)
        print(x2)
    
  