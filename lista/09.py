#Faça um Programa que leia um vetor A com 10 números inteiros, 
#calcule e mostre a soma dos quadrados dos elementos do vetor.
A = []
for i in range(10):
	A.append(int(input('digite um numero:')))
  
soma = 0
for j in A:
  soma = soma + j ** 2
print(soma)
  