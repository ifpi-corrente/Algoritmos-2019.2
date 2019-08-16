n = int(input("Digite um número inteiro: "))

i = 2
quantidade = 0

while i < n:
    if n % i == 0:
        print(i)
        quantidade = quantidade + 1 
    i = i + 1

if quantidade == 0:
    print("Esse número é primo")
else:
    print(1)
    print(n)
    print("Esee número não é primo")
    