#Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

n = int(input("Informe N: "))

i = 0
menor = 0
maior = 0
soma = 0
while i < n:
    x = float(input("Digite um número: "))
    if i == 0:
        menor = x
        maior = x
    
    soma = soma + x
    if x > maior:
        maior = x
    if x < menor:
        menor = x
    i = i + 1
print(menor)
print(maior)
print(soma)