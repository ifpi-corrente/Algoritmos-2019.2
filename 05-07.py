#5.7.Crie um programa que imprime os números pares de 0 até um número digitado

x = int(input("Digite um número: "))
y = 0
while y <= x:
    if (y % 2) == 0:
        print(y)
        y += 1
    else:
        y +=1
     