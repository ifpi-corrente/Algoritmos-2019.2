#Faça um Programa que leia um vetor de 5 números inteiros, 
# mostre a soma, a multiplicação e os números.

numeros = []
soma = 0
multiplicacao = 1 
for i in range(5):
    numeros.append(int(input("Digite o número: ")))
    soma = soma + numeros[i]
    multiplicacao = multiplicacao * numeros[i]
print(f'Soma = {soma}')
print(f'Multiplicação = {multiplicacao}')
print(f'Números = {numeros}')
    
