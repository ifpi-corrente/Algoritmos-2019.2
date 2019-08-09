#4.3. Escreva um programa que leia três números e que imprima o maior e o menor.
a = float(input("Digite um número: "))
b = float(input("Digite um número: "))
c = float(input("Digite um número: "))

if (a > b > c): # if (a>b and b > c)
    print(f"{a} é maior e {c} é menor")
if (a > c > b):
    print(f"{a} é maior e {b} é menor")
if (b > a > c):
    print(f"{b} é maior e {c} é menor")
if (b > c > a):
    print(f"{b} é maior e {a} é menor")
if (c > a > b):
    print(f"{c} é maior e {b} é menor")
if (c > b > a):
    print(f"{c} é maior e {a} é menor")