#Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1.

n = int(input("Digite um número inteiro: "))

i = 1
quantidade = 0

while i <= n:
    if n % i == 0:
        quantidade = quantidade + 1 
    i = i + 1

if quantidade == 2:
    print("Esse número é primo")
else:
    print("Esee número não é primo")
    