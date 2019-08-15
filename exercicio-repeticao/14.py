#Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

i = 0
pares = 0
impares = 0
while i < 10:
    numero = int(input("Digite um número: "))
    if (numero % 2 == 0 and numero != 0):
        pares = pares + 1
    elif (numero % 2 != 0):
        impares = impares + 1
    i= i + 1

print("pares: {}".format(pares))
print("impares: {}".format(impares))