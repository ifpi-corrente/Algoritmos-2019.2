#Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
numeros = []

for i in range(10):
    numeros.append(float(input("Digite um valor: ")))

for i in range(10):
    print(numeros[-i-1])
