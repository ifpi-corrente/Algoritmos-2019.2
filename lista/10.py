#Faça um Programa que leia dois vetores com 10 elementos cada. 
#Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos 
#pelos elementos intercalados dos dois outros vetores.

numeros1 = []
numeros2 = []

for i in range(10):
  numeros1.append(int(input('Digite um número para primeiro vetor: ')))

print(numeros1)
  
for i in range(10):
  numeros2.append(int(input('Digite um número para segundo vetor: ')))

print(numeros2)
  
numeros3 = []

for j in range(10):
  numeros3.append(numeros1[j])
  numeros3.append(numeros2[j])

print(numeros3)